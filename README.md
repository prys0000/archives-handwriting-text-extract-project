# archives-textract

The objective of this project is to develop a text extraction and cleaning tool that utilizes the capabilities of Amazon Textract with customizable processes to adapt to repository or project specifications.  The code extracts text from documents stored in an AWS S3 bucket, performs text cleaning operations and saves the extracted and cleaned text to the existing metadata templates used by the repository. 

By automating the text extraction and cleaning processes, this project enables efficient handling of large-scale collections of documents, which can include various file formats such as PDFs, images, or other formats that contain text, whether it's handwritten or typed. 

The use of the scripts provide streamlined and scalable solutions for processing textual data, which can be valuable for applications such as data analysis, information retrieval, and natural language processing. 

## Installation

To get a local copy up and running follow these simple steps.

### Connecting Amazon Textract
 
Set the AWS access keys, S3 bucket name and AWS region. You will need to create a ['credentials.txt'](https://github.com/prys0000/archives-textract/blob/main/credentials.properties) file to control access and save in the same directory as your Python script.

* **AWS region** - AWS region where the S3 bucket and Textract service are located
aws_region = "  "  # Replace with your desired region

* **AWS access key** - user-specific alphanumeric string that identifies the AWS account or user making the API request
aws_access_key_id= "  " # Replace with AWS Access Key

* **AWS secret access key** - a secret key that is paired with the access key ID and is used to sign API requests for authentication
aws_secret_access_key= "  " # Replace with AWS Secret Access Key

* **Bucket name** - represents the name of the S3 bucket where the documents are stored
aws_S3_Bucket_Name= "  " # Replace with AWS S3 Bucket Name/path

```bash
AWS_ACCESS_KEY_ID=<your-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_REGION=<your desired region>
S3_BUCKET_NAME=<your-s3-bucket-name>
```

Load the ['credentials.txt'](https://github.com/prys0000/archives-textract/blob/main/credentials.properties) file and bucket.
```bash
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
```

Create an AWS Textract client and S3 client using the configured AWS region.
```bash
aws_region = "us-east-1"  # Replace with your desired region

textract = boto3.client('textract', region_name=aws_region)
s3_client = boto3.client('s3', region_name=aws_region)
```

You can now use the textract and s3_client objects to interact with Amazon Textract and Amazon S3 services in your code.
* Remember to replace the region and bucket name with the appropriate values for your setup.
* Remember to update the bucket access keys.
##

## Package prerequisites 

There are steps required to run the archive-textract scripts. First you must install some system packages using the apt-get package manager before installing textract from pypi.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

* **boto3** is the Amazon Web Services (AWS) SDK for Python, and it is used to interact with AWS services such as Amazon Textract and S3.

```bash
pip install boto3
```
* **nltk** is the Natural Language Toolkit library, which provides tools for natural language processing tasks such as tokenization, stemming, and stopwords removal.

```bash
pip install nltk
```
* **pandas** is a powerful data manipulation library, used here to create and manipulate data structures like DataFrames, which are used to store and analyze the extracted text data.
```bash
pip install pandas
```
* **fuzzywuzzy** is a Python library used for fuzzy string matching. It provides various functions and algorithms to compare and measure the similarity between two strings based on their similarity ratio or distance.
```bash
pip install fuzzywuzzy
```
* **pypdf2** is a Python library for working with PDF files. It allows you to extract text and metadata from PDF documents, merge or split PDF files, add watermarks, encrypt or decrypt PDFs, and more.
```bash
pip install pdfpy2
```
* **sumy** is a Python library for automatic text summarization. It provides a simple and convenient way to generate summaries from large blocks of text, such as articles, documents, or web pages. 
```bash
pip install sumy
```
* **openpyxl** is a Python library that allows you to interact with and manipulate Microsoft Excel files (XLSX/XLSM files). It provides functionality to create, read, modify, and save Excel files using Python
```bash
pip install openpyxl
```



# Extracting multi-page handwritten and typewritten text
The python script [multisync.py](https://gitlab.com/-/ide/project/cac-archives/\archives-textract\extracting\multipgexcelsynch.py)  demonstrates the usage of Amazon Textract, Amazon S3, NLTK, and the SpellChecker package to extract text from documents stored in an S3 bucket, perform text cleaning, and save the extracted and cleaned text to Excel files.

The [multisync.py](https://gitlab.com/-/ide/project/cac-archives/\archives-textract\extracting\multipgexcelsynch.py) script allows for processing various types of files:

* **EPUB (Electronic Publication):** Textract can extract text from EPUB files. EPUB is a popular file format for e-books, allowing for dynamic content and reflowable text across different devices.
* **PDF (Portable Document Format):** Textract can process PDF documents and extract text from them. PDF is a common file format used for sharing documents that preserves the formatting and layout across different devices.
* **DOC and DOCX:** Textract supports extracting text from Microsoft Word documents. DOC and DOCX are file formats used by Microsoft Word for creating and editing documents.
* **RTF (Rich Text Format):** Textract supports extracting text from RTF files. RTF is a document file format that allows for rich text formatting, including fonts, styles, and images.
* **XLS, XLSX, XLSB, XLSM, XLTX:** Textract can extract text from various Microsoft Excel file formats. These file formats are used for storing spreadsheets and tabular data.
* **CSV (Comma-Separated Values):** Textract can process CSV files and extract text from them. CSV is a plain text format used for storing tabular data, with each value separated by commas.
* **PPTX and POTX:** Textract can extract text from Microsoft PowerPoint files. PPTX and POTX are file formats used for creating and presenting slide-based presentations.
* **PNG, JPG, GIF:** Textract supports extracting text from image files in formats such as PNG, JPG, and GIF. These formats contain visual information, and Textract can process them to extract any text present within the images.
* **DXF (Drawing Exchange Format):** Textract can extract text from DXF files. DXF is a file format used for CAD (Computer-Aided Design) drawings.

### Additional cleaning options
#### Pre-processing
* **preprocess_text** function takes the extracted text as input and applies the following pre-processing steps:
  * Removal of special characters and symbols: It uses regular expressions (re.sub) to remove any non-alphanumeric characters from the text.
  * Conversion to lowercase: It converts the text to lowercase to ensure consistency and avoid case sensitivity issues.
  * Removal of extra whitespace: It uses the split and join functions to split the text into words and then rejoin them with a single space, effectively removing extra whitespace.
  * Spell checking or correction: This step is commented out in the code since it depends on the specific library or technique you choose to use for spell checking or correction. You can incorporate a spell checker library, such as pyspellchecker, to perform spell checking and correction on the extracted text.
  * Expansion of abbreviations: This step is also commented out since it depends on the technique or dictionary you use for expanding abbreviations. You can incorporate a custom dictionary or algorithm to expand abbreviations in the text if needed.
```bash
import re

def preprocess_text(text):
    # Remove special characters and symbols
    text = re.sub(r'[^\w\s]', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = ' '.join(text.split())

    # Perform spell checking or correction (using appropriate library)
    # spell_corrected_text = spell_checker.correct(text)
    # text = spell_corrected_text

    # Expand abbreviations (using appropriate technique or dictionary)
    # expanded_text = abbreviation_expander.expand(text)
    # text = expanded_text

    return text

# Example usage
extracted_text = "This is some example text with symbols, extra   whitespace, and misspellings!"
preprocessed_text = preprocess_text(extracted_text)
print(preprocessed_text)
```
* **blocktype** function performs document layout analysis for Textract in Python. These block types provide information about the layout and structure of the document such as PAGE, LINE, WORD, TABLE, and more.
```bash
# Get the extracted blocks from Textract
blocks = response['Blocks']

# Iterate over the blocks and perform layout analysis
for block in blocks:
    # Perform custom layout analysis based on block types
    if block['BlockType'] == 'PAGE':
        # Process the entire page

    elif block['BlockType'] == 'LINE':
        # Process individual lines of text

    elif block['BlockType'] == 'TABLE':
        # Process tables

    # Apply other custom layout analysis techniques as needed

# Perform additional post-processing and formatting steps

# Save the processed document or extract specific regions as needed
```
#### Post-processing
* **remove_special_characters()** function takes a text as input and applies the regular expression pattern [^a-zA-Z0-9\s] to remove any characters that are not alphanumeric or whitespace characters. 
* **re.sub()** function replaces the matched characters with an empty string.

```bash
import re

def remove_special_characters(text):
    # Define the pattern for special characters using regular expressions
    pattern = r'[^a-zA-Z0-9\s]'  # Keep alphanumeric characters and whitespaces

    # Use the sub() function from the re module to replace the special characters with an empty string
    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text
```
* **remove_whitespace()** function uses the re.sub() function to replace multiple consecutive spaces (\s+) with a single space
* **strip()** method is then called to remove any leading and trailing whitespace.
```bash
import re

def remove_whitespace(text):
    # Use regular expression to replace multiple consecutive spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', text).strip()

    return cleaned_text

text = "   Hello,    world!   "
cleaned_text = remove_whitespace(text)
print(cleaned_text)
```




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
