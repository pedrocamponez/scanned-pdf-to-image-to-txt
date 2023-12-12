# Setup

In order for everything to work, you have to clone this repository and use either your machine or a localhost development platform - like Docker.
In order to use pdf2image, you have to install popper. You can get the Windows downloader here (make sure to insert it into the Windows PATH): https://github.com/oschwartz10612/poppler-windows/releases or you can go to the official website and install it for Linux/MacOS.
Then you should use 'pip install easyocr pandas pdf2image shutil' and you're good to go.

# Classes

## DataChecker

The DataChecker class is responsible for checking the current txt files (running through the folder) with the excel sheet rows.
You can insert the rows and columns that you want to check in the check_data() method. 
It uses pandas, shutil and os.

## PDFConverter

The PDFConverter class is responsible for converting the Scanned PDF file into an image (.png) so we can extract the text.
It uses pdf2image and os.

## TextExtractor

The TextExtractor class is responsible for extracting the text from the images that came from the PDF files.
It uses easyocr and os.
