from pathlib import Path

# Dataset
RAW_DATASET = Path("data/raw/research_papers.csv")


# Processed dataset
PROCESSED_DATASET = Path("data/processed/research_papers.csv")

# Vector DB
VECTOR_DB = Path("data/vector_db")

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Search
TOP_K = 5
