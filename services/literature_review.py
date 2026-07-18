"""
literature_review.py
--------------------
Generate literature reviews from research papers.
"""

from llm.groq_client import GroqClient
from services.search_manager import SearchManager


class LiteratureReviewGenerator:

    def __init__(self):

        self.search = SearchManager.get_search()

        self.llm = GroqClient()

    def generate(self, topic):

        papers = self.search.search(topic, top_k=5)

        if not papers:
            return "No relevant papers found."

        context = ""

        for i, paper in enumerate(papers, start=1):

            context += f"""
Paper {i}

Title:
{paper['title']}

Authors:
{paper['authors']}

Published:
{paper['published']}

Abstract:
{paper['abstract']}

----------------------------------------
"""

        prompt = f"""
You are an AI Research Assistant.

Generate a professional literature review on:

{topic}

using ONLY the research papers below.

Research Papers

{context}

The review should contain:

1. Introduction
2. Current Research
3. Common Methodologies
4. Research Gaps
5. Future Directions
6. Conclusion

Return the answer in markdown.
"""

        return self.llm.generate(prompt)
