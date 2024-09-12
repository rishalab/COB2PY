from antlr.Cobol85Visitor import Cobol85Visitor
from antlr.Cobol85Parser import Cobol85Parser
from other.necessary_functions import *


class CustomVisitor(Cobol85Visitor):
    def __init__(self,parser,symbol_table,mapaddress):
        super().__init__()
        self.python_code = ""
        self.parser = parser
        self.symbol_table = symbol_table
        self.indentation = 0
        self.loop_indentation_level = 0
        self.mapaddress = mapaddress
        
    def get_python_code(self):
        return self.python_code
    def mapsearch(self,name):
        varName = name[0]
        if varName.isdigit():
            return varName
        print(name)
        name = name[::-1]
        name.pop(-1)
        for x in self.mapaddress:
            if varName == x[0].dataName:
                diff = len(x[0].parents) - len(name)
                found = True
                for y in x[0].parents:
                    print(y.dataName,"--")
                print(name,"!!")
                for i in range(0,len(name)):
                    print(x[0].parents[i+diff].dataName,name[i],"che",varName)
                    if x[0].parents[i+diff].dataName==name[i]:
                        found&=True
                    else:
                        found&=False
                if found:
                    return x[1]
        
        print(name, " Var Not Found")
    #overide
    def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
        
        return self.visitChildren(ctx)
    

# ------------  Display  ------------------------------------------------

    def visitDisplayStatement(self, ctx: Cobol85Parser.DisplayStatementContext):
        # Inden.increase_indentation(self)
        self.python_code += Inden.add_indentation(self)
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
        rhs,lhs=[],[]
        isrhs=True
        for child in ctx.children:
            print(lhs,rhs,"rfd ")
            if child.getText().upper()=='TO' and  isrhs:
                isrhs=False
            elif isrhs:
               if type(child)==Cobol85Parser.AddFromContext:
                if(len(self.mapsearch(self.extractMultipleDataNamesFrom(child)[0]))!=0):
                    print(self.getVariableLine(child.children[0]),'--------------------------------------------------------------------------------------',child.identifier().getText())
                    rhs.append(self.mapsearch(self.extractMultipleDataNamesFrom(child)[0]))
                if(len(self.extractMultipleDataNamesFrom(child)[1])!=0):
                    rhs.append(self.extractMultipleDataNamesFrom(child)[1])
            elif not isrhs:
                if type(child)==Cobol85Parser.AddToContext:
                    if(len(self.mapsearch(self.extractMultipleDataNames(child)))!=0):
                        print(self.extractMultipleDataNames(child),"beforee")
                        lhs.append(self.mapsearch(self.extractMultipleDataNames(child)))
            rhs1 = ''
        for x in rhs:
            if x.isdigit():
                rhs1+=(x+"+")
            else:
                rhs1+=(f'self.get{x}()+')
        for x in lhs :
            self.python_code +=f'\t\tself.set{x}({rhs1[:-1]})\n'     
            
        
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
                self.python_code+=Inden.add_indentation(self)
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
                self.python_code+=Inden.add_indentation(self)
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
                self.python_code+=Inden.add_indentation(self)
                self.python_code += f'{lhs} = {rhs}\n'

        return self.visitChildren(ctx)

# --------------------   MULTIPLY   --------------------

    # def visitMultiplyStatement(self, ctx:Cobol85Parser.MultiplyStatementContext):
    #     return self.visitChildren(ctx)


    def visitMultiplyRegular(self, ctx:Cobol85Parser.MultiplyRegularContext):
        multiplends = []
        for child in ctx.children:
            # print(child.getText(),"-------99999999999-------------")
            multiplends.append(self.mapsearch(self.getVariableLine(child.children[0])))
            print(multiplends," pppppppppppppppppppppppppppppppppppppppp")
        multiplier = self.mapsearch(self.getVariableLine(ctx.parentCtx.children[1]))
        for chi in multiplends:
            self.python_code+=Inden.add_indentation(self)
            if multiplier.isdigit():
                self.python_code += f"set{chi}(get{chi}() * {multiplier})\n"
            else:   
                self.python_code += f"set{chi}(get{chi}() * get{multiplier}())\n"
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
        self.python_code+=Inden.add_indentation(self)
        self.python_code += f"{result} = {multiplend} * {multiplier}\n"
        return self.visitChildren(ctx)
    
