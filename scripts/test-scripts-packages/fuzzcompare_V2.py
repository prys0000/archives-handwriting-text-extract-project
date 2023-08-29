from fuzzywuzzy import fuzz
import pandas as pd

def calculate_accuracy(row):
    # Retrieve the values from the specified columns (change 'A' and 'B' to the actual column labels)
    text_a = str(row['Text'])
    text_b = str(row['transcribed text'])

    # Normalize strings (convert to lowercase and remove punctuation, for example)
    normalized_text_a = text_a.lower()
    normalized_text_b = text_b.lower()

    # Calculate similarity score using token sort ratio
    similarity_score = fuzz.token_sort_ratio(normalized_text_a, normalized_text_b)

    return similarity_score

# Read the input Excel file
data = pd.read_excel('xomparisonV1.xlsx')

# Add a new column for the accuracy results
data['Accuracy'] = data.apply(calculate_accuracy, axis=1)

# Save the updated data to a new Excel file
data.to_excel('output.xlsx', index=False)
