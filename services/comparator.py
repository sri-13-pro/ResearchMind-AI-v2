"""
comparator.py
--------------
Compare two research papers.
"""

from llm.groq_client import GroqClient
from services.pdf_processor import PDFProcessor
from services.summarizer import PaperSummarizer


class PaperComparator:

    def __init__(self):

        self.pdf = PDFProcessor()

        self.summarizer = PaperSummarizer()

        self.llm = GroqClient()

    def compare(self, pdf1, pdf2):

        text1 = self.pdf.extract_text(pdf1)

        text2 = self.pdf.extract_text(pdf2)

        summary1 = self.summarizer.summarize(text1)

        summary2 = self.summarizer.summarize(text2)

        prompt = f"""
You are an AI Research Assistant.

Compare the following two research papers.

Paper 1 Summary

{summary1}

-----------------------------------

Paper 2 Summary

{summary2}

-----------------------------------

Compare them using this format:

1. Research Objective

2. Methodology

3. Dataset

4. Strengths

5. Weaknesses

6. Results

7. Future Work

8. Overall Comparison

Return the answer in markdown.
"""

        return self.llm.generate(prompt)
