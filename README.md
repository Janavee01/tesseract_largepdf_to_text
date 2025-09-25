# PDF Text Extractor using Tesseract OCR

## Overview
This is a Python-based tool designed for extracting text from large PDF files using OCR. It leverages the Tesseract OCR engine to process PDF pages as images and extract the embedded text. The tool is built to handle multi-page PDFs, processing each page individually to ensure robustness and provide detailed progress information.

## Features
- **Text Extraction from PDFs:** Converts pages of a PDF file into images and then uses Tesseract to extract text from these images.
- **Handles Large Files:** Designed to process large, multi-page PDF documents efficiently.
- **Page-by-Page Processing:** Processes the PDF one page at a time, which is memory-efficient and allows for graceful error handling.
- **Robust Error Handling:** Includes error handling to skip pages that fail to process, ensuring the extraction process completes for the rest of the document.
- **Customizable DPI:** Allows for adjusting the DPI (dots per inch) for image conversion to balance quality and performance.

## Tech Stack
The project is built with Python and utilizes the following libraries:
- `pytesseract` – A Python wrapper for Google's Tesseract-OCR Engine.
- `pdf2image` – A library to convert PDF to a PIL Image object.
- `Pillow` (PIL Fork) – An imaging library for Python.
- `PyPDF2` – A library for reading and manipulating PDF files.

All dependencies are listed in the `requirements.txt` file.

## Setup and Usage

### Prerequisites
- Python 3.x
- Tesseract OCR engine installed and accessible in your system's PATH.

### Installation
Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
Install the required Python packages:

pip install -r requirements.txt
Running the Script
Place the PDF file you want to process in the project directory and name it CAO.pdf (or modify the pdf_path in main.py).

Run the main script from the terminal:
python main.py
The script will process the PDF page by page, and the extracted text will be saved to cao_output_text.txt by default.
```
The output is a single text file containing the extracted text from the PDF. Each page's text is separated by a header indicating the page number.
