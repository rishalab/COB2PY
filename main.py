from antlr4 import *
from Cobol85Lexer import Cobol85Lexer
from Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable

file_path = './tests/HELLO.cbl'
def main(file_path):
    input_stream = FileStream(file_path)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    sym_tab=SymbolTable()
    sym_tab.visit(tree=tree)
    visitor = CustomVisitor(parser,sym_tab)
    visitor.visit(tree=tree)
    print(sym_tab.__repr__())
    print("Generated Python Code:\n")
    print(visitor.get_python_code())

if __name__ == '__main__':
    main(file_path)
