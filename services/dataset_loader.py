"""
dataset_loader.py
-----------------
Loads and validates the research paper dataset.
"""

from pathlib import Path

import pandas as pd


class DatasetLoader:

    REQUIRED_COLUMNS = ["title", "abstract"]

    def __init__(self, dataset_path):

        self.dataset_path = Path(dataset_path)

    def exists(self):

        return self.dataset_path.exists()

    def load(self):

        if not self.exists():
            raise FileNotFoundError(f"Dataset not found:\n{self.dataset_path}")

        df = pd.read_csv(self.dataset_path)

        return df

    def validate(self, df):

        missing = []

        for column in self.REQUIRED_COLUMNS:

            if column not in df.columns:
                missing.append(column)

        if missing:
            raise ValueError(f"Missing columns: {missing}")

        return True

    def clean(self, df):

        df = df.dropna(subset=["title", "abstract"])

        df = df.drop_duplicates(subset=["title"])

        df = df.reset_index(drop=True)

        return df

    def get_dataset(self):

        df = self.load()

        self.validate(df)

        df = self.clean(df)

        print(f"Loaded {len(df)} research papers.")

        return df
