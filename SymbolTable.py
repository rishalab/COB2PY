from antlr.Cobol85Parser import Cobol85Parser
from antlr.Cobol85Visitor import Cobol85Visitor
from collections import defaultdict 
import re


class SymbolCell():

	def __init__(self,dataName,level,length,picture,occurs,picInfo,value,parents):
		self.dataName=dataName
		self.level=level
		self.length=length
		self.occurs = occurs
		self.picture=picture
		self.ref=False
		self.isMod=False
		self.isSuppressed=False
		self.initialized=False
		self.children = []
		self.parents = parents
		self.value=value
		self.picInfo=picInfo


class SymbolTable(Cobol85Visitor):

	def __init__(self):
		Cobol85Visitor.__init__(self)
		self.table = defaultdict(SymbolCell)
		self.prevLevelNumber = 0
		self.levelContextStack=[]
		self.memoryAdresss=[]
		self.addressMap = []
		self.memoryPointer=0
		self.memoryPointer2=0

	def addCell(self,symbolCell:SymbolCell):
		
		self.table[symbolCell.dataName]=symbolCell
	
	def getCell(self,dataName):
		return self.table[dataName]
	
	def stringify(self):
		result = "Symbol Table \n"
		for varible in self.table.values():
			if varible.level==1:
				result += f'{varible} {varible.dataName} {varible.level} {varible.picture} {varible.length}\n'
				print(f' {varible.dataName} {varible.level} {varible.picture} {varible.length}')
				ans = self.dfs(varible,0)
				print("size is ",ans)

		print("checking length--------------------------------------------------------------------------")
		for varible in self.table.values():
			if varible.level==1:
				self.dfs2(varible,0,1)
				self.memoryPointer2=self.memoryPointer=varible.length
		for x in self.addressMap:
			print(x)

		
	

	def dfs(self,variable,level)->int:
		if len((variable.children))!=0:
			length = 0
			for child in variable.children:
				#print(f'{child} {child.dataName} {child.level} {child.picture} {child.length} level{level} {len(child.children)}')
				#print("ins ",child.dataName,' le:',length)
				length+=self.dfs(child,level+1)*child.occurs
				#print("ins----------------------------------- ",child.dataName,' le:',length)
			#print("recu ",length,variable.dataName)
			variable.length=length
			return length
		else:
			#print("recu1 ",variable.length,variable.dataName)
			return variable.length
	
	def dfs2(self,variable,level,occ):
		print(f'{variable.dataName} {variable.level} {variable.picInfo} len:{variable.length} occurs{variable.occurs} {len(variable.children)}')

		self.addressMap.append([variable,variable.dataName,self.memoryPointer,variable.occurs*variable.length,variable.length,variable.picInfo])
		#print(":: ",variable.dataName,self.memoryPointer,self.memoryPointer2)
		memoryPointer2 = self.memoryPointer
		#print(":: ",variable.dataName,self.memoryPointer,self.memoryPointer2)
		for child in variable.children:
			self.dfs2(child,level,occ)
		#print(":: ",variable.dataName,self.memoryPointer,self.memoryPointer2)
		self.memoryPointer = memoryPointer2
		#print(":: ",variable.dataName,self.memoryPointer,self.memoryPointer2)
		self.memoryPointer+=((variable.occurs)*(variable.length)) if len(variable.children)!=0 else (variable.occurs*variable.length)
		

		
		
		


	
	def __repr__(self):
		return self.stringify()
	
	def getCode(self):
		code=''
		return code
	
	def parsePic(self,picture):
		integer = re.compile("(S{0,1}([9P](\\([0-9]+\\))?)*([9P](\\([0-9]+\\))?)*)")
		decimal = re.compile("(S{0,1}([9P](\\([0-9]+\\))?)*[V]([9P](\\([0-9]+\\))?)*)")
		numericEdited = re.compile("(((CR)|(DB)){0,1}S{0,1}([$PZ9B0/\\,\\<\\>\\+\\-\\*](\\([0-9]+\\))?)*([V\\.]([$PZ9B0/\\,\\<\\>\\+\\-\\*](\\([0-9]+\\))?)*)?((CR)|(DB)){0,1})")

		alphaNumericEdited = re.compile("([AX9B0/\\.\\,](\\([0-9]+\\))?)*")
		national = re.compile("([N])*")
		nationalEdited = re.compile("([WGNB09/])*")
		externalFloating = re.compile("[+-]([9.V](\\([0-9]+\\))?)*[E][+-]([9])*")
		plainText = re.compile("([AX](\\([0-9]+\\))?)*")
		if integer.fullmatch(picture) is not None:
			return self.interpret(picture,picType="integer"),'integer'
		if decimal.fullmatch(picture) is not None:
			return self.interpret(picture,picType="decimal"),'decimal'
		if numericEdited.fullmatch(picture) is not None:
			return self.interpretNumericEdited(picture),'numericEdited'
		if alphaNumericEdited.fullmatch(picture) is not None:
			return self.interpretAlphaNumericEdited(picture),'alphaNumericEdited'
		if national.fullmatch(picture) is not None:
			return picture,len(picture),'national'
		if nationalEdited.fullmatch(picture) is not None:
			return picture,len(picture),'natinalEdited'
		if externalFloating.fullmatch(picture) is not None:
			return self.interpretExternalFloating(picture),'externalFloating'
		if plainText.fullmatch(picture) is not None:
			return self.interpret(picture,picType="integer"),'plainText'

	def interpret(self,picture,picType):
		isSigned,length,i,newPicture = False,0,0,''
		if picType=="decimal":
			pi = picture.split("V") if "V" in picture else picture
			picture = pi[0]+'.'+pi[1]
		if picture[0]=='S':
			isSigned = True
			i=1
		while i<len(picture):
			if i+1 < len(picture):
				if picture[i+1]=='(':
					char = picture[i]
					#print("hi")
					i +=2
					num=''
					while picture[i]!=')':
						num +=(picture[i])
						#print(num,picture[i])
						i+=1
					#print(num)
					newPicture += char*int(num)
					length+=int(num)
				elif picture[i]=='9' or picture[i]=='A' or picture[i]=='X':
					newPicture+=picture[i]
					length+=1
				elif picture[i]=='P':
					newPicture+=picture[i]
				elif picture[i]=='.':
					newPicture+=picture[i]
			else:
				newPicture+=picture[i]
				length+=1
			i+=1
		
		return newPicture,length,isSigned
	
	def interpretNumericEdited(self,picture):
		newPicture,length,isSigned = '',0,False
		CRatStart,CRatEnd = False,False
		DBatStart,DBatEnd = False,False
		if picture.startswith("CR"):
			CRatStart = True
			picture = picture[2:]
		if picture.endswith("CR"):
			CRatEnd=True
			picture = picture[:-2]
		if picture.startswith("DB"):
			DBatStart = True
			picture = picture[2:]
		if picture.endswith("DB"):
			DBatEnd=True
			picture = picture[:-2]
		if picture[0]=='S':
			isSigned=True
			picture=picture[1:]
		i = 0
		while i<len(picture):
			if i+1 < len(picture):
				if picture[i+1]=='(':
					char = picture[i]
					#print("hi")
					i +=2
					num=''
					while picture[i]!=')':
						num +=(picture[i])
						#print(num,picture[i])
						i+=1
					#print(num)
					newPicture += char*int(num)
					length+=int(num)
				elif picture[i]=='9' or picture[i]=='A' or picture[i]=='.' or picture[i]==',' or picture[i]=='0' or picture[i]=='\\' :
					newPicture+=picture[i]
					length+=1
				elif picture[i]=='P':
					newPicture+=picture[i]
			else:
				newPicture+=picture[i]
			i+=1

		return newPicture,length,isSigned,CRatStart,CRatEnd,DBatStart,DBatEnd
	
	def interpretAlphaNumericEdited(self,picture):
		newPicture,length = '',0
		i = 0
		while i<len(picture):
			if i+1 < len(picture):
				if picture[i+1]=='(':
					char = picture[i]
					#print("hi")
					i +=2
					num=''
					while picture[i]!=')':
						num +=(picture[i])
						#print(num,picture[i])
						i+=1
					#print(num)
					newPicture += char*int(num)
					length+=int(num)
				elif picture[i]=='9' or picture[i]=='A' or picture[i]=='X' or picture[i]=='B' or picture[i]=='.' or picture[i]==',' or picture[i]=='0' or picture[i]=='\\':
					newPicture+=picture[i]
					length+=1
				elif picture[i]=='P':
					newPicture+=picture[i]
			else:
				newPicture+=picture[i]
			i+=1

		return newPicture,length

		


	#override
	def visitDataDescriptionEntry(self, ctx:Cobol85Parser.DataDescriptionEntryContext):
		return self.visitChildren(ctx)


	# override
	def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
		#print("hi1234",self.lastDataName,ctx.children[1].getText())
		if ctx.children[0].getText()=='77':
			occurs = 1
			picInfo=None
			if len(ctx.children)==4:
				level='77'
				dataName = ctx.children[1].getText().upper().replace('-','_')
				picture = ctx.children[2].children[1].getText().upper()
				if '(' not in picture:
					length=len(picture)
					picture = picture[0]
				else:
					length=int(picture[2:-1])
					picture = picture[0]
				self.addCell(SymbolCell(dataName,level,length,picture,occurs,picInfo,None))
			if len(ctx.children)==5:
				level='77'
				dataName = ctx.children[1].getText()
				picture = ctx.children[2].children[1].getText()
				if '(' not in picture:
					length=len(picture)
					picture = picture[0]
				else:
					length=int(picture[2:-1])
					picture = picture[0]
				cell = SymbolCell(dataName,level,length,picture,occurs,picInfo,None)
				cell.initialized=True
				value = ctx.children[3].children[-1].getText()
				if picture=='9' and value.upper()=='ZEROS':
					value = 0
				elif value.upper()=='SPACES':
					value = ' '*length
				cell.value= int(value) if picture=='9' else value
				self.addCell(cell)
			
		elif int(ctx.children[0].getText())<50 and int(ctx.children[0].getText())>0:
			level = int(ctx.children[0].getText())
			types = []
			dataName,picture,length,value,occurs,picInfo='','',0,None,1,None
			for child in ctx.children:
				types .append(type(child))
				if type(child)==Cobol85Parser.DataNameContext:
					dataName = child.getText().upper().replace('-','_')
				if type(child)==Cobol85Parser.DataPictureClauseContext:
					picture = child.children[-1].getText().upper()
					picInfo = self.parsePic(picture)
					picture = picInfo[0]
					# print("picinfo ",picInfo)
				if type(child)==Cobol85Parser.DataValueClauseContext:
					# need to look again
					value = child.children[-1].getText()
				if type(child)==Cobol85Parser.DataOccursClauseContext:
					minTimes = int(child.children[1].getText())
					maxTimes = None
					for chi in child.children:
						if type(chi)==Cobol85Parser.DataOccursToContext:
							maxTimes = int(chi.children[1].getText())
					occurs=maxTimes if maxTimes is not None else minTimes
					
			parents = []
			if Cobol85Parser.DataPictureClauseContext in types:
				if level==1:
					self.addCell(SymbolCell(dataName,level,picInfo[0][1],picture,occurs,picInfo,value,parents))
					self.levelContextStack.append([level,dataName])
				else:
					#print("-----------------",self.levelContextStack)
					while len(self.levelContextStack)!=0 and level <= self.levelContextStack[-1][0]:
						self.levelContextStack.pop(-1)
					parents = self.table[self.levelContextStack[-1][1]].parents +[self.table[self.levelContextStack[-1][1]]]
					self.table[self.levelContextStack[-1][1]].children.append(SymbolCell(dataName,level,picInfo[0][1],picture,occurs,picInfo,value,parents))
			else:
				if(len(self.levelContextStack)!=0):
					#print("-----------------",self.levelContextStack)
					while len(self.levelContextStack)!=0 and level <= self.levelContextStack[-1][0]:
						self.levelContextStack.pop(-1)
				if(level!=1):
					parents = self.table[self.levelContextStack[-1][1]].parents +[self.table[self.levelContextStack[-1][1]]]
					self.table[self.levelContextStack[-1][1]].children.append(SymbolCell(dataName,level,length,picture,occurs,picInfo,value,parents))
					currCell = self.table[self.levelContextStack[-1][1]].children[-1]
					self.addCell(currCell)
				else:
					self.addCell(SymbolCell(dataName,level,length,picture,occurs,picInfo,value,parents))
				self.levelContextStack.append([level,dataName])

		return self.visitChildren(ctx)
	
	# override
	def visitDataDescriptionEntryFormat2(self, ctx:Cobol85Parser.DataDescriptionEntryFormat2Context):
		return self.visitChildren(ctx)

	# override
	def visitDataDescriptionEntryFormat3(self, ctx:Cobol85Parser.DataDescriptionEntryFormat3Context):
		return self.visitChildren(ctx)