"""
keyword_extractor.py
--------------------
Extract keywords from research papers.
"""

from yake import KeywordExtractor

from services.pdf_processor import PDFProcessor


class KeywordExtractorService:

    def __init__(self):

        self.pdf = PDFProcessor()

        self.extractor = KeywordExtractor(lan="en", n=2, top=15)

    def extract(self, pdf_path):

        text = self.pdf.extract_text(pdf_path)

        keywords = self.extractor.extract_keywords(text)

        return [keyword for keyword, score in keywords]
