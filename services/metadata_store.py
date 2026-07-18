"""
metadata_store.py
-----------------
Stores metadata for each text chunk.
"""

import json
from pathlib import Path


class MetadataStore:

    def __init__(self):

        self.file = Path("data/vector_db/metadata.json")

        self.file.parent.mkdir(parents=True, exist_ok=True)

        if self.file.exists():

            with open(self.file, "r", encoding="utf-8") as f:

                self.metadata = json.load(f)

        else:

            self.metadata = []

    def add(self, metadata: dict):

        self.metadata.append(metadata)

    def save(self):

        with open(self.file, "w", encoding="utf-8") as f:

            json.dump(self.metadata, f, indent=4, ensure_ascii=False)

    def get(self, index: int):

        return self.metadata[index]

    def size(self):

        return len(self.metadata)
