import re
def preprocess_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        comments = []
        preprocessed_lines = []
        first_line = lines[0].lstrip() if lines else ""
        if not any(re.match(r'^\s*IDENTIFICATION\s*DIVISION\.', line, re.IGNORECASE) for line in lines):
            preprocessed_lines.insert(0, "IDENTIFICATION DIVISION.")
        line_number = 1
        for line in lines:
            line = re.sub(r'^\d{6}\s*', '', line)
            # print(line)
            stripped_line = line.lstrip()
            # Remove lines where '*' is the first non-space character
            if stripped_line.startswith('*'):
                if stripped_line.startswith('*>'):
                    comments.append([stripped_line[2:].strip(), line_number])
                else:
                    comments.append([stripped_line[1:].strip(), line_number])
                line_number += 1
                continue
            # Remove inline comments starting with '*>'
            line = line.split('*>')[0]
            if re.search(r'(?<!\bnot\s)(?<!\bis\s)ZERO', line):
                line = line.replace('ZERO', '0')
            line = line.replace('SPACE', "' '")
            line = line.replace('SPACES', "' '")
            line = line.replace('QUOTE', "'")
            line = line.replace('QUOTES', "'")
            if stripped_line.startswith('DISPLAY') and line.rstrip().endswith("UPON CONSOLE"):
                line = line.rsplit("UPON CONSOLE", 1)[0].rstrip()
            # Strip trailing spaces or any unnecessary formatting
            preprocessed_lines.append(line.rstrip())
            preprocessed_lines.append('\n')
            line_number += 1
        # Join the processed lines into a single block of text
        preprocessed_data = ''.join(preprocessed_lines)
        # print("-------------------------------------------------\n"+preprocessed_data)
        return preprocessed_data, comments

    except Exception as e:
        print(f"Error preprocessing file: {e}")