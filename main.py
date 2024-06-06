import antlr4
from Cobol85Lexer import Cobol85Lexer
from Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor

file_path = './tests/DIVIDE.cbl'

input_stream = antlr4.FileStream(file_path)
lexer = Cobol85Lexer(input_stream)
stream = antlr4.CommonTokenStream(lexer)
parser = Cobol85Parser(stream)
tree = parser.startRule()
print(tree.toStringTree(recog=parser))
print(type(tree))
vistor = CustomVisitor()
vistor.visit(tree=tree)