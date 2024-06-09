from Cobol85Visitor import Cobol85Visitor
from Cobol85Parser import Cobol85Parser

class CustomVisitor(Cobol85Visitor):
    def __init__(self,parser,symbol_table):
        super().__init__()
        self.python_code = ""
        self.parser = parser
        self.symbol_table = symbol_table

    def get_python_code(self):
        return self.python_code
    #overide
    def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
        
        return self.visitChildren(ctx)
    
    # def visitDivideStatement(self, ctx: Cobol85Parser.DivideStatementContext):
    #     dividend = self.visit(ctx.getChildren(1))
    #     division_clause = self.visit(ctx.getChildren(2))
    #     remainder = self.visit(ctx.divideRemainder()) if ctx.divideRemainder() else None
    #     on_size_error_phrase = self.visit(ctx.onSizeErrorPhrase()) if ctx.onSizeErrorPhrase() else None
    #     not_on_size_error_phrase = self.visit(ctx.notOnSizeErrorPhrase()) if ctx.notOnSizeErrorPhrase() else None

    #     self.python_code += f"result = {dividend} / {division_clause}"
    #     if remainder:
    #         self.python_code += f"  # Remainder into {remainder}"
    #     self.python_code += "\n"

    #     return self.visitChildren(ctx)
    
    # def visitDivideGivingPhrase(self, ctx: Cobol85Parser.DivideGivingPhraseContext):
    #     giving_values = [self.visit(child) for child in ctx.divideGiving()]

    #     return ", ".join(giving_values)

    # def visitDivideInto(self, ctx: Cobol85Parser.DivideIntoContext):
    #     into_value = self.visit(ctx.getChild(0))
    #     rounded = "rounded" if ctx.ROUNDED() else ""

    #     return f"{into_value} {rounded}"

    # def visitDivideGiving(self, ctx: Cobol85Parser.DivideGivingContext):
    #     giving_value = self.visit(ctx.getChild(0))
    #     rounded = "rounded" if ctx.ROUNDED() else ""

    #     return f"{giving_value} {rounded}"

# ------------  Display  ------------------------------------------------

    def visitDisplayStatement(self, ctx: Cobol85Parser.DisplayStatementContext):
        display_operands = []

        for operand in ctx.displayOperand():
            operand_text = self.visit(operand)
            if operand_text:
                display_operands.append(operand_text)

        display_at = self.visit(ctx.displayAt()) if ctx.displayAt() else None
        display_upon = self.visit(ctx.displayUpon()) if ctx.displayUpon() else None
        display_with = ctx.displayWith() is not None

        if display_operands:
            if display_with:
                self.python_code += "print(" + ", ".join(f"{operand}" for operand in display_operands) + ", end='')\n"
            else:
                self.python_code += "print(" + ", ".join(f"{operand}" for operand in display_operands) + ")\n"

        if display_at:
            if display_with:
                self.python_code += f"print(' at {display_at}', end='')\n"
            else:
                self.python_code += f"print(' at {display_at}')\n"

        if display_upon:
            if display_with:
                self.python_code += f"print(' upon {display_upon}', end='')\n"
            else:
                self.python_code += f"print(' upon {display_upon}')\n"


        return self.visitChildren(ctx)
    def visitDisplayOperand(self, ctx: Cobol85Parser.DisplayOperandContext):
        return ctx.getText()    

    def visitDisplayAt(self, ctx: Cobol85Parser.DisplayAtContext):
        return ctx.getText()    

    def visitDisplayUpon(self, ctx: Cobol85Parser.DisplayUponContext):
        return ctx.getText()    

    def visitDisplayWith(self, ctx: Cobol85Parser.DisplayWithContext):
        return ctx.getText()    

# --------------------   DIVIDE   ---------------

    def visitDivideStatement(self, ctx: Cobol85Parser.DivideStatementContext):
        dividend = (ctx.children[1].getText())
        division_clause = (ctx.children[2].getText())

        remainder = self.visit(ctx.divideRemainder()) if ctx.divideRemainder() else None
        on_size_error_phrase = self.visit(ctx.onSizeErrorPhrase()) if ctx.onSizeErrorPhrase() else None
        not_on_size_error_phrase = self.visit(ctx.notOnSizeErrorPhrase()) if ctx.notOnSizeErrorPhrase() else None
        self.python_code += f"result = {dividend} / {division_clause}\n"
        if remainder:
            self.python_code += f"# Remainder into {remainder}\n"
        return self.visitChildren(ctx)
# --------------------   ADD   ---------------
    def visitAddToStatement(self, ctx:Cobol85Parser.AddToStatementContext):
        rhs,lhs='',''
        isrhs=True
        for child in ctx.children:
            if child.getText().upper()=='TO' and  isrhs:
                isrhs=False
                rhs = rhs[:-2]
            elif isrhs:
                rhs+=f'{child.getText()} + '
            elif not isrhs:
                lhs=child.getText()
                self.python_code += f'{lhs} += {rhs}\n'
        
        return self.visitChildren(ctx)


    def visitAddToGivingStatement(self, ctx:Cobol85Parser.AddToGivingStatementContext):
        rhs,lhs='',''
        isrhs=True
        for child in ctx.children:
            if child.getText().upper()=='GIVING' and  isrhs:
                isrhs=False
                rhs = rhs[:-2]
            elif isrhs and child.getText().upper()!='TO':
                rhs+=f'{child.getText()} + '
            elif not isrhs:
                lhs=child.getText()
                self.python_code += f'{lhs} = {rhs}\n'

        return self.visitChildren(ctx)
# --------------------   SUBTRACT   ---------------    
    def visitSubtractFromStatement(self, ctx:Cobol85Parser.SubtractFromStatementContext):
        rhs,lhs='',''
        isrhs=True
        for child in ctx.children:
            if child.getText().upper()=='FROM' and  isrhs:
                isrhs=False
                rhs = rhs[:-2]
            elif isrhs:
                rhs+=f'{child.getText()} + '
            elif not isrhs:
                lhs=child.getText()
                self.python_code += f'{lhs} -= {rhs}\n'
        
        return self.visitChildren(ctx)


    def visitSubtractFromGivingStatement(self, ctx:Cobol85Parser.SubtractFromGivingStatementContext):
        rhs,lhs='',''
        isrhs=True
        afterFrom=False
        for child in ctx.children:
            if child.getText().upper()=='GIVING' and  isrhs:
                isrhs=False
            elif isrhs and child.getText().upper()!='FROM' and (not afterFrom):
                rhs+=f'{child.getText()} + '
            elif isrhs and child.getText().upper()!='FROM' and afterFrom:
                rhs=f'{child.getText()} - {rhs}'
            elif isrhs and child.getText().upper()=='FROM':
                rhs = '('+rhs[:-3]+')'
                afterFrom=True
            elif not isrhs:
                lhs=child.getText()
                self.python_code += f'{lhs} = {rhs}\n'

        return self.visitChildren(ctx)