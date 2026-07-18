"""
preprocessor.py
---------------
Cleans and preprocesses research papers.
"""

import re

import pandas as pd


class ResearchPreprocessor:

    def __init__(self):
        pass

    def clean_text(self, text):

        if pd.isna(text):
            return ""

        text = str(text)

        # Remove newlines
        text = text.replace("\n", " ")

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text)

        # Remove URLs
        text = re.sub(r"http\S+", "", text)

        # Remove special characters (keep punctuation)
        text = re.sub(r"[^a-zA-Z0-9.,!?()\- ]", "", text)

        return text.strip()

    def preprocess(self, df):

        df = df.copy()

        df["title"] = df["title"].apply(self.clean_text)
        df["abstract"] = df["abstract"].apply(self.clean_text)

        return df
