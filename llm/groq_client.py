"""
groq_client.py
--------------
Handles communication with the Groq API.
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqClient:

    def __init__(self):

        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        self.model = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

    def generate(self, prompt: str):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        return response.choices[0].message.content

    def answer_question(self, question: str, context: str):

        prompt = f"""
You are an AI Research Assistant.

Use ONLY the research context below to answer the question.

If the answer is not present, clearly state that.

Research Context

{context}

Question

{question}

Answer:
"""

        return self.generate(prompt)
