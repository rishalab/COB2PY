from Cobol85Visitor import Cobol85Visitor
from Cobol85Parser import Cobol85Parser
from symbol_table import SymbolTable

class CustomVisitor(Cobol85Visitor):
    def __init__(self,parser):
        self.python_code=""
        self.parser=parser
        self.symbol_table=SymbolTable()
        Cobol85Visitor.__init__(self)

    def get_python_code(self):
        return self.python_code
    
    def get_symbol_table(self):
        return self.symbol_table
    #overide
    def visitDataDescriptionEntryFormat1(self, ctx:Cobol85Parser.DataDescriptionEntryFormat1Context):
        print(ctx.children[1].getText())
        return self.visitChildren(ctx)
