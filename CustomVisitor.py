from antlr.Cobol85Visitor import Cobol85Visitor
from antlr.Cobol85Parser import Cobol85Parser

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

# --------------------   MULTIPLY   --------------------

    # def visitMultiplyStatement(self, ctx:Cobol85Parser.MultiplyStatementContext):
    #     return self.visitChildren(ctx)


    def visitMultiplyRegular(self, ctx:Cobol85Parser.MultiplyRegularContext):
        multiplends = []
        for child in ctx.children:
            multiplends.append(child.getText())
        multiplier = ctx.parentCtx.children[1].getText()
        for chi in multiplends:
            self.python_code += f"{chi} = {chi} * {multiplier}\n"
        return self.visitChildren(ctx)


    def visitMultiplyRegularOperand(self, ctx:Cobol85Parser.MultiplyRegularOperandContext):
        return self.visitChildren(ctx)


    def visitMultiplyGiving(self, ctx:Cobol85Parser.MultiplyGivingContext):
        return self.visitChildren(ctx)


    def visitMultiplyGivingOperand(self, ctx:Cobol85Parser.MultiplyGivingOperandContext):
        return self.visitChildren(ctx)


    def visitMultiplyGivingResult(self, ctx:Cobol85Parser.MultiplyGivingResultContext):
        multiplend = ctx.parentCtx.parentCtx.children[1].getText()
        multiplier = ctx.parentCtx.children[0].getText()
        result = ctx.children[0].getText()
        self.python_code += f"{result} = {multiplend} * {multiplier}\n"
        return self.visitChildren(ctx)
    
# --------------------   DIVIDE   ---------------

    def visitDivideIntoStatement(self, ctx:Cobol85Parser.DivideIntoStatementContext):
        divisor = ctx.children[1].getText()
        dividend = ctx.parentCtx.children[1].getText()
        self.python_code += f"{divisor} = {divisor} // {dividend}\n"
        return self.visitChildren(ctx)

    def visitDivideIntoGivingStatement(self, ctx:Cobol85Parser.DivideIntoGivingStatementContext):
        divisor = ctx.parentCtx.children[1].getText()
        dividend = ctx.children[1].getText()
        quotient = ctx.children[2].children[1].getText()
        self.python_code += f"{quotient} = {dividend} // {divisor}\n"
        return self.visitChildren(ctx)

    def visitDivideByGivingStatement(self, ctx:Cobol85Parser.DivideByGivingStatementContext):
        quotient = ctx.children[2].children[1].getText()
        divisor = ctx.children[1].getText()
        dividend = ctx.parentCtx.children[1].getText()
        self.python_code += f"{quotient} = {dividend} // {divisor}\n"
        return self.visitChildren(ctx)

    def visitDivideRemainder(self, ctx:Cobol85Parser.DivideRemainderContext):
        dividend = ctx.parentCtx.children[1].getText()
        divisor = ctx.parentCtx.children[2].children[1].getText()
        remainder = ctx.children[1].getText()
        if ctx.parentCtx.children[2].children[0].getText().lower() == "by":
            self.python_code += f"{remainder} = {dividend} % {divisor}\n"
        else :
            self.python_code += f"{remainder} = {divisor} % {dividend}\n"
        return self.visitChildren(ctx)
    
#---------------------------- ACCEPT --------------------------------------

    def visitAcceptStatement(self, ctx:Cobol85Parser.AcceptStatementContext):
        var_accept = ctx.children[1].getText()
        self.python_code += f"{var_accept} = input()\n"
        return self.visitChildren(ctx)
