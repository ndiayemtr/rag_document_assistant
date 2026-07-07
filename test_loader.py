from src.loader import PDFLoader
from src.config import PDF_DIR

loader = PDFLoader(PDF_DIR / "rapport.pdf")

text = loader.load()

print(text[:100])