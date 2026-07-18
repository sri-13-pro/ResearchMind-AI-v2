from services.semantic_search import SemanticSearch

search = SearchManager.get_search()

results = search.search("Explain Retrieval-Augmented Generation")

for i, paper in enumerate(results, 1):
    print("=" * 80)
    print(f"Paper {i}")
    print("Score:", paper["score"])
    print("Title:", paper["title"])
    print()
