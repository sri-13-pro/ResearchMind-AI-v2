from services.pdf_processor import PDFProcessor
from services.summarizer import PaperSummarizer

processor = PDFProcessor()

text = processor.extract_text("sample.pdf")

summarizer = PaperSummarizer()

summary = summarizer.summarize(text)

print(summary)
