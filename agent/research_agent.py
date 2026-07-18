"""
research_agent.py
-----------------
Main AI Research Agent
"""

from pathlib import Path

from agent.memory import ConversationMemory
from agent.router import CommandRouter
from agent.tools import AgentTools
from llm.groq_client import GroqClient
from services.export_manager import ExportManager
from services.history_manager import HistoryManager


class ResearchAgent:

    def __init__(self):

        self.router = CommandRouter()
        self.tools = AgentTools()

        self.memory = ConversationMemory()
        self.history = HistoryManager()

        self.llm = GroqClient()

        self.export_manager = ExportManager()

        self.last_output = ""
        self.last_type = ""

    # ---------------------------------------------------
    # Export Last Output
    # ---------------------------------------------------

    def export_last_output(self):

        if not self.last_output:

            return "Nothing to export."

        path = self.export_manager.export(self.last_type, self.last_output)

        return f"Exported successfully.\n\nSaved to:\n{path}"

    # ---------------------------------------------------
    # Build Search Context
    # ---------------------------------------------------

    def _build_context(self, papers):

        context = ""

        for paper in papers:

            context += f"""
Title:
{paper.get("title", "Unknown")}

Authors:
{paper.get("authors", "Unknown")}

Published:
{paper.get("published", "Unknown")}

Categories:
{paper.get("categories", "Unknown")}

Similarity Score:
{paper.get("score", 0):.4f}

Abstract:
{paper.get("abstract", "")}

------------------------------------------------------------
"""

        return context

    # ---------------------------------------------------
    # Main Entry
    # ---------------------------------------------------

    def ask(self, question: str):

        action, data = self.router.route(question)

        # =================================================
        # HELP
        # =================================================

        if action == "help":

            return """
==============================
ResearchMind-AI Commands
==============================

search <topic>
    Search research papers

summarize <pdf_file>
    Summarize a PDF

compare <paper1.pdf> <paper2.pdf>
    Compare two papers

keywords <pdf_file>
    Extract keywords

review <topic>
    Generate literature review

cite <pdf_file>
    Generate citation

clear
    Clear conversation memory

help
    Show this menu

history
    Show conversation history

export last
    Export previous output

version
    Show application version
"""

        # =================================================
        # CLEAR MEMORY
        # =================================================

        elif action == "clear":

            self.memory.clear()

            return "Conversation memory cleared."

        # =================================================
        # SUMMARIZE PDF
        # =================================================

        elif action == "summarize":

            if data is None:

                return "Usage:\n\nsummarize sample.pdf"

            pdf_path = Path(data)

            if not pdf_path.exists():

                return f"File not found:\n{pdf_path}"

            summary = self.tools.summarize_pdf(str(pdf_path))

            self.last_output = summary
            self.last_type = "summary"

            return summary

        # =================================================
        # COMPARE
        # =================================================

        elif action == "compare":

            if data is None:

                return "Usage:\n\n" "compare paper1.pdf paper2.pdf"

            pdf1, pdf2 = data

            if not Path(pdf1).exists():

                return f"File not found:\n{pdf1}"

            if not Path(pdf2).exists():

                return f"File not found:\n{pdf2}"

            comparison = self.tools.compare_papers(pdf1, pdf2)

            self.last_output = comparison
            self.last_type = "compare"

            return comparison

        # =================================================
        # KEYWORDS
        # =================================================

        elif action == "keywords":

            if data is None:

                return "Usage:\n\nkeywords sample.pdf"

            pdf_path = Path(data)

            if not pdf_path.exists():

                return f"File not found:\n{pdf_path}"

            keywords = self.tools.extract_keywords(str(pdf_path))

            if not keywords:

                return "No keywords found."

            response = "Top Keywords\n\n"

            for i, keyword in enumerate(keywords, start=1):

                response += f"{i}. {keyword}\n"

            self.last_output = response
            self.last_type = "keywords"

            return response  # =================================================
        # LITERATURE REVIEW
        # =================================================

        elif action == "review":

            if data is None:

                return "Usage:\n\n" "review Retrieval-Augmented Generation"

            review = self.tools.literature_review(data)

            self.last_output = review
            self.last_type = "review"

            return review

        # =================================================
        # CITATION
        # =================================================

        elif action == "cite":

            if data is None:

                return "Usage:\n\n" "cite sample.pdf"

            pdf_path = Path(data)

            if not pdf_path.exists():

                return f"File not found:\n{pdf_path}"

            citation = self.tools.generate_citation(str(pdf_path))

            self.last_output = citation
            self.last_type = "citation"

            return citation

        # =================================================
        # SEARCH
        # =================================================

        elif action == "search":

            if data is None:

                return "Usage:\n\n" "search transformers"

            question = data

        # =================================================
        # DEFAULT CHAT
        # =================================================

        elif action == "chat":

            question = data

        else:

            return "Unknown command."

        # =================================================
        # SEMANTIC SEARCH
        # =================================================

        papers = self.tools.search_papers(question)

        if not papers:

            return "No relevant papers were found."

        context = self._build_context(papers)

        history = self.memory.get_context()

        full_context = history + "\n\n" + context

        answer = self.llm.answer_question(question, full_context)

        # ---------------------------------------------
        # Save Memory
        # ---------------------------------------------

        self.memory.add(question, answer)

        # ---------------------------------------------
        # Save History
        # ---------------------------------------------

        self.history.save(question, answer)

        # ---------------------------------------------
        # Save for Export
        # ---------------------------------------------

        self.last_output = answer
        self.last_type = "search"

        return answer
