from services.pdf_processor import PDFProcessor

processor = PDFProcessor()

pdf_path = "sample.pdf"

text = processor.extract_text(pdf_path)

print("=" * 80)
print(text[:3000])
