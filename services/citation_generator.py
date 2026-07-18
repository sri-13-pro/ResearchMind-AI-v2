"""
citation_generator.py
---------------------
Generate citations from research papers.
"""

import re

from llm.groq_client import GroqClient
from services.pdf_processor import PDFProcessor


class CitationGenerator:

    def __init__(self):

        self.pdf = PDFProcessor()

        self.llm = GroqClient()

    def generate(self, pdf_path):

        text = self.pdf.extract_text(pdf_path)

        # Use only the beginning of the paper
        text = text[:5000]

        prompt = f"""
You are an academic citation assistant.

Below is the beginning of a research paper.

{text}

Identify the paper metadata if available.

Generate citations in the following formats:

1. APA
2. IEEE
3. MLA
4. BibTeX

If any field is missing, use 'Unknown'.

Return the answer in Markdown.
"""

        return self.llm.generate(prompt)