# --------------------   DIVIDE   ---------------

    def visitDivideIntoStatement(self, ctx:Cobol85Parser.DivideIntoStatementContext):
        divisor = ctx.children[1].getText()
        dividend = ctx.parentCtx.children[1].getText()
        self.python_code+=Inden.add_indentation(self)
        self.python_code += f"{divisor} = {divisor} // {dividend}\n"
        return self.visitChildren(ctx)

    def visitDivideIntoGivingStatement(self, ctx:Cobol85Parser.DivideIntoGivingStatementContext):
        divisor = ctx.parentCtx.children[1].getText()
        dividend = ctx.children[1].getText()
        quotient = ctx.children[2].children[1].getText()
        self.python_code+=Inden.add_indentation(self)
        self.python_code += f"{quotient} = {dividend} // {divisor}\n"
        return self.visitChildren(ctx)

    def visitDivideByGivingStatement(self, ctx:Cobol85Parser.DivideByGivingStatementContext):
        quotient = ctx.children[2].children[1].getText()
        divisor = ctx.children[1].getText()
        dividend = ctx.parentCtx.children[1].getText()
        self.python_code+=Inden.add_indentation(self)
        self.python_code += f"{quotient} = {dividend} // {divisor}\n"
        return self.visitChildren(ctx)

    def visitDivideRemainder(self, ctx:Cobol85Parser.DivideRemainderContext):
        dividend = ctx.parentCtx.children[1].getText()
        divisor = ctx.parentCtx.children[2].children[1].getText()
        remainder = ctx.children[1].getText()
        if ctx.parentCtx.children[2].children[0].getText().lower() == "by":
            self.python_code+=Inden.add_indentation(self)
            self.python_code += f"{remainder} = {dividend} % {divisor}\n"
        else :
            self.python_code+=Inden.add_indentation(self)
            self.python_code += f"{remainder} = {divisor} % {dividend}\n"
        return self.visitChildren(ctx)
    
#----------------------------  ACCEPT  ------------------------------------

    def visitAcceptStatement(self, ctx:Cobol85Parser.AcceptStatementContext):
        var_accept = ctx.children[1].getText()
        self.python_code+=Inden.add_indentation(self)
        self.python_code += f"{var_accept} = input()\n"
        return self.visitChildren(ctx)

#-----------------------------  IF  ---------------------------------------

    def visitIfStatement(self, ctx:Cobol85Parser.IfStatementContext):
        self.python_code += Inden.add_indentation(self);
        if_condition = ctx.children[1].getText();
        self.python_code += f"if {if_condition} :\n"
        Inden.increase_indentation(self);
        result = self.visitChildren(ctx)
        Inden.decrease_indentation(self)
        return result

    def visitIfElse(self, ctx:Cobol85Parser.IfElseContext):
        self.python_code += Inden.add_indentation(self);
        Inden.decrease_indentation(self);
        self.python_code += f"else:\n"
        Inden.increase_indentation(self);
        print(ctx.getText())
        return self.visitChildren(ctx)
    
#----------------------------- STOP & Paragraphs ---------------------------------------

    def visitStopStatement(self, ctx:Cobol85Parser.StopStatementContext):
        Inden.decrease_indentation(self)
        return self.visitChildren(ctx)
    def visitParagraphs(self, ctx:Cobol85Parser.ParagraphsContext):
        Inden.increase_indentation(self)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#paragraph.
    def visitParagraph(self, ctx:Cobol85Parser.ParagraphContext):
        name = replacehypwund(ctx.children[0].getText())
        self.python_code += Inden.add_indentation(self)
        self.python_code += f"def {name}():\n"
        Inden.increase_indentation(self)
        result = self.visitChildren(ctx)
        Inden.decrease_indentation(self)
        return result
