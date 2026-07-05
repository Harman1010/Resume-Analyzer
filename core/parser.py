from typing import BinaryIO
import pdfplumber


def read_pdf(file: BinaryIO) -> str:
    """
    Extract text from a PDF file.
    """

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text