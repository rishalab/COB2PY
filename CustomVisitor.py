from antlr.Cobol85Visitor import Cobol85Visitor
from antlr.Cobol85Parser import Cobol85Parser
from other.necessary_functions import *


class CustomVisitor(Cobol85Visitor):
	def __init__(self,parser,symbol_table,mapaddress):
		super().__init__()
		self.python_code = ""
		self.parser = parser
		self.symbol_table = symbol_table
		self.indentation = 1
		self.loop_indentation_level = 0
		self.mapaddress = mapaddress
		self.isEvaluateStarted = False
		
	def get_python_code(self):
		return self.python_code
	def is_digdec(self,s):
		try:
			float(s)
			return True
		except ValueError:
			return False
	def mapsearch(self,name):
		# if not name:
		#     return 'NOT founfed'
		varName = name[0]
		if self.is_digdec(varName):
			return varName
		# print(name)
		name = name[::-1]
		name.pop(-1)
		for x in self.mapaddress:
			if varName == x[0].dataName:
				diff = len(x[0].parents) - len(name)
				found = True
				for y in x[0].parents:
					print(y.dataName,"--")
				# print(name,"!!")
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
			# print(type(operand.children[0]),"-----------------")
			if type(operand.children[0])==Cobol85Parser.IdentifierContext:
				operand_text=self.getStringGen(operand.children[0])
			else:
				operand_text = self.visit(operand)
			if operand_text:
				display_operands.append(operand_text)
		# print(display_operands,"-----------------")
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
			if child.getChildCount()==1:
				self.python_code+=Inden.add_indentation(self)
				tempstr = child.parentCtx.parentCtx.children[1].getText()
			# print(tempstr,"-------99999999999-------------")
				if self.is_digdec(tempstr):
					self.python_code += f"self.set{child.children[0].getText()}(self.get{child.children[0].getText()}() * {child.parentCtx.parentCtx.children[1].getText()})\n"
				else :
					self.python_code += self.setStringGen(child.children[0])+self.getStringGen(child.children[0])+" * "+self.getStringGen(child.parentCtx.parentCtx.children[1])+")\n"
			else:
				self.python_code+=Inden.add_indentation(self)
				tempstr = child.parentCtx.parentCtx.children[1].getText()
			# print(tempstr,"-------99999999999-------------")
				if self.is_digdec(tempstr):
					self.python_code += f"self.set{child.children[0].getText()}(self.get{child.children[0].getText()}() * {child.parentCtx.parentCtx.children[1].getText()}, True)\n"
				else :
					self.python_code += self.setStringGen(child.children[0])+self.getStringGen(child.children[0])+" * "+self.getStringGen(child.parentCtx.parentCtx.children[1])+", True)\n"
 
			# print(child.parentCtx.getText(),"-------99999999999-------------")
		# for child in ctx.children:
		#     # print(child.getText(),"-------99999999999-------------")
		#     multiplends.append(self.mapsearch(self.getVariableLine(child.children[0])))
		#     # print(multiplends," pppppppppppppppppppppppppppppppppppppppp")
		# multiplier = self.mapsearch(self.getVariableLine(ctx.parentCtx.children[1]))
		# for chi in multiplends:
		#     self.python_code+=Inden.add_indentation(self)
		#     # self.python_code += self.setStringGen()
		#     if multiplier.isdigit():
		#         self.python_code += f"set{chi}(get{chi}() * {multiplier})\n"
		#     else:   
		#         self.python_code += f"set{chi}(get{chi}() * get{multiplier}())\n"
		return self.visitChildren(ctx)


	def visitMultiplyRegularOperand(self, ctx:Cobol85Parser.MultiplyRegularOperandContext):
		return self.visitChildren(ctx)


	def visitMultiplyGiving(self, ctx:Cobol85Parser.MultiplyGivingContext):
		return self.visitChildren(ctx)


	def visitMultiplyGivingOperand(self, ctx:Cobol85Parser.MultiplyGivingOperandContext):
		return self.visitChildren(ctx)


	def visitMultiplyGivingResult(self, ctx:Cobol85Parser.MultiplyGivingResultContext):
		# multiplend = ctx.parentCtx.parentCtx.children[1].getText()
		# multiplier = ctx.parentCtx.children[0].getText()
		# result = ctx.children[0].getText()
		# self.python_code+=Inden.add_indentation(self)
		# self.python_code += f"{result} = {multiplend} * {multiplier}\n"
		
		if self.is_digdec(ctx.parentCtx.parentCtx.children[1].getText()):
			multiplend = ctx.parentCtx.parentCtx.children[1].getText()
		else :
			multiplend = self.getStringGen(ctx.parentCtx.parentCtx.children[1])
		if self.is_digdec(ctx.parentCtx.children[0].getText()):
			multiplier = ctx.parentCtx.children[0].getText()
		else :
			multiplier = self.getStringGen(ctx.parentCtx.children[0].children[0])
		if ctx.getChildCount()==2:
			self.python_code+=Inden.add_indentation(self)
			self.python_code += self.setStringGen(ctx.children[0])+multiplend+" * "+multiplier+", True)\n"
		else:
			self.python_code+=Inden.add_indentation(self)
			self.python_code += self.setStringGen(ctx.children[0])+multiplend+" * "+multiplier+")\n"
		return self.visitChildren(ctx)
	
