"""
summarizer.py
--------------
Research paper summarization using Groq.
"""

from llm.groq_client import GroqClient


class PaperSummarizer:

    def __init__(self):
        self.client = GroqClient()

    def summarize(self, text: str):

        prompt = f"""
You are an expert research assistant.

Summarize the following research paper.

Return:

1. Title
2. Abstract Summary
3. Key Contributions
4. Methodology
5. Results
6. Limitations
7. Future Work

Paper

{text[:12000]}
"""

        return self.client.generate(prompt)
