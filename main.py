from antlr4 import *
from Cobol85Lexer import Cobol85Lexer
from Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable

<<<<<<< HEAD
file_path = './tests/DIVIDE.cbl'
def main(file_path):
    input_stream = FileStream(file_path)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    # print(tree.toStringTree(recog=parser))
    # print(type(tree))
    visitor = CustomVisitor(parser)
    visitor.visit(tree=tree)
    
    
    print("python code\n")
    print(visitor.get_python_code())
    print(visitor.get_symbol_table())

if __name__ == '__main__':
    main(file_path)
=======
file_path = './tests/shop.cbl'

input_stream = antlr4.FileStream(file_path)
lexer = Cobol85Lexer(input_stream)
stream = antlr4.CommonTokenStream(lexer)
parser = Cobol85Parser(stream)
tree = parser.startRule()
print(tree.toStringTree(recog=parser))
print(type(tree))
vistor = SymbolTable()
vistor.visit(tree=tree)
>>>>>>> 03b2440 (Symbol table)