# --------------------   DIVIDE   ---------------

	# def visitDivideIntoStatement(self, ctx:Cobol85Parser.DivideIntoStatementContext):
	#     divisor = ctx.children[1].getText()
	#     dividend = ctx.parentCtx.children[1].getText()
	#     self.python_code+=Inden.add_indentation(self)
	#     self.python_code += f"{divisor} = {divisor} // {dividend}\n"
	#     return self.visitChildren(ctx)

	# def visitDivideIntoGivingStatement(self, ctx:Cobol85Parser.DivideIntoGivingStatementContext):
	#     if ctx.children[1].qualifiedDataName():
	#         print("muy iusuiefhbiodsiugiougnfs")
	#     else:
	#         print("uygduysiugyusiuyg udgyudiughui fdiug") 
	#     print((type(ctx.children[1])==Cobol85Parser.IdentifierContext),"000000000000000-------------------00000000")
	#     divisor = ctx.parentCtx.children[1].getText()
	#     dividend = ctx.children[1].getText()
	#     quotient = ctx.children[2].children[1].getText()
	#     self.python_code+=Inden.add_indentation(self)
	#     self.python_code += f"{quotient} = {dividend} // {divisor}\n"
	#     return self.visitChildren(ctx)

	# def visitDivideByGivingStatement(self, ctx:Cobol85Parser.DivideByGivingStatementContext):
	#     quotient = ctx.children[2].children[1].getText()
	#     divisor = ctx.children[1].getText()
	#     dividend = ctx.parentCtx.children[1].getText()
	#     self.python_code+=Inden.add_indentation(self)
	#     self.python_code += f"{quotient} = {dividend} // {divisor}\n"
	#     return self.visitChildren(ctx)

	# def visitDivideRemainder(self, ctx:Cobol85Parser.DivideRemainderContext):
	#     dividend = ctx.parentCtx.children[1].getText()
	#     divisor = ctx.parentCtx.children[2].children[1].getText()
	#     remainder = ctx.children[1].getText()
	#     if ctx.parentCtx.children[2].children[0].getText().lower() == "by":
	#         self.python_code+=Inden.add_indentation(self)
	#         self.python_code += f"{remainder} = {dividend} % {divisor}\n"
	#     else :
	#         self.python_code+=Inden.add_indentation(self)
	#         self.python_code += f"{remainder} = {divisor} % {dividend}\n"
	#     return self.visitChildren(ctx)
	def visitDivideInto(self, ctx:Cobol85Parser.DivideIntoContext):
		dividend = ctx.children[0]
		divisor = ctx.parentCtx.parentCtx.children[1]
		self.python_code+=Inden.add_indentation(self)
		if ctx.getChildCount()==2:
			self.python_code += self.setStringGen(dividend)+self.getStringGen(dividend)+" / "+self.getStringGen(divisor)+", True)\n"
		else:
			self.python_code += self.setStringGen(dividend)+self.getStringGen(dividend)+" / "+self.getStringGen(divisor)+")\n"
		return self.visitChildren(ctx)

	def visitDivideGiving(self, ctx:Cobol85Parser.DivideGivingContext):
		quotient = ctx.children[0]
		dividend = ctx.parentCtx.parentCtx.children[1]
		divisor = ctx.parentCtx.parentCtx.parentCtx.children[1]
		if ctx.parentCtx.parentCtx.children[0].getText().lower() == "by":
			self.python_code+=Inden.add_indentation(self)
			if ctx.getChildCount()==2:
				self.python_code += self.setStringGen(quotient)+self.getStringGen(divisor)+" / "+self.getStringGen(dividend)+", True)\n"
			else:
				self.python_code += self.setStringGen(quotient)+self.getStringGen(divisor)+" / "+self.getStringGen(dividend)+")\n"
		else :
			self.python_code+=Inden.add_indentation(self)
			if ctx.getChildCount()==2:
				self.python_code += self.setStringGen(quotient)+self.getStringGen(dividend)+" / "+self.getStringGen(divisor)+", True)\n"
			else:
				self.python_code += self.setStringGen(quotient)+self.getStringGen(dividend)+" / "+self.getStringGen(divisor)+")\n"
		return self.visitChildren(ctx)

	def visitDivideRemainder(self, ctx:Cobol85Parser.DivideRemainderContext):
		divisor = ctx.parentCtx.children[1]
		dividend = ctx.parentCtx.children[2].children[1]
		self.python_code+=Inden.add_indentation(self)
		if ctx.parentCtx.children[2].children[0].getText().lower() == "by":
			self.python_code += self.setStringGen(ctx.children[1])+self.getStringGen(divisor)+" % "+self.getStringGen(dividend)+")\n"
		else :
			self.python_code += self.setStringGen(ctx.children[1])+self.getStringGen(dividend)+" % "+self.getStringGen(divisor)+")\n"
		return self.visitChildren(ctx)

	
