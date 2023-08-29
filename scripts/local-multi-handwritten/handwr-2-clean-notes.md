## Script Overview:
The provided Python script extracts text from multi-page PDF files, corrects grammar and spelling using LanguageTool, removes non-alphanumeric characters, and saves the cleaned text to an Excel file.

**Prerequisites:**

1. Python must be installed on your system.
2. Install required packages using pip:
```bash
pip install pdf2image pytesseract language_tool_python pandas
```

**Script Breakdown:**

**1. Import Required Libraries:**

   * The necessary libraries are imported, including os for file operations, [pdf2image](https://pypi.org/project/pdf2image/) for PDF to image conversion, [pytesseract](https://pypi.org/project/pytesseract/) for OCR, [LanguageTool](https://github.com/languagetool-org/languagetool) for grammar and spelling correction, and [re](https://docs.python.org/3/library/re.html) for regular expressions.

**2. Specify PDF Folder and Output Excel File:**

   * pdf_folder should be set to the folder containing your PDF files.
output_excel should be set to the desired name of the output Excel file.

**3. Initialize Empty Data List and LanguageTool:**

   * An empty list named data is created to store extracted text and file names.
   * LanguageTool is initialized with the 'en-US' language for grammar and spelling correction.

**4. Iterate Over PDF Files:**

   * The script iterates through files in the specified pdf_folder.
   * Only files with '.pdf' extensions are processed.

**5. PDF to Image Conversion and OCR:**

   * Each PDF file is converted to images using pdf2image.
   * Each image is processed using pytesseract for OCR, and the extracted text is accumulated with newline separators.

**6. Grammar and Spelling Correction:**

   * The accumulated text is corrected using LanguageTool.
   * Grammar and spelling errors are identified and corrected.

**7. Punctuation Removal:**

   * Using re.sub(), non-alphanumeric characters (except spaces) are removed from the corrected text.
   * This helps to eliminate punctuation and special characters that might affect analysis and readability.

**8. Append Data to List:**

   * The cleaned text and file name are appended to the data list.

**9. Create and Save DataFrame:**

   * A Pandas DataFrame is created using the data list.
   * The DataFrame is saved to an Excel file named output_excel.

**10. Execution and Output:**

   * Run the script.
   * The script processes PDF files, performs OCR, grammar and spelling corrections, and removes punctuation.
   * Extracted, cleaned text is saved to the specified Excel file.

**Usage:**

1. Place your PDF files in the pdf_folder.
2. Set the output_excel to the desired Excel file name.
3. Run the script using Python.

**Output:**

The script generates an Excel file containing cleaned text extracted from the PDF files. Each row corresponds to a PDF file, with columns for the file name and cleaned text.

**Note:**

* While the script aims to improve text quality, manual review is still recommended for accuracy.
* OCR quality may vary based on PDF content and handwriting.
* Adjustments to the script may be required for specific use cases.

#

**Script-Handwritten-Text-Extraction**

```python
import os
import pandas as pd
from pdf2image import convert_from_path
import pytesseract
from language_tool_python import LanguageTool
import re

# Path to the folder containing the PDF files
pdf_folder = r'C:\Users\user\Desktop\TEXTRACT TEST FOLDER\V8_2023_08_29\pdf'

# Output Excel file name
output_excel = 'extracted_text.xlsx'

# Create an empty list to store the extracted text data
data = []

# Initialize LanguageTool for grammar and spelling correction
tool = LanguageTool('en-US')

# Iterate over PDF files in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        # Construct full path to the PDF file
        pdf_path = os.path.join(pdf_folder, filename)

        # Convert PDF to images using pdf2image
        images = convert_from_path(pdf_path)

        pdf_text = ''  # Initialize text for the current PDF
        for image in images:
            # Perform OCR using pytesseract
            page_text = pytesseract.image_to_string(image)
            pdf_text += page_text + '\n'  # Add a newline between pages

        # Clean up text using LanguageTool for grammar and spelling correction
        corrected_text = tool.correct(pdf_text)

        # Remove non-alphanumeric characters (except spaces)
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', corrected_text)

        # Append the extracted text and file name to the data list
        data.append({'File Name': filename, 'Text': cleaned_text})

# Create a DataFrame from the extracted text data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(output_excel, index=False)
print(f"Extracted text saved to {output_excel}")
```
