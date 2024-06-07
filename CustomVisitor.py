from Cobol85Visitor import Cobol85Visitor
from Cobol85Parser import Cobol85Parser

class CustomVisitor(Cobol85Visitor):
    def __init__(self):
        Cobol85Visitor.__init__()
        
    #overide
    def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
        print(ctx.children[1].getText())
        return self.visitChildren(ctx)
