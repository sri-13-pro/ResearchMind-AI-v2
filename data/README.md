# Data Directory

The `data` directory stores datasets and vector indexes used by ResearchMind-AI.

## Structure

raw/

Original datasets.

processed/

Cleaned datasets used during semantic search.

vector_db/

FAISS vector indexes generated from processed datasets.

## Workflow

Raw Dataset

↓

Preprocessing

↓

Sentence Embeddings

↓

FAISS Index

↓

Semantic Search

## Notes

Large datasets and generated vector indexes are generally excluded from Git version control.
