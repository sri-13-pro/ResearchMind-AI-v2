"""
vector_store.py
---------------
Builds and loads the FAISS vector database.
"""

from pathlib import Path

import faiss
import numpy as np

from config.settings import VECTOR_DB


class VectorStore:

    def __init__(self):

        VECTOR_DB.mkdir(parents=True, exist_ok=True)

        self.embedding_file = VECTOR_DB / "embeddings.npy"
        self.index_file = VECTOR_DB / "research.index"

    def build(self):

        print("Loading embeddings...")

        embeddings = np.load(self.embedding_file)

        dimension = embeddings.shape[1]

        print(f"Embedding Dimension : {dimension}")

        index = faiss.IndexFlatIP(dimension)

        index.add(embeddings)

        faiss.write_index(index, str(self.index_file))

        print("\nFAISS Index Created!")

        print(self.index_file)

    def load(self):

        if not self.index_file.exists():

            raise FileNotFoundError("FAISS index not found.")

        return faiss.read_index(str(self.index_file))
