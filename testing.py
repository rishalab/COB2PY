import os
import subprocess
import sys
from antlr4 import FileStream, CommonTokenStream
from antlr.Cobol85Lexer import Cobol85Lexer
from antlr.Cobol85Parser import Cobol85Parser
from CustomVisitor import CustomVisitor
from SymbolTable import SymbolTable
from FileWriter import FileWriter
from processend import process_file

def main(file_path):
    # Read the input COBOL file
    input_stream = FileStream(file_path)
    lexer = Cobol85Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Cobol85Parser(stream)
    tree = parser.startRule()

    # Process the syntax tree using SymbolTable and Visitor
    sym_tab = SymbolTable()
    sym_tab.visit(tree=tree)
    print(sym_tab.stringify())
    
    initCode = sym_tab.getCode()
    writer = FileWriter()
    writer.writeHeader()
    writer.constructor(sym_tab.addressMap)
    mapaddress = writer.writeGetterAndSetter(sym_tab.addressMap)
    writer.intializer(mapaddress)

    # Visit the tree to generate Python code
    visitor = CustomVisitor(parser, sym_tab, mapaddress)
    visitor.python_code = initCode
    visitor.visit(tree=tree)

    # Write the generated Python code to 'converted.py'
    with open(os.path.join(".", "converted.py"), "a+") as f:
        f.write(visitor.get_python_code())

    # Post-process the generated Python code
    process_file('converted.py')
    
    # Append the final part of the Python code to exit properly
    with open(os.path.join(".", "converted.py"), "a+") as f:
        f.write("\t\texit()\nconverted().main()")     

    # --------------------------------Files operations------------------------------------
    filename = os.path.basename(file_path)
    output_python_filename = filename.split('.')[0] + "_python_output.py"
    output_st_filename = filename.split('.')[0] + "_symbol_table.txt"

    # Write the generated Python code to the output folder
    # with open(os.path.join("./outputs/python_codes", output_python_filename), "w") as f, open('./converted.py', 'r') as source:
    #     f.write(source.read())

    # Optionally, write the symbol table (currently commented)
    # with open(os.path.join("./outputs/symbol_tables", output_st_filename), "w") as f:
    #     f.write("Generated Symbol Table : \n\n")
    #     f.write(sym_tab.__repr__())
    
    # # Optional: Run the generated Python code (also commented)
    # user_input = input("Enter '1' to execute the generated Python script: ")
    # if user_input == '1':
    #     run_output_filename = filename.split('.')[0] + "_python_run.txt"
    #     subprocess.run(["python", os.path.join("./outputs/python_codes", output_python_filename)], check=True, stdout=subprocess.DEVNULL)
    #     with open(os.path.join("./outputs/python_codes", run_output_filename), "w") as f_out:
    #         result = subprocess.run(["python", os.path.join("./outputs/python_codes", output_python_filename)], stdout=subprocess.PIPE)
    #         output = result.stdout.decode('utf-8').strip()
    #         f_out.write(output)

if __name__ == '__main__':
    # Check if a file path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Verify that the file exists
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Run the main function with the provided file path
    main(file_path)
