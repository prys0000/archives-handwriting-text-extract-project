import boto3
import re
import nltk
from spellchecker import SpellChecker
import time
import pandas as pd
from openpyxl import Workbook
import subprocess

# Read AWS credentials and S3 bucket name from credentials.txt file
with open('credentials.txt', 'r') as file:
    credentials = file.readlines()

aws_access_key_id = None
aws_secret_access_key = None
s3_bucket_name = None

for line in credentials:
    if line.startswith('AWS_ACCESS_KEY_ID='):
        aws_access_key_id = line.split('=')[1].strip()
    elif line.startswith('AWS_SECRET_ACCESS_KEY='):
        aws_secret_access_key = line.split('=')[1].strip()
    elif line.startswith('S3_BUCKET_NAME='):
        s3_bucket_name = line.split('=')[1].strip()

if aws_access_key_id is None or aws_secret_access_key is None or s3_bucket_name is None:
    raise ValueError("Invalid credentials in credentials.txt file")

# AWS region
aws_region = "us-east-1"  # Replace with your desired region

# Amazon Textract client
textract = boto3.client('textract', region_name=aws_region)

# Create an S3 client
s3_client = boto3.client('s3', region_name=aws_region)

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Initialize SpellChecker
spell = SpellChecker()

# Retrieve the list of objects in the S3 bucket
response = s3_client.list_objects_v2(Bucket=s3_bucket_name)

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
                        'Bucket': s3_bucket_name,
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

# Save the DataFrame to an Excel file
excel_file = 'extracted_text.xlsx'
df.to_excel(excel_file, index=False)
print(f"Extracted text saved to {excel_file}")

# Call RapidMiner to perform text cleaning
cleaned_excel_file = 'cleaned_text.xlsx'
rapidminer_path = r'C:\Program Files\RapidMiner\rapidminer-studio.bat'
text_cleaning_rmp = 'text_cleaning.rmp'

subprocess.run([rapidminer_path, '-f', text_cleaning_rmp, '-P', f'input_excel_file={excel_file}', '-P', f'output_excel_file={cleaned_excel_file}'])

print(f"Text cleaned and saved to {cleaned_excel_file}")
