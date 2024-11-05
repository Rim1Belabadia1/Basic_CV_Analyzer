# cv_reader.py

from PyPDF2 import PdfReader

def read_cv(cv_file):
    with open(cv_file, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text
