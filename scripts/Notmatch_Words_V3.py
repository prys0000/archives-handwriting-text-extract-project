import pandas as pd
import re

# Read the data from Excel
data = pd.read_excel(r'C:\Users\user\Desktop\TEXTRACT TEST FOLDER\V3_fuzzyoutput.xlsx')

# Create new columns for mismatched and matched words
data['Mismatched Words'] = ''
data['Matched Words'] = ''

# Iterate over the rows and compare the text in each pair of cells
for index, row in data.iterrows():
    text_a = str(row['Text'])  # Convert the value to string
    text_b = str(row['transcribed text'])  # Convert the value to string

    # Remove non-alphanumeric characters and convert to lowercase
    text_a = re.sub(r'\W+', ' ', text_a.lower())
    text_b = re.sub(r'\W+', ' ', text_b.lower())

    # Tokenize the text into words
    words_a = set(text_a.split())
    words_b = set(text_b.split())

    # Find the mismatched and matched words
    mismatched_words = words_a.symmetric_difference(words_b)
    matched_words = words_a.intersection(words_b)

    # Store the mismatched and matched words in the respective columns
    data.at[index, 'Mismatched Words'] = ', '.join(mismatched_words)
    data.at[index, 'Matched Words'] = ', '.join(matched_words)

# Save the updated data to a new Excel file
data.to_excel('output.xlsx', index=False)
