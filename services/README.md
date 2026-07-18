# Services Module

The `services` package contains all business logic used throughout ResearchMind-AI.

Each service performs one independent task, making the application modular and easy to maintain.

## Available Services

### semantic_search.py

Performs semantic similarity search using Sentence Transformers and FAISS.

### search_manager.py

Provides a singleton interface for the semantic search engine.

### pdf_processor.py

Extracts clean text from PDF research papers.

### summarizer.py

Generates structured summaries using the Groq LLM.

### comparator.py

Compares two research papers and identifies similarities and differences.

### keyword_extractor.py

Extracts important keywords using YAKE.

### literature_review.py

Generates literature reviews from multiple research papers.

### citation_generator.py

Creates academic citations in APA, IEEE, MLA, and BibTeX formats.

### history_manager.py

Stores conversation history locally.

### export_manager.py

Exports generated outputs to Markdown and Text files.

## Design Principles

- Single Responsibility Principle
- Modular Architecture
- Independent Components
- Easy Testing
- Easy Extension
