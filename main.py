import argparse
import os
import subprocess
from antlr4 import *
from antlr.Cobol85Lexer import Cobol85Lexer
from antlr.Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable
from other.FileWriter import FileWriter
from other.preprocessing import preprocess_file
from other.processend import process_file

active_file = './active_test.cbl'

def main(file_path):
    content, comments = preprocess_file(file_path)
    with open(active_file, 'w') as file:
        file.write(content)
    input_stream = FileStream(active_file)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()
    sym_tab = SymbolTable()
    sym_tab.visit(tree=tree)
    sym_tab.stringify()
    initCode = sym_tab.getCode()
    writer = FileWriter()
    writer.writeHeader()
    writer.writeComments(comments)
    writer.constructor(sym_tab.addressMap)
    mapaddress = writer.writeGetterAndSetter(sym_tab.addressMap)
    writer.intializer(mapaddress)
    visitor = CustomVisitor(parser, sym_tab, mapaddress)
    visitor.python_code = initCode
    visitor.visit(tree=tree)
    with open(os.path.join(".", "converted.py"), "a+") as f:
        f.write(visitor.get_python_code())
    process_file('converted.py')
    with open(os.path.join(".", "converted.py"), "a+") as f:
        f.write("\t\texit()\nconverted().main()")
    # --------------------------------Files operations------------------------------------
    filename = os.path.basename(file_path)
    output_python_filename = filename.split('.')[0] + "_python_output.py"
    output_st_filename = filename.split('.')[0] + "_symbol_table.txt"
    with open(os.path.join("./outputs/python_codes", output_python_filename), "w") as f, open('./converted.py', 'r') as source:
        f.write(source.read())
    # #-------------------------------------------------------------------------------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="COBOL TO PYTHON TRANSLATOR",
        epilog="Example: python main.py ./tests/ADD.cbl"
    )
    parser.add_argument(
        'file_path', 
        type=str, 
        help='Path to the COBOL file to process'
    )

    # Parse arguments
    args = parser.parse_args()

    # Validate arguments
    if not os.path.isfile(args.file_path):
        print(f"Error: The file '{args.file_path}' does not exist.")
        print("Usage: python main.py <file_path>")
        exit(1)

    main(args.file_path)

    # Extract the base name without extension to display
    output_file_name = os.path.basename(args.file_path).split('.')[0] + "_python_output.py"
    print("Conversion successful\n")
    print(f"Check the 'outputs/python_codes/{output_file_name}' file or './converted.py' file for the output Python file\n")
    
