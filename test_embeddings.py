from src.loader import PDFLoader
from src.chunking import TextChunker
from src.embeddings import EmbeddingModel
from src.config import PDF_DIR

loader = PDFLoader(PDF_DIR / "rapport.pdf")

text = loader.load()

chunker = TextChunker()

chunks = chunker.split(text)

embedder = EmbeddingModel()

vectors = embedder.encode(chunks)

print("Nombre de chunks :", len(chunks))

print("Shape :", vectors.shape)

print(vectors[0][:10])