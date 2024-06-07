from antlr4 import *
from Cobol85Lexer import Cobol85Lexer
from Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable

file_path = './tests/shop.cbl'
def main(file_path):
    input_stream = FileStream(file_path)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    visitor = SymbolTable()
    visitor.visit(tree=tree)
    print(visitor.__repr__())

if __name__ == '__main__':
    main(file_path)
