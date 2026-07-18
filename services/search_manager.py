"""
search_manager.py
-----------------
Singleton manager for SemanticSearch.
"""

from services.semantic_search import SemanticSearch


class SearchManager:

    _instance = None

    @classmethod
    def get_search(cls):

        if cls._instance is None:

            cls._instance = SemanticSearch()

        return cls._instance