#----------------------------- PERFORM ------------------------------------

    def visitPerformStatement(self, ctx:Cobol85Parser.PerformStatementContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performInlineStatement.
    def visitPerformInlineStatement(self, ctx:Cobol85Parser.PerformInlineStatementContext):
        # self.python_code += Inden.add_indentation(self)
        # self.python_code+=f"for _ in range(1) :\n"
        # Inden.increase_indentation(self)
        result = self.visitChildren(ctx)
        if(Inden.get_loop_inden(self) == 2):
            Inden.decrease_indentation(self)
            Inden.loop_inden_decrement(self)
            Inden.loop_inden_decrement(self)
            
        Inden.decrease_indentation(self)
        return result


    # Visit a parse tree produced by Cobol85Parser#performProcedureStatement.
    def visitPerformProcedureStatement(self, ctx:Cobol85Parser.PerformProcedureStatementContext):
        i = 0
        # print(ctx.getChildCount())
        # print(ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText())
        while ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText() != ctx.children[0].getText() :
            i+=1
            # print(ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText()+"\n")
            # print(ctx.children[0].getText()+"\n")
        self.python_code += Inden.add_indentation(self)
        self.python_code+=f"{replacehypwund(ctx.children[0].getText())}()\n"
        if ctx.getChildCount()!=1:
            while ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText() != ctx.children[2].getText():
                i+=1
                self.python_code += Inden.add_indentation(self)
                tempstr = replacehypwund(ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText())
                # print(tempstr+"  ==\n")
                self.python_code+=f"{tempstr}()\n"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performType.
    def visitPerformType(self, ctx:Cobol85Parser.PerformTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performTimes.
    def visitPerformTimes(self, ctx:Cobol85Parser.PerformTimesContext):
        self.python_code += Inden.add_indentation(self)
        self.python_code += f"for _ in range({ctx.children[0].getText()}):\n"
        Inden.increase_indentation(self)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performUntil.
    def visitPerformUntil(self, ctx:Cobol85Parser.PerformUntilContext):
        if ctx.parentCtx.parentCtx.children[0].getText() != "VARYING" and ctx.parentCtx.parentCtx.children[0].getText() != "AFTER" :
            self.python_code += Inden.add_indentation(self)
            if ctx.children[0].getText() == "UNTIL":
                self.python_code += f"while not ( {ctx.children[1].getText()}):\n"
            else:
                self.python_code += f"while not ( {ctx.children[2].getText()}):\n"
            Inden.increase_indentation(self)
        else :
            var = ctx.parentCtx.children[0].getText()
            start = ctx.parentCtx.children[1].children[1].getText()
            condition = ctx.parentCtx.children[3].children[1].getText()
            self.python_code += Inden.add_indentation(self)
            self.python_code += f"{var} = {start}\n"
            self.python_code += Inden.add_indentation(self)
            self.python_code += f"while {condition} :\n"
            Inden.increase_indentation(self)
            Inden.loop_inden_increment(self)
            
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performVarying.
    def visitPerformVarying(self, ctx:Cobol85Parser.PerformVaryingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performVaryingClause.
    def visitPerformVaryingClause(self, ctx:Cobol85Parser.PerformVaryingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performVaryingPhrase.
    def visitPerformVaryingPhrase(self, ctx:Cobol85Parser.PerformVaryingPhraseContext):
        # print(ctx.getToken)
        # var = ctx.children[0].getText()
        # start = ctx.children[1].children[1].getText()
        # condition = ctx.children[3].children[1].getText()
        # self.python_code += Inden.add_indentation(self)
        # self.python_code += f"{var} = {start}\n"
        # self.python_code += Inden.add_indentation(self)
        # self.python_code += f"while {condition} :\n"
        # Inden.increase_indentation(self)
        # result = ctx
        # self.python_code += Inden.add_indentation(self)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performAfter.
    def visitPerformAfter(self, ctx:Cobol85Parser.PerformAfterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performFrom.
    def visitPerformFrom(self, ctx:Cobol85Parser.PerformFromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performBy.
    def visitPerformBy(self, ctx:Cobol85Parser.PerformByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cobol85Parser#performTestClause.
    def visitPerformTestClause(self, ctx:Cobol85Parser.PerformTestClauseContext):
        return self.visitChildren(ctx)
    
    #----------Helpers-----------------------------------#
    def extractMultipleDataNamesFrom(self, ctx: Cobol85Parser.AddFromContext):
        data_names,literals = [],[]
        if ctx.identifier():
            identifier = ctx.identifier()
            literal= ctx.literal()
            if literal:
                literals.append(literal.getText())

            if identifier.qualifiedDataName():
                qualified_data_name = identifier.qualifiedDataName()

                if qualified_data_name.qualifiedDataNameFormat1():
                    format1 = qualified_data_name.qualifiedDataNameFormat1()

                    if format1.dataName():
                        data_names.append(format1.dataName().getText().replace('-','_'))

                    if format1.qualifiedInData():
                        for qualifiedInData in format1.qualifiedInData():
                            if qualifiedInData.inData():
                                if qualifiedInData.inData().dataName():
                                    data_names.append(qualifiedInData.inData().dataName().getText().replace('-','_'))
        print(data_names)
        
        return data_names,literals
    
    def extractMultipleDataNames(self, ctx: Cobol85Parser.AddToContext):
        data_names = []
        if ctx.identifier():
            identifier = ctx.identifier()
            
            if identifier.qualifiedDataName():
                qualified_data_name = identifier.qualifiedDataName()

                if qualified_data_name.qualifiedDataNameFormat1():
                    format1 = qualified_data_name.qualifiedDataNameFormat1()

                    if format1.dataName():
                        data_names.append(format1.dataName().getText().replace('-','_'))

                    if format1.qualifiedInData():
                        for qualifiedInData in format1.qualifiedInData():
                            if qualifiedInData.inData():
                                if qualifiedInData.inData().dataName():
                                    data_names.append(qualifiedInData.inData().dataName().getText().replace('-','_'))
        print(data_names,"!!!!!!!!!!!!!")
        
        return data_names
    def getVariableLine(self,ctx:Cobol85Parser.identifier):
        names = []
        node = ctx.children[0].children[0]
        start = True
        for child in node.children:
            if start:
                names.append(child.getText().replace('-', '_'))
                start = False
            else:
                names.append(child.children[0].children[1].getText().replace('-', '_'))
        print (names," --000000000000000000000000-------------------")
        return names
    