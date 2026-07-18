"""
pdf_processor.py
----------------
Extracts text from PDF files.
"""

import fitz  # PyMuPDF


class PDFProcessor:

    def extract_text(self, pdf_path: str) -> str:

        document = fitz.open(pdf_path)

        text = ""

        for page in document:

            text += page.get_text()

            text += "\n"

        document.close()

        return text
