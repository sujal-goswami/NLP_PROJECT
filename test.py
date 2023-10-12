import re

# Function to preprocess a text file
def preprocess_text_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove lines that contain only a page number
    cleaned_lines = [line for line in lines if not re.fullmatch(r'\d+\n', line)]

    # Remove chapter names (e.g., CHAPTER ONE, CHAPTER TWO, etc.)
    cleaned_lines = [re.sub(r'CHAPTER \w+', '', line) for line in cleaned_lines]

    # Convert the list of lines back to a single string
    text = ''.join(cleaned_lines)

    # Remove extra whitespace and line breaks
    text = ' '.join(text.split())

    # Write the preprocessed text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)


