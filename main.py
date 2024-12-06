from antlr4 import *
from antlr.Cobol85Lexer import Cobol85Lexer
from antlr.Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable
import os
import subprocess
from other.FileWriter import FileWriter
from other.processend import process_file
from other.preprocessing import preprocess_file
import argparse
parser = argparse.ArgumentParser(description="Command-Line Interface")
parser.add_argument('--src', type=str, help='source file', required=True)
parser.add_argument('--dest', type=str, help='dest file',required=True)
parser.add_argument('--name', type=str, help='name of file',required=True)
args = parser.parse_args()


file_path = args.src
name = args.name
dest = args.dest
def main(file_path,name,dest):
    preprocess = preprocess_file(file_path)
    input_stream = FileStream(preprocess)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    sym_tab=SymbolTable()
    sym_tab.visit(tree=tree)
    print(sym_tab.stringify())
    initCode = sym_tab.getCode()
    writer = FileWriter(name,dest)
    writer.writeHeader()
    writer.constructor(sym_tab.addressMap)
    mapaddress=writer.writeGetterAndSetter(sym_tab.addressMap)
    writer.intializer(mapaddress)
    visitor = CustomVisitor(parser,sym_tab,mapaddress)
    visitor.python_code=initCode
    visitor.visit(tree=tree)
    with open(os.path.join(".","converted.py"),"a+") as f:
        f.write(visitor.get_python_code())
    process_file('converted.py')
    with open(os.path.join(".","converted.py"),"a+") as f:
        f.write("\t\texit()\nconverted().main()")     
    # --------------------------------Files operations------------------------------------
    filename = os.path.basename(file_path)
    output_python_filename = filename.split('.')[0] + "_python_output.py"
    output_st_filename = filename.split('.')[0] + "_symbol_table.txt"
    # with open(os.path.join("./outputs/symbol_tables", output_st_filename), "w") as f:
    #     f.write("Generated Symbol Table : \n\n")
    #     f.write(sym_tab.__repr__())
    # with open(os.path.join("./outputs/python_codes", output_python_filename), "w") as f:
    #     f.write("# Generated Python Code:\n")
    #     f.write(visitor.get_python_code())
    # user_input = input("Enter '1' to execute the generated Python script: ")
    # if user_input == '1':
    #     run_output_filename = filename.split('.')[0] + "_python_run.txt"
    #     subprocess.run(["python", os.path.join("./outputs/python_codes", output_python_filename)], check=True, stdout=subprocess.DEVNULL)
    #     with open(os.path.join("./outputs/python_codes", run_output_filename), "w") as f_out:
    #         result = subprocess.run(["python", os.path.join("./outputs/python_codes", output_python_filename)], stdout=subprocess.PIPE)
    #         output = result.stdout.decode('utf-8').strip()
    #         f_out.write(output)
    with open(os.path.join("./outputs/python_codes", output_python_filename), "w") as f, open('./converted.py', 'r') as source:
        f.write(source.read())
    # #-------------------------------------------------------------------------------------

if __name__ == '__main__':
    main(file_path)

'''issues
1.commented lines in cobol is not being ignored
By default sign is trailing in cobol
'''
