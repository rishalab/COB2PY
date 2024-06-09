from antlr4 import *
from Cobol85Lexer import Cobol85Lexer
from Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable

file_path = './tests/DIVIDE.cbl'
def main(file_path):
    input_stream = FileStream(file_path)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    sym_tab=SymbolTable()
    sym_tab.visit(tree=tree)
    initCode = sym_tab.getCode()
    visitor = CustomVisitor(parser,sym_tab)
    visitor.python_code=initCode
    visitor.visit(tree=tree)
    with open("./outputs/symbol_table.txt", "w") as f:
        f.write("Generated Symbol Table : \n\n")
        f.write(sym_tab.__repr__())
    with open("./outputs/python_output.py", "w") as f:
        f.write("# Generated Python Code:\n")
        f.write(visitor.get_python_code())

if __name__ == '__main__':
    main(file_path)

'''issues
1.commented lines in cobol is not being ignored
2.On SIZE ERROR,END-ADD,END-SUBTRACT
3.add Giving statement after TO only one should be there but parser is parsing for many
4.your grammar is not  taking ,(coma) as separator it is only taking space
'''