#----------------------------  ACCEPT  ------------------------------------

	def visitAcceptStatement(self, ctx:Cobol85Parser.AcceptStatementContext):
		var_accept = ctx.children[1].getText()
		self.python_code+=Inden.add_indentation(self)
		self.python_code += f"{var_accept} = input()\n"
		return self.visitChildren(ctx)

#-----------------------------  IF  ---------------------------------------

	def visitIfStatement(self, ctx:Cobol85Parser.IfStatementContext):
		# print("hi",self.arithmeticExpressionget(ctx.children[1].children[0].children[0].children[0].children[0].children[0]))
		self.python_code += Inden.add_indentation(self);
		if_condition = self.conditionget(ctx.children[1])
		self.python_code += f"if {if_condition} :\n"
		Inden.increase_indentation(self);
		result = self.visitChildren(ctx)
		Inden.decrease_indentation(self)
		return result

	def visitIfElse(self, ctx:Cobol85Parser.IfElseContext):
		Inden.decrease_indentation(self);
		self.python_code += Inden.add_indentation(self);
		self.python_code += f"else:\n"
		Inden.increase_indentation(self);
		# print(ctx.getText())
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
		self.python_code += f"def {name}(self):\n"
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
		self.python_code+=f"self.{replacehypwund(ctx.children[0].getText())}()\n"
		if ctx.getChildCount()!=1:
			while ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText() != ctx.children[2].getText():
				i+=1
				self.python_code += Inden.add_indentation(self)
				tempstr = replacehypwund(ctx.parentCtx.parentCtx.parentCtx.parentCtx.children[i].children[0].getText())
				# print(tempstr+"  ==\n")
				self.python_code+=f"self.{tempstr}()\n"
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
	#----------COMPUTE-----------------------------------#
	
	def visitComputeStatement(self, ctx: Cobol85Parser.ComputeStatementContext):
		i = 1
		# print(ctx.getChildCount(), " ================== ")
		# for child in ctx.children:
		#     print(child.getText(), " ================== ")
			
		for child in ctx.children:
			if child.getText().upper() == "EQUAL" or child.getText().upper() == "=":
				break
			i+=1
		print(i,"====================")
		for j in range(1,i):
			if type(ctx.children[j])==Cobol85Parser.ComputeStoreContext:
				self.python_code += Inden.add_indentation(self)
				if ctx.children[j].getChildCount()==1:
					self.python_code += f"{self.setStringGen(ctx.children[j].children[0])} {self.arithmeticExpressionget(ctx.children[i])})\n"
				elif ctx.children[j].getChildCount()==2:
					self.python_code += f"{self.setStringGen(ctx.children[j].children[0])} {self.arithmeticExpressionget(ctx.children[i])}, True)\n"
		return self.visitChildren(ctx)

