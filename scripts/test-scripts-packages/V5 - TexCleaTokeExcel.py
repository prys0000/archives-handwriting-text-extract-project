import boto3
import re
import nltk
from spellchecker import SpellChecker
import time
import pandas as pd

# S3 bucket name
s3BucketName = "wickershamtest"

# AWS region
awsRegion = "us-east-1"  # Replace with your desired region

# Amazon Textract client
textract = boto3.client('textract', region_name=awsRegion)

# Create an S3 client
s3_client = boto3.client('s3', region_name=awsRegion)

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Initialize SpellChecker
spell = SpellChecker()

# Retrieve the list of objects in the S3 bucket
response = s3_client.list_objects_v2(Bucket=s3BucketName)

# Create an empty list to store the extracted text data
data = []

# Iterate over the objects in the bucket
for obj in response.get('Contents', []):
    # Get the object key
    object_key = obj.get("Key")

    if object_key:
        # Call Amazon Textract to start document analysis job for the object
        try:
            response = textract.start_document_text_detection(
                DocumentLocation={
                    'S3Object': {
                        'Bucket': s3BucketName,
                        'Name': object_key
                    }
                }
            )

            # Get the JobId for the document analysis job
            job_id = response['JobId']

            # Poll for the completion of the document analysis job
            while True:
                response = textract.get_document_text_detection(JobId=job_id)

                status = response['JobStatus']
                if status in ['SUCCEEDED', 'FAILED']:
                    break

                time.sleep(5)  # Wait for 5 seconds before polling again

            if status == 'SUCCEEDED':
                # Get the results of the document analysis job
                blocks = response['Blocks']

                # Extract text from each block
                text = ''
                for block in blocks:
                    if block['BlockType'] == 'LINE':
                        text += block['Text'] + '\n'

                # Append the file title and text to the data list
                data.append({'File Title': object_key, 'Text': text})

                print(f"Text extracted for {object_key}")
            else:
                print(f"Error processing {object_key}: Document analysis job failed")
        except Exception as e:
            print(f"Error processing {object_key}: {str(e)}")
    else:
        print("Object key is None")

# Create a DataFrame from the extracted text data
df = pd.DataFrame(data)

# Perform text cleaning using NLTK
cleaned_text = []

for text in df['Text']:
    # Tokenize the text into words by splitting on white space
    words = text.split()

    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    words = [word for word in words if word.lower() not in stopwords]

    # Perform spell checking and correction
    corrected_words = [spell.correction(word) if spell.correction(word) is not None else word for word in words]

    # Join the corrected words back into a cleaned text
    cleaned_text.append(' '.join(corrected_words))

# Check if the length of cleaned_text matches the length of the DataFrame index
if len(cleaned_text) == len(df.index):
    # Replace the 'Text' column in the DataFrame with cleaned text
    df['Text'] = cleaned_text
else:
    print("Error: Length of cleaned_text does not match the length of the DataFrame index.")

# Save the DataFrame to an Excel file
excel_file = 'extracted_text.xlsx'
df.to_excel(excel_file, index=False)
print(f"Extracted text saved to {excel_file}")

