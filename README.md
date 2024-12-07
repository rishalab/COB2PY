
# COB2PY: A COBOL to Python Translator

COB2PY is an open-source tool that translates COBOL code into equivalent Python code. Using a rule-based approach, COB2PY facilitates the migration of legacy COBOL systems to Python, generating Python code in an object-oriented paradigm.

---

## Tool Description
COB2PY aims to simplify the migration process of COBOL legacy systems for developers and industries. It translates COBOL programs into Python code, easing the understanding and modernization of older systems.

---

## Features
- **Abstract Syntax Tree (AST) Generation**: Constructs ASTs from COBOL code using the ANTLR4 parser.
- **Symbol Table Generation**: Extracts and stores variable information from the data division.
- **Procedure Division Analysis**: Maps COBOL statements to Python while adapting variable syntax.
- **Code Generation**: Produces a Python class representing the COBOL code with equivalent functionality.

---

## Installation

### Requirements

#### Step 1: Create and activate a Python virtual environment

```bash
python(3) -m venv <path_to_env/env_name>
```

#### Step 2: Clone the repository

HTTPS:
```bash
git clone https://github.com/Kowshik0514/cobol_to_python.git
```

SSH:
```bash
git clone git@github.com:Kowshik0514/cobol_to_python.git
```
Navigate to the `cobol_to_python` directory:
```bash
cd cobol_to_python
```
#### Step 3: Install the dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Run the tool


Run the main script with the input file path:
```bash
python(3) main.py input_file_path
```

> **Note**: The generated Python file requires `Program.py` (dependency file) to execute.

---

## Approach

COB2PY's translation process involves four main phases:

1. **Abstract Syntax Tree (AST) Generation**:  
   - The AST is constructed using ANTLR4 based on the COBOL grammar from the [ANTLR Grammars-V4 repository](https://github.com/antlr/grammars-v4).

2. **Symbol Table Generation**:  
   - Information from the Data Division of the COBOL program is stored in a symbol table.

3. **Procedure Division Analysis**:  
   - Maps COBOL statements to equivalent Python code with necessary variable renaming.

4. **Translated Code Generation**:  
   - Outputs Python code as a class, preserving the control flow of the original COBOL program.

![COB2PY Architecture (1)](https://github.com/user-attachments/assets/050a982b-64e6-48d6-b9a9-7933321570ce)

---

## Goal
The tool's primary goal is to reduce the effort and complexity of migrating COBOL-based systems to Python. COB2PY empowers developers and industries to modernize legacy systems efficiently.

---

## Results
COB2PY was tested on 103 COBOL programs from the CodeNet dataset, which includes programs from AIZU and AtCoder platforms. Key results:
- **99 programs passed all test cases.**
- **Test case pass percentage: 98.35%.**

This demonstrates the tool's effectiveness and accuracy for supported COBOL constructs.

---

## Demo Video
[Watch the COB2PY Demo Video](https://www.youtube.com/embed/nCmbjJUf78E?rel=0)

---

## Contributors
- Kowshik Reddy Challa
- Sonith M V
- Chiranjeevi B S
- Sridhar Chimalakonda
