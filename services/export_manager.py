"""
export_manager.py
-----------------
Export AI outputs to Markdown files.
"""

from datetime import datetime
from pathlib import Path


class ExportManager:

    def __init__(self):

        self.export_dir = Path("exports")
        self.export_dir.mkdir(exist_ok=True)

    def export(self, export_type: str, content: str):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{export_type}_{timestamp}.md"

        filepath = self.export_dir / filename

        with open(filepath, "w", encoding="utf-8") as file:

            file.write(f"# {export_type.title()}\n\n")

            file.write(content)

        return filepath
