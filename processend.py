import re
import os
def extract_function_name(func_string):
    match = re.search(r'def\s+(\w+)\s*\(', func_string)
    if match:
        return match.group(1)
    return None

def add_function_call_after_main(file_path):
    if not os.path.isfile(file_path):
        print("File not found.")
        return
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    main_index = None
    first_function_index = None

    for index, line in enumerate(lines):
        if 'def main' in line and main_index is None:
            main_index = index
        elif main_index is not None and line.strip().startswith('def '):
            first_function_index = index
            break
    
    if main_index is not None and first_function_index is not None:
        lines.insert(first_function_index, f'\t\tself.{extract_function_name(lines[first_function_index].strip())}_flow()\n')
        
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        pass

def process_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    functions_after_main = []
    copying_started = False
    function_regex = re.compile(r'\s*def\s+(\w+)\(')

    for i, line in enumerate(lines):
        new_lines.append(line)
        if "def main(" in line:
            copying_started = False
        match = function_regex.match(line)
        if match:
            func_name = match.group(1)
            if copying_started:
                functions_after_main.append((i, func_name))
            if func_name == "main":
                copying_started = True

    num_functions = len(functions_after_main)
    
    for index, (func_index, func_name) in enumerate(functions_after_main):
        new_lines.append('\n')
        new_lines.append(lines[func_index].replace(func_name, func_name + "_flow"))
        for body_line in lines[func_index + 1:]:
            if function_regex.match(body_line):
                break
            new_lines.append(body_line)
        if index < num_functions - 1:
            next_func_name = functions_after_main[index + 1][1]
            new_lines.append(f"\t\tself.{next_func_name}_flow()\n")
    with open(file_path, 'w') as f:
        f.writelines(new_lines)
    add_function_call_after_main(file_path)

# process_file('converted.py')