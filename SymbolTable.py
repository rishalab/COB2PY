from Cobol85Parser import Cobol85Parser
from Cobol85Visitor import Cobol85Visitor
from collections import defaultdict 


class SymbolCell():

    def __init__(self,dataName,level,length,picture):
        self.dataName=dataName
        self.level=level
        self.length=length
        self.usage =1
        self.picture=picture
        self.ref=False
        self.isMod=False
        self.isSuppressed=False
        self.initialized=False
        self.children = []
        self.value=None
    
    def incrementUsage(self):
        self.usage+=1


class SymbolTable(Cobol85Visitor):

    def __init__(self):
        Cobol85Visitor.__init__(self)
        self.table = defaultdict(SymbolCell)
        self.prevLevelNumber = 0
        self.lastDataName:list[str] = ["" for i in range(49)]

    def addCell(self,symbolCell:SymbolCell):
        
        self.table[symbolCell.dataName]=symbolCell
    
    def getCell(self,dataName):
        return self.table[dataName]
    
    def stringify(self):
        result = "Symbol Table \n"
        for varible in self.table.values():
            result += f'{varible.dataName} {varible.level} {varible.picture} {varible.length}\n'
        return result
    
    def __repr__(self):
        return self.stringify()
    
    def getCode(self):
        code=''
        
        
        return code
    def getlastDataName(self,level):
        start = level-1
        while(self.lastDataName[start]==""):
            start-=1
            if start <0:
                break
        return self.lastDataName[start]

    #override
    def visitDataDescriptionEntry(self, ctx:Cobol85Parser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # override
    def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
        #print("hi1234",self.lastDataName,ctx.children[1].getText())
        if ctx.children[0].getText()=='77':
            if len(ctx.children)==4:
                level='77'
                dataName = ctx.children[1].getText()
                picture = ctx.children[2].children[1].getText()
                if '(' not in picture:
                    length=len(picture)
                    picture = picture[0]
                else:
                    length=int(picture[2:-1])
                    picture = picture[0]
                self.addCell(SymbolCell(dataName,level,length,picture))
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
                cell = SymbolCell(dataName,level,length,picture)
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
            dataName,picture,length,value='','',0,None
            for child in ctx.children:
                types .append(type(child))
                if type(child)==Cobol85Parser.DataNameContext:
                    dataName = child.getText()
                if type(child)==Cobol85Parser.DataPictureClauseContext:
                    picture = child.children[-1].getText()
                if type(child)==Cobol85Parser.DataValueClauseContext:
                    value = child.children[-1].getText()
                    if picture[0]=='9' and value.upper()=='ZEROS':
                        value = 0
                    elif value.upper()=='SPACES':
                        value = ' '*length
                    value= int(value) if picture[0]=='9' else value

            if Cobol85Parser.DataPictureClauseContext in types:
                cell= SymbolCell(dataName,level,length,picture)
                cell.value = value if value is not None else None
                if int(ctx.children[0].getText())!=1:
                    #print("level is",level)
                    self.table[self.getlastDataName(level-1)].children.append(SymbolCell(dataName,level,length,picture))
                else:
                    self.addCell(SymbolCell(dataName,level,length,picture))
            else:
                if int(ctx.children[0].getText())!=1:
                    self.table[self.getlastDataName(level-1)].children.append(SymbolCell(dataName,level,-1,'Record'))
                    self.addCell(self.table[self.getlastDataName(level-1)].children[-1])
                    self.lastDataName.pop(level-1)
                    self.lastDataName.insert(level-1,dataName)
                else:
                    self.addCell(SymbolCell(dataName,level,-1,'Record'))
                    #print(dataName,self.lastDataName)
                    self.lastDataName.pop(0)
                    self.lastDataName.insert(0,dataName)
               
        return self.visitChildren(ctx)



    


    # override
    def visitDataDescriptionEntryFormat2(self, ctx:Cobol85Parser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # override
    def visitDataDescriptionEntryFormat3(self, ctx:Cobol85Parser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    
