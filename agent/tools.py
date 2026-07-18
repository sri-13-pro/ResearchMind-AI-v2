"""
tools.py
---------
Tools available to the Research Agent.
"""

from services.citation_generator import CitationGenerator
from services.comparator import PaperComparator
from services.keyword_extractor import KeywordExtractorService
from services.literature_review import LiteratureReviewGenerator
from services.pdf_processor import PDFProcessor
from services.search_manager import SearchManager
from services.summarizer import PaperSummarizer


class AgentTools:

    def __init__(self):

        self.search = SearchManager.get_search()

        self.pdf = PDFProcessor()
        self.comparator = PaperComparator()

        self.summarizer = PaperSummarizer()
        self.keyword_extractor = KeywordExtractorService()
        self.review_generator = LiteratureReviewGenerator()
        self.citation_generator = CitationGenerator()

    def extract_keywords(self, pdf_path):

        return self.keyword_extractor.extract(pdf_path)

    def search_papers(self, query, top_k=5):

        return self.search.search(query, top_k)

    def summarize_pdf(self, pdf_path):

        text = self.pdf.extract_text(pdf_path)

        return self.summarizer.summarize(text)

    def compare_papers(self, pdf1, pdf2):

        return self.comparator.compare(pdf1, pdf2)

    def literature_review(self, topic):

        return self.review_generator.generate(topic)

    def generate_citation(self, pdf_path):

        return self.citation_generator.generate(pdf_path)
