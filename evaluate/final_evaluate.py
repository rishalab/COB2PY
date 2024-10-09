import os
import shutil
import subprocess
import openpyxl

def find_cobol_file(folder):
    """Find the first COBOL file in the folder."""
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".cob"):
                return os.path.join(root, file)
    return None

def generate_python_file(cobol_file):
    """Run the COBOL file through a Python script to generate 'converted.py'."""
    converted_file = "converted.py"
    try:
        # Assuming you have a script or command to convert COBOL to Python
        subprocess.run(["python3", "..\\testing.py", cobol_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {cobol_file} to Python: {e}")
        return None
    return converted_file

def copy_python_file(converted_file, dest_folder):
    """Copy the converted Python file to the destination folder."""
    try:
        shutil.copy(converted_file, dest_folder)
    except Exception as e:
        print(f"Error copying {converted_file}: {e}")

def run_test_case(python_file, input_file, output_file):
    """Run the Python file with the input file and compare the output to the expected output."""
    with open(input_file, 'r') as infile:
        input_data = infile.read()

    try:
        result = subprocess.run(["python3", python_file], input=input_data, text=True, capture_output=True, check=True)
        with open(output_file, 'r') as outfile:
            expected_output = outfile.read()
            # Compare the output
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

def update_excel(folder_name, passed, total_tests, excel_file):
    """Update the Excel file with the folder name, pass percentage, and ratio."""
    percentage = (passed / total_tests) * 100 if total_tests > 0 else 0
    ratio = f"{passed}/{total_tests}"

    if not os.path.exists(excel_file):
        # Create a new Excel file if it doesn't exist
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Folder Name", "Percentage", "Ratio"])
    else:
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

    # Add the new data
    sheet.append([folder_name, percentage, ratio])
    workbook.save(excel_file)

def process_folder(base_folder):
    """Process a single folder containing COBOL files and test cases."""
    # Step 1: Find the COBOL file in the folder
    cobol_file = find_cobol_file(base_folder)
    if cobol_file is None:
        print(f"No COBOL file found in {base_folder}.")
        return
    print(f"COBOL file found: {cobol_file}")
    
    # Step 2: Convert COBOL to Python
    converted_file = generate_python_file(cobol_file)
    if not converted_file:
        print(f"Python file generation failed for {base_folder}.")
        return
    
    # Step 3: Copy the Python file to the target folder
    copy_python_file(converted_file, base_folder)
    
    # Step 4: Run the Python file with test cases
    in_folder = os.path.join(base_folder, "tc", "in")
    out_folder = os.path.join(base_folder, "tc", "out")
    
    passed, total_tests, failed_tests = run_all_tests(os.path.join(base_folder, converted_file), in_folder, out_folder)
    
    # Step 5: Print the results
    print(f"Test cases passed for {base_folder}: {passed}/{total_tests}")
    if failed_tests:
        print(f"Failed test cases: {failed_tests}")
    
    # Step 6: Update the Excel sheet
    excel_file = os.path.join(base_folder, "outice.xlsx")
    update_excel(base_folder, passed, total_tests, excel_file)

def main():
    current_folder = os.getcwd()
    
    # Find all folders that start with "p0"
    folders = [f for f in os.listdir(current_folder) if f.startswith("p0") and os.path.isdir(f)]
    
    # Process each folder
    for folder in folders:
        print(f"Processing folder: {folder}")
        process_folder(folder)

if __name__ == "__main__":
    main()
