from src.loader import PDFLoader
from src.chunking import TextChunker
from src.config import PDF_DIR


loader = PDFLoader(PDF_DIR / "rapport.pdf")

text = loader.load()

chunker = TextChunker()

chunks = chunker.split(text)

print("Nombre de chunks:", len(chunks))

print("\nPremier chunk :\n")

print(chunks[0])