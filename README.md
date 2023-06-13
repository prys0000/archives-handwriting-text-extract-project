<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Carl Albert Center Archives][logo]][https://www.ou.edu/content/carlalbertcenter/_jcr_content/relatedpar/textimage/image.img.png/1649863950405.png]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/prys0000/archives-textract">
    <img src="SIG.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">archives-textract</h3>

  <p align="center">
    The objective of this project is to develop a text extraction and cleaning tool that utilizes the capabilities of Amazon Textract and RapidMiner. The code extracts text from documents stored in an AWS S3 bucket, performs text cleaning operations using RapidMiner, and saves the extracted and cleaned text to Excel files. By automating the text extraction and cleaning processes, this project enables efficient handling of large-scale collections of documents. The use of Amazon Textract and RapidMiner allows for reliable and accurate extraction and cleaning of text from various document formats. The resulting system provides a streamlined and scalable solution for processing textual data, which can be valuable for applications such as data analysis, information retrieval, and natural language processing. By leveraging Amazon Textract for extraction and RapidMiner for cleaning, it provides a comprehensive solution for processing textual data. The extracted and cleaned text can be further utilized for various applications, such as data analysis, natural language processing, and information retrieval.
    <br />
    <a href="https://github.com/prys0000/archives-textract"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/prys0000/archives-textract/issues">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/prys0000/archives-textract/blob/main/githubja.png)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `prys0000`, `archives-textract`, `@CarlAlbertCtr`, 'japryse@ou.edu', `archives-textract`, `The objective of this project is to develop a text extraction and cleaning tool that utilizes the capabilities of Amazon Textract and RapidMiner. The code extracts text from documents stored in an AWS S3 bucket, performs text cleaning operations using RapidMiner, and saves the extracted and cleaned text to Excel files. By automating the text extraction and cleaning processes, this project enables efficient handling of large-scale collections of documents. The use of Amazon Textract and RapidMiner allows for reliable and accurate extraction and cleaning of text from various document formats. The resulting system provides a streamlined and scalable solution for processing textual data, which can be valuable for applications such as data analysis, information retrieval, and natural language processing. By leveraging Amazon Textract for extraction and RapidMiner for cleaning, it provides a comprehensive solution for processing textual data. The extracted and cleaned text can be further utilized for various applications, such as data analysis, natural language processing, and information retrieval.`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.py]][https://www.python.org/]
* [![Get][Get.git]][https://git-scm.com/]
* [![Rapidminer][Rapidminer.js]][https://docs.rapidminer.com/9.9/studio/installation]
* [![Textract][Textract.io]][https://aws.amazon.com/textract/]
* [![Levenshtein][Levenshtein.dev]][https://maxbachmann.github.io/Levenshtein/]
* [![Wit][Wit.ai]][Wit.ai]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![openpyxl[openpyxl.py]][https://openpyxl.readthedocs.io/en/stable/]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

There are steps required to run the archive-textract scripts. First you must install some system packages using the apt-get package manager before installing textract from pypi.
* apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev
pip install textract

### Amazon AWS Cloudshell 

1. Create a session using your AWS credentials 
session = boto3.Session(
    aws_access_key_id='ACCESS KEY',
    aws_secret_access_key='SECRET ACCESS KEY',
    region_name='REGION'
	
2. If you're unable to install boto3 directly in AWS CloudShell, you can try using a virtual environment to install and run the package. Here's a step-by-step guide:

	*Open AWS CloudShell in your AWS Management Console.
	Create a virtual environment using the following command:

	Copy code
	python3 -m venv myenv
	Activate the virtual environment:

	bash
	Copy code
	source myenv/bin/activate
	Install boto3 using the pip command:

	Copy code
	pip install boto3
	Once boto3 is installed, you can write and execute your code in the CloudShell terminal.
	
	* Note: Virtual environments in CloudShell are ephemeral and will be discarded when you close the session. You'll need to repeat these steps each time you start a new CloudShell session.
	* If you're still experiencing issues installing boto3 in AWS CloudShell, it's recommended to reach out to AWS Support for further assistance. Handtext_comb_V4 seems to be OK but needs some post-processing improvements
   ```

3. Once AWS is connected you will install a few basic packages:

	* Open AWS CloudShell in your AWS Management Console.
	PyPDF2: This package is used for extracting text from PDF files.
	You can install it using the command: pip install PyPDF2.

	sumy: This package is used for text summarization.
	You can install it using the command: pip install sumy.

	openpyxl: This package is used for working with Excel files (.xlsx)
	You can install it using the command: pip install openpyxl

	rake-nltk: This package is used for keyword extraction algorithm which tries to determine key phrases in a body of text by analyzing the frequency of word appearance and its co-occurrence with other words in the text

	pyspellchecker: This package is is designed to be easy to use to get basic spell checking.
	
	levenshtein: Levenshtein Python C extension module contains functions for fast computation of: Levenshtein (edit) distance, and edit operations, string similarity, approximate median strings, and generally string averaging
	You can install it using the command: pip install levenshtein

	* Once you have installed these packages make sure to provide the correct folder paths for the PDF files and the summary text files before executing the script.
	```
	
	
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


The archives-textract project has combined powerful Amazon AWS Textract services with  automates the extraction of text and data from scanned documents. It goes beyond traditionalOCR by not only recognizing printed text but also identifying and extracting information from historical handwritten documents, enabling efficient digitization and preservation of valuable records.  Textract can be leveraged for indexing documents, creating subject or topic classifications based on the extracted handwritten text, allowing for efficient organization and retrieval of information from large document collections.

Using Python, we have created a workflow that automatically retrieves documents from a designated source, passes them through the Textract service for text extraction (including handwritten text), and stores the extracted information in an organized manner allowing for migration, long-term data preservation, and access to large data stores for collection analysis. Scripting enables the integration of additional functionalities such as sentiment analysis, indexing, and topic creation. This automation significantly reduces the manual efforts required for archival processing, saving time and increasing efficiency.

When extracting handwritten text, it's important to note that the accuracy and reliability of extracting handwritten text can vary depending on the legibility of the handwriting itself. Handwritten text presents a unique challenge due to variations in handwriting styles, quality, and clarity.

In cases where the handwritten text is not clearly written or is difficult to interpret, the accuracy of the extracted text may be compromised. Textract relies on machine learning algorithms to analyze and recognize text, but it may struggle with handwritten text that is messy, overlapping, or illegible.

Several packages have been used to increase readability including Levenshtein which has proven to create the most reliable reults:

The accuracy algorithm used is based on the fuzzywuzzy library, which implements the Levenshtein distance algorithm for fuzzy string matching. The specific algorithm used is the token sort ratio.

The token sort ratio is a variation of the standard Levenshtein distance algorithm that takes into account the order of the words in the compared strings. It first tokenizes the strings into individual words, sorts them alphabetically, and then compares the sorted tokens. This approach is useful when comparing text that may have different word order but still represent the same information.

The resulting similarity score from the token sort ratio algorithm represents the percentage of similarity between the two strings. A score of 100 indicates an exact match, while lower scores indicate a decreasing level of similarity.

In the provided code, a similarity threshold is set to 70. This means that only text pairs with a similarity score equal to or above 70 will be considered as a match. Any pairs below this threshold will have an accuracy of 0.

You can adjust the similarity threshold value according to your specific needs and the level of strictness you want for considering a match. Higher values will require a closer match, while lower values will allow for more leniency.

It's important to note that while the token sort ratio algorithm can provide a good indication of similarity, it may not always capture the full context or meaning of the text. You may need to consider additional techniques or algorithms depending on the specific requirements of your application.


_For more examples, please refer to the [LINK DOC](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed by the Carl Albert Congressional Center Archives. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

JA Pryse - [@CarlAlbertCtr](https://twitter.com/@CarlAlbertCtr) - japryse@ou.edu

Project Link: [https://github.com/prys0000/archives-textract](https://github.com/prys0000/archives-textract)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>




