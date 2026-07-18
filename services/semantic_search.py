"""
semantic_search.py
------------------
Performs semantic search using FAISS.
"""

import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

from config.settings import (EMBEDDING_MODEL, PROCESSED_DATASET, TOP_K,
                             VECTOR_DB)


class SemanticSearch:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print("Loading FAISS index...")

        self.index = faiss.read_index(str(VECTOR_DB / "research.index"))

        self.df = pd.read_csv(PROCESSED_DATASET)

    def search(self, query, top_k=TOP_K):

        query_embedding = self.model.encode([query], normalize_embeddings=True)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):

            paper = self.df.iloc[idx]

            results.append(
                {
                    "score": float(score),
                    "title": paper["title"],
                    "abstract": paper["abstract"],
                    "authors": paper.get("authors", ""),
                    "published": paper.get("published", ""),
                    "categories": paper.get("categories", ""),
                }
            )

        return results
