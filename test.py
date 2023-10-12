import re
import nltk
nltk.download('punkt')
import string


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


def tokenization(input_file):
# Opening the text-converted book.
    file = open( input_file, encoding = 'utf-8' )

    listofwords = file.read().splitlines()

    listofwords = [i for i in listofwords if i != ' ']

    text = " "

    text = text.join(listofwords)

# Defining string which contains the punctuations which have ot be ignored.
    punctuations = string.punctuation

    filteredtext = ""

    for i in text:
        if i not in punctuations:
            filteredtext = filteredtext + i
    
# Converting the result to lower-case
    filteredtext = filteredtext.lower()
    tokenisedtext = nltk.tokenize.word_tokenize(filteredtext)
    print( tokenisedtext[:10]) # This prints out the first 10 tokens of the filtered text.


tokenization("preprocessed.txt")