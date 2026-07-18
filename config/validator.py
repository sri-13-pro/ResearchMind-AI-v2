"""
validator.py
-------------
Application startup validation.
"""

import os
from pathlib import Path

from config.settings import PROCESSED_DATASET, VECTOR_DB


class StartupValidator:

    def validate(self):

        print("=" * 60)
        print("Checking Application...")
        print("=" * 60)

        # -------------------------------
        # API KEY
        # -------------------------------

        if os.getenv("GROQ_API_KEY"):

            print("✓ GROQ API Key Found")

        else:

            print("✗ GROQ API Key Missing")

        # -------------------------------
        # DATASET
        # -------------------------------

        if Path(PROCESSED_DATASET).exists():

            print("✓ Dataset Found")

        else:

            print("✗ Dataset Missing")

        # -------------------------------
        # VECTOR DATABASE
        # -------------------------------

        index_file = VECTOR_DB / "research.index"

        if index_file.exists():

            print("✓ FAISS Index Found")

        else:

            print("✗ FAISS Index Missing")

        print("=" * 60)
