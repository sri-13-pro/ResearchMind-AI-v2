"""
embedding_service.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL, PROCESSED_DATASET, VECTOR_DB


class EmbeddingService:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        VECTOR_DB.mkdir(parents=True, exist_ok=True)

    def generate(self):

        df = pd.read_csv(PROCESSED_DATASET)

        texts = (df["title"] + ". " + df["abstract"]).tolist()

        print(f"Generating embeddings for {len(texts)} papers...")

        embeddings = self.model.encode(
            texts,
            batch_size=16,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        np.save(VECTOR_DB / "embeddings.npy", embeddings)

        print("\nEmbeddings Saved!")

        return embeddings
