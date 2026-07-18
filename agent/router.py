"""
router.py
----------
Routes user commands to the appropriate tool.
"""

from pathlib import Path


class CommandRouter:

    def route(self, command: str):

        command = command.strip()

        lower = command.lower()

        # Help
        if lower == "help":
            return ("help", None)

        # Clear memory
        if lower == "clear":
            return ("clear", None)

        # Summarize PDF
        if lower.startswith("summarize"):

            parts = command.split(maxsplit=1)

            if len(parts) < 2:
                return ("summarize", None)

            return ("summarize", parts[1])

        # Search command
        if lower.startswith("search"):

            parts = command.split(maxsplit=1)

            if len(parts) < 2:
                return ("search", None)

            return ("search", parts[1])

        # Compare command
        if lower.startswith("compare"):

            parts = command.split(maxsplit=2)

            if len(parts) < 3:
                return ("compare", None)

            return ("compare", (parts[1], parts[2]))

        # Keywords
        if lower.startswith("keywords"):

            parts = command.split(maxsplit=1)

            if len(parts) < 2:
                return ("keywords", None)

            return ("keywords", parts[1])

        # Literature Review
        if lower.startswith("review"):

            parts = command.split(maxsplit=1)

            if len(parts) < 2:
                return ("review", None)

            return ("review", parts[1])

        # Citation
        if lower.startswith("cite"):

            parts = command.split(maxsplit=1)

            if len(parts) < 2:
                return ("cite", None)

            return ("cite", parts[1])

        # Default: Treat as research question
        return ("chat", command)
