"""
history_manager.py
------------------
Persistent conversation history.
"""

import json
from datetime import datetime
from pathlib import Path


class HistoryManager:

    def __init__(self):

        self.file = Path("logs/history.json")

        if not self.file.exists():

            self.file.parent.mkdir(parents=True, exist_ok=True)

            self.file.write_text("[]", encoding="utf-8")

    def save(self, question, answer):

        history = self.load()

        history.append(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "question": question,
                "answer": answer,
            }
        )

        self.file.write_text(json.dumps(history, indent=4), encoding="utf-8")

    def load(self):

        try:

            return json.loads(self.file.read_text(encoding="utf-8"))

        except:

            return []

    def clear(self):

        self.file.write_text("[]", encoding="utf-8")
