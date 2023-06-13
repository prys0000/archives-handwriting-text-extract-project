import boto3
import re
import nltk
from spellchecker import SpellChecker
import time
import pandas as pd
import subprocess

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
            response = textract.start_document_analysis(
                DocumentLocation={
                    'S3Object': {
                        'Bucket': s3BucketName,
                        'Name': object_key
                    }
                },
                FeatureTypes=['TABLES', 'FORMS']
            )

            # Get the JobId for the document analysis job
            job_id = response['JobId']

            # Poll for the completion of the document analysis job
            while True:
                response = textract.get_document_analysis(JobId=job_id)

                status = response['JobStatus']
                if status in ['SUCCEEDED', 'FAILED']:
                    break

                time.sleep(5)  # Wait for 5 seconds before polling again

            if status == 'SUCCEEDED':
                # Get the results of the document analysis job
                blocks = response['Blocks']

                # Create a text document name based on the object key
                text_document_name = re.sub(r"[^a-zA-Z0-9-_. ]+", "", str(object_key)) + ".txt"

                # Open the text document in read mode
                with open(text_document_name, 'r') as file:
                    # Read the text from the file
                    text = file.read()

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
subprocess.run(['C:\Program Files\RapidMiner\rapidminer-studio.bat', '-f', 'text_cleaning.rmp', '-P', f'input_excel_file={excel_file}', '-P', f'output_excel_file={cleaned_excel_file}'])

print(f"Text cleaned and saved to {cleaned_excel_file}")
