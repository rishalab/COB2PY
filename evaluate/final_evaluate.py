import os
import shutil
import subprocess
import openpyxl

def find_cobol_files(folder):
    """Find all COBOL files in the folder."""
    cobol_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".cob"):
                cobol_files.append(os.path.join(root, file))
    return cobol_files

def generate_python_file(cobol_file):
    """Run the COBOL file through a Python script to generate a Python file based on COBOL filename."""
    try:
        # Run the COBOL file conversion script (using placeholder 'testing.py')
        subprocess.run(["python3", "..\\testing.py", cobol_file], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {cobol_file} to Python: {e}")
        return False

def copy_python_file(cobol_file, dest_folder):
    """Copy the converted Python file to destination folder with the same name as the COBOL file."""
    cobol_basename = os.path.splitext(os.path.basename(cobol_file))[0]  # Get the base name of COBOL file
    python_filename = f"{cobol_basename}.py"  # Create Python filename based on COBOL file
    
    try:
        shutil.move("converted.py", os.path.join(dest_folder, python_filename))  # Move the file to destination
    except Exception as e:
        print(f"Error copying the converted file: {e}")
        return None
    return python_filename

def run_test_case(python_file, input_file, output_file):
    """Run the Python file with the input file and compare the output to the expected output."""
    with open(input_file, 'r') as infile:
        input_data = infile.read()

    try:
        result = subprocess.run(["python3", python_file], input=input_data, text=True, capture_output=True, check=True)
        with open(output_file, 'r') as outfile:
            expected_output = outfile.read()
            if result.stdout.strip() == expected_output.strip():
                return True
    except subprocess.CalledProcessError as e:
        print(f"Error running test case with {python_file}: {e}")
    return False

def run_all_tests(python_file, in_folder, out_folder):
    """Run all the test cases and return the number of passed and failed tests."""
    passed = 0
    failed_tests = []

    in_files = sorted(os.listdir(in_folder))
    out_files = sorted(os.listdir(out_folder))

    for in_file, out_file in zip(in_files, out_files):
        in_path = os.path.join(in_folder, in_file)
        out_path = os.path.join(out_folder, out_file)
        
        if run_test_case(python_file, in_path, out_path):
            passed += 1
        else:
            failed_tests.append(in_file)

    total_tests = len(in_files)
    return passed, total_tests, failed_tests

def update_excel(folder_name, cobol_file, converted_file, passed, total_tests, excel_file):
    """Update the Excel file with the folder name, COBOL file, converted filename, pass percentage, and ratio."""
    percentage = (passed / total_tests) * 100 if total_tests > 0 else 0
    ratio = f"{passed}/{total_tests}"


    folder_name_only = os.path.basename(folder_name)

    if not os.path.exists(excel_file):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Folder Name", "COBOL File", "Converted File", "Percentage", "Ratio"])
    else:
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

    sheet.append([folder_name_only, os.path.basename(cobol_file), converted_file, percentage, ratio])
    workbook.save(excel_file)


def process_folder(base_folder):
    cobol_files = find_cobol_files(base_folder)
    if not cobol_files:
        print(f"No COBOL files found in {base_folder}.")
        return
    
    for cobol_file in cobol_files:
        print(f"COBOL file found: {cobol_file}")
        if not generate_python_file(cobol_file):
            print(f"Python file generation failed for {cobol_file}.")
            continue
        
        # Copy the converted Python file with the same name as the COBOL file
        final_converted_file = copy_python_file(cobol_file, base_folder)
        if not final_converted_file:
            print(f"Failed to move and rename converted.py for {cobol_file}.")
            continue

        in_folder = os.path.join(base_folder, "tc", "in")
        out_folder = os.path.join(base_folder, "tc", "out")
        
        passed, total_tests, failed_tests = run_all_tests(os.path.join(base_folder, final_converted_file), in_folder, out_folder)
        
        print(f"Test cases passed for {final_converted_file}: {passed}/{total_tests}")
        if failed_tests:
            print(f"Failed test cases for {final_converted_file}: {failed_tests}")
        
        excel_file = os.path.join(base_folder, "../outice.xlsx")
        update_excel(base_folder, cobol_file, final_converted_file, passed, total_tests, excel_file)

def main():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    for folder in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, folder)
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_path}")
            process_folder(folder_path)

if __name__ == "__main__":
    main()
