import os
import pandas as pd
from pdf2image import convert_from_path
import pytesseract
from language_tool_python import LanguageTool

# Path to the folder containing the PDF files
pdf_folder = r'C:\Users\user\Desktop\TEXTRACT TEST FOLDER\V8_2023_08_29\pdf'

# Output Excel file name
output_excel = 'extracted_text.xlsx'

# Create an empty list to store the extracted text data
data = []

# Initialize LanguageTool
tool = LanguageTool('en-US')

# Iterate over PDF files in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, filename)

        # Convert PDF to images using pdf2image
        images = convert_from_path(pdf_path)

        pdf_text = ''
        for image in images:
            # Perform OCR using pytesseract
            page_text = pytesseract.image_to_string(image)
            pdf_text += page_text + '\n'  # Add a newline between pages

        # Clean up text using LanguageTool
        corrected_text = tool.correct(pdf_text)

        # Append the extracted text and file name to the data list
        data.append({'File Name': filename, 'Text': corrected_text})

# Create a DataFrame from the extracted text data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(output_excel, index=False)
print(f"Extracted text saved to {output_excel}")
