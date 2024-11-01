import re
def preprocess_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        preprocessed_lines = []
        first_line = lines[0].lstrip() if lines else ""
        if not re.match(r'^IDENTIFICATION\s*DIVISION\.', first_line):
            preprocessed_lines.append("IDENTIFICATION DIVISION.")
        for line in lines:
            line = re.sub(r'^\d{6}\s*', '', line)
            # print(line)
            stripped_line = line.lstrip()
            # Remove lines where '*' is the first non-space character
            if stripped_line.startswith('*'):
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
        # Join the processed lines into a single block of text
        preprocessed_data = '\n'.join(preprocessed_lines)

        return preprocessed_data

    except Exception as e:
        print(f"Error preprocessing file: {e}")