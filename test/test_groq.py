from llm.groq_client import GroqClient
from services.semantic_search import SemanticSearch

search = SearchManager.get_search()

llm = GroqClient()

question = "What is Retrieval-Augmented Generation?"

results = search.search(question)

context = ""

for paper in results:

    context += f"""
Title:
{paper['title']}

Abstract:
{paper['abstract']}

"""

answer = llm.generate(question, context)

print()

print("=" * 80)

print(answer)
