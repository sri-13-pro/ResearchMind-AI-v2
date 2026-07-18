"""
bm25_search.py
--------------
Keyword-based search using BM25.
"""

from rank_bm25 import BM25Okapi


class BM25Search:

    def __init__(self, documents):

        self.documents = documents

        self.tokenized_docs = [doc.lower().split() for doc in documents]

        self.bm25 = BM25Okapi(self.tokenized_docs)

    def search(self, query, top_k=5):

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

        return ranked[:top_k]