# ----------------------- EVALUATE -------------------------
	def visitEvaluateStatement(self, ctx: Cobol85Parser.EvaluateStatementContext):
		r = self.visitChildren(ctx)
		self.isEvaluateStarted = False
		return r
	def visitEvaluateWhenOther(self, ctx: Cobol85Parser.EvaluateWhenOtherContext):
		self.python_code += Inden.add_indentation(self)
		self.python_code += "else:\n"
		Inden.increase_indentation(self)
		r = self.visitChildren(ctx)
		Inden.decrease_indentation(self)
		return r
	def visitEvaluateWhenPhrase(self, ctx: Cobol85Parser.EvaluateWhenPhraseContext):
		select = ctx.parentCtx
		n = 0
		arr1 = []
		for child in select.children[1:]:
			if type(child)==Cobol85Parser.EvaluateSelectContext:
				arr1.append(self.evaluateselectget(child))
				n+=1
			elif type(child)==Cobol85Parser.EvaluateAlsoSelectContext:
				arr1.append(self.evaluateselectget(child.children[1]))
				n+=1
		# print(n, "{{{{{{{{{{{[[[[]]]]}}}}}}}}}}}")
		# print (arr1)
		str = ""
		for child in ctx.children:
			# str = ""
			if type(child) == Cobol85Parser.EvaluateWhenContext:
				if str != "":
					str += " or "
				str += self.evaluatewhenget(child, arr1)
				print(str, " ############### ")
		if self.isEvaluateStarted:
			self.python_code += Inden.add_indentation(self)
			self.python_code += f"elif {str}:\n"
			Inden.increase_indentation(self)
		else:
			self.python_code += Inden.add_indentation(self)
			self.python_code += f"if {str}:\n"
			Inden.increase_indentation(self)
			self.isEvaluateStarted = True
		ans = self.visitChildren(ctx)
		Inden.decrease_indentation(self)
		return ans
	def evaluatewhenget(self,ctx:Cobol85Parser.EvaluateWhenContext, lhs):
		rhs = []
		str = ""
		n= len(lhs)
		i = 0
		# print(ctx.getText()," 888888888888888888888********8 ")
		for child in ctx.children[1:]:
			# print(str," 9999999999999999********8 ")
			# print(child.getText()," 888888888888888888888********8 ")
			# print(child.children[1].getText()," 888888888888888888888********8 ")
			print(lhs[i], "  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
			if type(child)==Cobol85Parser.EvaluateConditionContext:
				print(str," 9999999999999999********8 ")
				print(type(child.children[0])," 888888888888888888888********8 ")
				print(child.children[0].getChildCount()," 888888888888888888888********8 ")
				str += self.evaluateconditionget(child, lhs[i])
			elif type(child)==Cobol85Parser.EvaluateAlsoConditionContext:
				str += " and "
				print(str," 9999999999999999********8 ")
				print(child.children[1].getText()," 888888888888888888888********8 ")
				str += self.evaluateconditionget(child.children[1], lhs[i])
			i+=1
			print(str," ||||||||||||||||||||||||| ")
		return '(' +  str + ')'
	def evaluateconditionget(self,ctx:Cobol85Parser.EvaluateConditionContext, txt):
		# print(ctx.getText()," 888888888888888888888********8 ")
		if type(ctx.children[0])==Cobol85Parser.ConditionContext:
			return txt+' == '+self.conditionget(ctx.children[0])
		elif type(ctx.children[0])==Cobol85Parser.BooleanLiteralContext:
			return txt + " == " + ctx.children[0].getText()
		elif ctx.getText().upper() == "ANY":
			return "True"
		else:
			if ctx.children[0].getText().upper() == "NOT":
				if ctx.getChildCount()==2:
					return txt + " != " + self.evaluatevalueget(ctx.children[1])
					# return self.evaluatevalueget(ctx.children[1]) + " <= " + txt + " <= " + self.evaluatevalueget(ctx.children[2].children[1])
				elif ctx.getChildCount()==3:
					return '( '+ txt + ' < ' + self.evaluatevalueget(ctx.children[1]) + ' or ' + txt + ' > ' + self.evaluatevalueget(ctx.children[2].children[1]) + ' )'
			else:
				if ctx.getChildCount()==2:
					return self.evaluatevalueget(ctx.children[0]) + " <= " + txt + " <= " + self.evaluatevalueget(ctx.children[1].children[1])
				elif ctx.getChildCount()==1:
					return txt + " == " + self.evaluatevalueget(ctx.children[0])
	def evaluatevalueget(self,ctx:Cobol85Parser.EvaluateValueContext):
		if type(ctx.children[0])==Cobol85Parser.ArithmeticExpressionContext:
			return self.arithmeticExpressionget(ctx.children[0])
		elif type(ctx.children[0])==Cobol85Parser.LiteralContext:
			return ctx.children[0].getText()
		else:
			return ctx.children[0].getText()
	def evaluateselectget(self,ctx:Cobol85Parser.EvaluateSelectContext):
		# print(ctx.children[0].getText()," 888888888888888888888********8 ")
		if type(ctx.children[0])==Cobol85Parser.IdentifierContext :
			x = self.getStringGen(ctx.children[0])
			return x
		elif type(ctx.children[0])==Cobol85Parser.ArithmeticExpressionContext:
			return self.arithmeticExpressionget(ctx.children[0])
		elif type(ctx.children[0])==Cobol85Parser.LiteralContext:
			return ctx.children[0].getText()
		else:
			return self.conditionget(ctx.children[0])
# -----------------  EVALUATE  ------------------------------
	# def visitEvaluateStatement(self, ctx: Cobol85Parser.EvaluateStatementContext):
	# 	r = self.visitChildren(ctx)
	# 	# Inden.decrease_indentation(self)
	# 	return r
	# def evaluatesetget(self,ctx:Cobol85Parser.EvaluateStatementContext):
	# 	a = []
	# 	for child in ctx.children:
	# 		if type(child)==Cobol85Parser.EvaluateSelectContext:
	# 			a.append(self.evaluateselectget(child))
	# 		elif type(child)==Cobol85Parser.EvaluateAlsoSelectContext:
	# 			a.append(self.evaluateselectget(child.children[1]))
	# 	print(a,"-----------------")
	# 	return a

	# def evaluateselectget(self,ctx:Cobol85Parser.EvaluateSelectContext):
	# 	print(ctx.children[0].getText()," 888888888888888888888********8 ")
	# 	if type(ctx.children[0])==Cobol85Parser.IdentifierContext or type(ctx.children[0])==Cobol85Parser.LiteralContext:
	# 		x = self.getStringGen(ctx.children[0])
	# 		pair = (1,x)
	# 		return pair
	# 	elif type(ctx.children[0])==Cobol85Parser.ArithmeticExpressionContext:
	# 		return (1,self.arithmeticExpressionget(ctx.children[0]))
	# 	elif type(ctx.children[0])==Cobol85Parser.LiteralContext:
	# 		return (1,ctx.children[0].getText())
	# 	else:
	# 		return (2,self.conditionget(ctx.children[0]))
	# def visitEvaluateStatement(self,ctx:Cobol85Parser.EvaluateStatementContext):
	# 	a = self.evaluateselectget(ctx)
	# 	print(len(a),"}}}}}}}")
	# 	return self.visitChildren(ctx)

	# def visitEvaluateWhenPhrase(self, ctx: Cobol85Parser.EvaluateWhenPhraseContext):
	# 	self.python_code += Inden.add_indentation(self)
	# 	self.python_code += "if "
	# 	a = self.evaluatesetget(ctx.parentCtx)
	# 	# print(a," 999999 ")
	# 	# print(len(a)," 999999 ")
	# 	b = []

	# 	print(ctx.children[0].getText()," 999999 ")
	# 	print(ctx.children[0].children[0].getText()," ----------------- ")
	# 	# for child in ctx.children[0].children:
	# 	# 	print(child.getText()," iiiiiiiiiiiiiiii ")
	# 	# 	if child.getText().upper() == 'WHEN':
	# 	# 		continue
	# 	# 	if type(child)==Cobol85Parser.EvaluateConditionContext:
	# 	# 		ki = child.getChildCount()
	# 	# 		if ki==1:
	# 	# 			if type(child.children[0]) == Cobol85Parser.ConditionContext:
	# 	# 				b.append(self.conditionget(child.children[0]))
	# 	# 			elif type(child.children[0])==Cobol85Parser.BooleanLiteralContext:
	# 	# 				b.append(child.children[0].getText())

	# 	# 		b.append(self.conditionget(child.children[0]))
	# 	# 	elif type(child)==Cobol85Parser.EvaluateAlsoConditionContext:
	# 	# 		b.append("True")
	# 	# for i in range(0,len(a)):
	# 	# 	if a[i][0]==1:
	# 	# 		self.python_code += f"{a[i][1]} == "
	# 	# 	else:
	# 	# 		self.python_code += f"{a[i][1]} "
	# 	# 	if i!=len(a)-1:
	# 	# 		self.python_code += "or "
	# 	r = self.visitChildren(ctx)
	# 	Inden.decrease_indentation(self)
	# 	return r
	# def visitEvaluateWhenOther(self, ctx: Cobol85Parser.EvaluateWhenOtherContext):
	# 	self.python_code += Inden.add_indentation(self)
	# 	self.python_code += "else:\n"
	# 	Inden.increase_indentation(self)
	# 	r = self.visitChildren(ctx)
	# 	Inden.decrease_indentation(self)
	# 	return r
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
		# print(data_names,"!!!!!!!!!!!!!")
		
		return data_names
	def getVariableLine(self,ctx:Cobol85Parser.identifier):
		names = []
		occurs_nums = []
		# print(ctx.getText(),"******************************8")
		# print(type(ctx.children[0]),"-------------------")
		if type(ctx.children[0])==Cobol85Parser.TableCallContext:
			for child in ctx.children[0].children:
				# print(type(child), "[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]====================")
				if type(child)==Cobol85Parser.QualifiedDataNameContext:
					names.append(child.getText().replace('-', '_'))
				elif child.getText()!="(" and child.getText()!=")":
					if child.getText().isdigit():
						occurs_nums.append(child.getText())
					else :
						arr,new = self.getVariableLine(child)
						# print(arr,"-----------ppppppppppp--------")
						occurs_nums.append(self.getStringGen(child))
						# occurs_nums.append("get"+self.mapsearch(arr)+"()")

		elif type(ctx.children[0])==Cobol85Parser.QualifiedDataNameContext:
			node = ctx.children[0].children[0]
			start = True
			for child in node.children:
				if start:
					names.append(child.getText().replace('-', '_'))
					start = False
				else:
					names.append(child.children[0].children[1].getText().replace('-', '_'))
		# print(occurs_nums,"============iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii=======")
		# print (names," --000000000000000000000000-------------------\n")
		output_string = ','.join(occurs_nums)
		return names,output_string

	def setStringGen(self,ctx:Cobol85Parser.identifier):
		names,occurs_nums = self.getVariableLine(ctx)
		stringout = ''
		if occurs_nums == '':
			stringout += 'self.set' + self.mapsearch(names) + '('
		else:
			stringout += 'self.set' + self.mapsearch(names) + '(' + occurs_nums + ','
		return stringout
	
	def getStringGen(self,ctx:Cobol85Parser.identifier):
		if(self.is_digdec(ctx.getText())):
			return ctx.getText()
		names,occurs_nums = self.getVariableLine(ctx)
		stringout = ''
		# print(names," 9999999999999999999 ")
		stringout += 'self.get' + self.mapsearch(names) + '(' + occurs_nums + ')'
		return stringout
	
	def conditionget(self,ctx:Cobol85Parser.condition):
		if ctx.getChildCount()==1:
			return self.combinableConditionget(ctx.children[0])
		else:
			number = ctx.getChildCount()
			temp1 = 1
			stringout = self.combinableConditionget(ctx.children[0])
			while temp1 != number:
				if ctx.children[temp1].children[0].getText().upper() == "AND":
					if type(ctx.children[temp1].children[1])==Cobol85Parser.ConditionContext:
						stringout += " and " + self.combinableConditionget(ctx.children[temp1].children[1])
				else:
					if type(ctx.children[temp1].children[1])==Cobol85Parser.ConditionContext:
						stringout += " or " + self.combinableConditionget(ctx.children[temp1].children[1])
				temp1 += 1
			return stringout
	def combinableConditionget(self,ctx:Cobol85Parser.combinableCondition):
		if ctx.children[0].getText().upper() == "NOT":
			return "not " + self.simpleConditionget(ctx.children[1])
		else :
			return self.simpleConditionget(ctx.children[0])
	def simpleConditionget(self,ctx:Cobol85Parser.simpleCondition):
		if type(ctx.children[0])==Cobol85Parser.RelationConditionContext:
			return self.relationConditionget(ctx.children[0])
		elif type(ctx.children[0])==Cobol85Parser.ClassConditionContext:
			return self.classConditionget(ctx.children[0])
		# elif type(ctx.children[0])==Cobol85Parser.ConditionNameReferenceContext:
		#     return conditionNameConditionget(ctx.children[0])
		else :
			return '(' + self.conditionget(ctx.children[1]) + ')'
	def classConditionget(self,ctx:Cobol85Parser.classCondition):
		value = self.getStringGen(ctx.children[0])
		count = ctx.getChildCount()
		if count == 3:
			if ctx.children[2].getText().upper() == "NUMERIC":
				return value + ".isnumeric()"
			elif ctx.children[2].getText().upper() == "ALPHABETIC":
				return value + ".isalpha()"
			elif ctx.children[2].getText().upper() == "ALPHANUMERIC":
				return value + ".isalnum()"
			elif ctx.children[2].getText().upper() == "DBCS":
				return value + ".isprintable()"
			elif ctx.children[2].getText().upper() == "KANJI":
				return value + ".isprintable()"
		if count == 4:
			if ctx.children[2].getText().upper() == "NOT":
				if ctx.children[3].getText().upper() == "NUMERIC":
					return "not " + value + ".isnumeric()"
				elif ctx.children[3].getText().upper() == "ALPHABETIC":
					return "not " + value + ".isalpha()"
				elif ctx.children[3].getText().upper() == "ALPHANUMERIC":
					return "not " + value + ".isalnum()"
				elif ctx.children[3].getText().upper() == "DBCS":
					return "not " + value + ".isprintable()"
				elif ctx.children[3].getText().upper() == "KANJI":
					return "not " + value + ".isprintable()"
		print("Error in classCondition")
	def relationConditionget(self,ctx:Cobol85Parser.relationCondition):
		if type(ctx.children[0])==Cobol85Parser.RelationSignConditionContext:
			return self.relationSignConditionget(ctx.children[0])
		elif type(ctx.children[0])==Cobol85Parser.RelationArithmeticComparisonContext:
			return self.relationArithmeticComparisonget(ctx.children[0])
		elif type(ctx.children[0])==Cobol85Parser.RelationCombinedComparisonContext:
			return self.relationCombinedComparisonget(ctx.children[0])
	def relationSignConditionget(self,ctx:Cobol85Parser.relationSignCondition):
		count = ctx.getChildCount()
		if count == 3:
			if ctx.children[2].getText().upper() == "ZERO":
				return self.arithmeticExpressionget(ctx.children[0]) + " == 0"
			elif ctx.children[2].getText().upper() == "POSITIVE":
				return self.arithmeticExpressionget(ctx.children[0]) + " > 0"
			elif ctx.children[2].getText().upper() == "NEGATIVE":
				return self.arithmeticExpressionget(ctx.children[0]) + " < 0"
		elif ctx.children[2].getText().upper() == "NOT":
			if ctx.children[1].getText().upper() == "ZERO":
				return self.arithmeticExpressionget(ctx.children[0]) + " != 0"
			elif ctx.children[1].getText().upper() == "POSITIVE":
				return self.arithmeticExpressionget(ctx.children[0]) + " <= 0"
			elif ctx.children[1].getText().upper() == "NEGATIVE":
				return self.arithmeticExpressionget(ctx.children[0]) + " >= 0"
		else :
			print("Error in relationSignCondition")
	def relationArithmeticComparisonget(self,ctx:Cobol85Parser.relationArithmeticComparison):
		return self.arithmeticExpressionget(ctx.children[0]) + " " + self.relationalOperatorget(ctx.children[1]) + " " + self.arithmeticExpressionget(ctx.children[2])
	def relationCombinedComparisonget(self,ctx:Cobol85Parser.relationCombinedComparison):
		return self.arithmeticExpressionget(ctx.children[0]) + " " + self.relationalOperatorget(ctx.children[1]) + "(" +  self.relationCombinedConditionget(ctx.children[3]) + ")"
	def relationCombinedConditionget(self,ctx:Cobol85Parser.relationCombinedCondition):
		count = ctx.getChildCount()
		string = self.arithmeticExpressionget(ctx.children[0])
		temp = 1
		while temp != count:
			if ctx.children[temp].getText().upper() == "AND":
				string += " and " + self.arithmeticExpressionget(ctx.children[temp+1])
			else:
				string += " or " + self.arithmeticExpressionget(ctx.children[temp+1])
			temp += 2
		return string
	def relationalOperatorget(self,ctx:Cobol85Parser.relationalOperator):
		operator_input = ctx.getText().upper()
		print(operator_input," ((((((((((((((((()))))))))))))))))")
		operator_mapping = {">": ">", ">": ">", "<": "<", "<": "<", "=": "==", "=": "==", "<>": "!=", ">=": ">=", "MORETHANOREQUAL": ">=", "LESSTHANOREQUALTO": "<=", "LESSTHANOREQUAL": "<="}
		negated_operator_mapping = {">": "<=", "<": ">=", "=": "!=", ">=": "<", "<=": ">", "<>": "=="}
		if operator_input.startswith("IS"):
			operator_input = operator_input[2:]
		elif operator_input.startswith("ARE"):
			operator_input = operator_input[3:]
		if operator_input.startswith("NOT"):
			operator_input = operator_input[3:]
			return negated_operator_mapping.get(operator_input, operator_input)

		return operator_mapping.get(operator_input, operator_input)
#Abbrevation is not done yet

	def arithmeticExpressionget(self,ctx:Cobol85Parser.arithmeticExpression):
		node_type = type(ctx)
		# print(node_type,"-----------------")
		if node_type == Cobol85Parser.ArithmeticExpressionContext:
			# Handle the root arithmetic expression
			# print(ctx.getText()," uyusyud ft ")
			return self.arithmeticExpressionget(ctx.children[0]) + ''.join(self.arithmeticExpressionget(child) for child in ctx.children[1:])
	
		elif node_type == Cobol85Parser.PlusMinusContext:
			# Handle addition and subtraction
			operator = '+' if ctx.children[0].getText() == '+' else '-'
			return operator + self.arithmeticExpressionget(ctx.children[1])
	
		elif node_type == Cobol85Parser.MultDivsContext:
			# Handle multiplication and division
			return self.arithmeticExpressionget(ctx.children[0]) + ''.join(self.arithmeticExpressionget(child) for child in ctx.children[1:])
	
		elif node_type == Cobol85Parser.MultDivContext:
			# Handle multiplication (*) or division (/)
			operator = '*' if ctx.children[0].getText() == '*' else '/'
			return operator + self.arithmeticExpressionget(ctx.children[1])
	
		elif node_type == Cobol85Parser.PowersContext:
			# Handle power (**) with possible sign
			current_child = 0
			if ctx.children[current_child].getText() in ['+', '-']:
				sign = ctx.children[current_child].getText()
				current_child += 1
			else:
				sign = ''
			base = self.arithmeticExpressionget(ctx.children[current_child])
			current_child += 1
			exponent = ''.join(f' ** {self.arithmeticExpressionget(ctx.children[i].children[1])}' for i in range(current_child, len(ctx.children), 1))
			return sign + base + exponent
	
		elif node_type == Cobol85Parser.BasisContext:
			# Handle parentheses, identifiers, and literals
			if ctx.children[0].getText() == '(':
				return f'({self.arithmeticExpressionget(ctx.children[1])})'
			elif type(ctx.children[0]) == Cobol85Parser.IdentifierContext:
				# print (type(ctx.children[0])," 00000000000000000 ")
				# print (ctx.children[0].getText()," iuhiu huo hoiuh iu")
				# return ""
				return f'{self.getStringGen(ctx.children[0])}'
			elif type(ctx.children[0]) == Cobol85Parser.LiteralContext:
				return str(ctx.children[0].getText())
		# Default case, in case something is not handled
		return ''
	def visitArithmeticExpression(self, ctx:Cobol85Parser.ArithmeticExpressionContext):
		# print(self.arithmeticExpressionget(ctx),"------------------")
		return self.visitChildren(ctx)
	
	def visitDataValueClause(self, ctx:Cobol85Parser.DataValueClauseContext):
		i = 0
		for child in ctx.children:
			if type(child)==Cobol85Parser.DataValueIntervalContext:
				break
			i+=1
		countchil = ctx.getChildCount()
		arr = []
		brr = []
		while i != countchil:
			if ctx.children[i].getChildCount()==1:
				brr.append(ctx.children[i].getText())
			else:
				a = ctx.children[i].children[0].getText()
				b = ctx.children[i].children[1].children[1].getText()
				pair = (a,b)
				arr.append(pair)
			i+=1
		# print(arr, " arr===============")
		# print(brr, " brr===============")
		return arr,brr
	
	