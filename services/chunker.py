"""
chunker.py
-----------
Splits long text into overlapping chunks.
"""

from typing import List


class TextChunker:

    def __init__(self, chunk_size: int = 500, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:

        if not text:
            return []

        words = text.split()

        chunks = []

        start = 0

        while start < len(words):

            end = start + self.chunk_size

            chunk = " ".join(words[start:end])

            chunks.append(chunk)

            if end >= len(words):
                break

            start += self.chunk_size - self.overlap

        return chunks
