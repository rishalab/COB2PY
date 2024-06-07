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
    
    def incrementUsage(self):
        self.usage+=1


class SymbolTable(Cobol85Visitor):

    def __init__(self):
        Cobol85Visitor.__init__(self)
        self.table = defaultdict(SymbolCell)

    def addCell(self,symbolCell:SymbolCell):
        self.table[symbolCell.dataName]=symbolCell
    
    def getCell(self,dataName):
        return self.table[dataName]
    
    def stringify(self):
        result = "Symbol Table \n"
        for varible in self.table.values:
            result += f'{varible.dataName} {varible.level} {varible.picture} {varible.length}\n'
        return result
    
    def __repr__(self):
        return self.stringify()

    #override
    def visitDataDescriptionEntry(self, ctx:Cobol85Parser.DataDescriptionEntryContext):
        return self.visitChildren(ctx)


    # override
    def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
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
        return self.visitChildren(ctx)


    # override
    def visitDataDescriptionEntryFormat2(self, ctx:Cobol85Parser.DataDescriptionEntryFormat2Context):
        return self.visitChildren(ctx)


    # override
    def visitDataDescriptionEntryFormat3(self, ctx:Cobol85Parser.DataDescriptionEntryFormat3Context):
        return self.visitChildren(ctx)


    
