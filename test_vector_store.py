from src.loader import PDFLoader
from src.chunking import TextChunker
from src.embeddings import EmbeddingModel
from src.vector_db import VectorStore
from src.config import PDF_DIR

loader = PDFLoader(PDF_DIR / "rapport.pdf")

text = loader.load()

chunker = TextChunker()

chunks = chunker.split(text)

embedder = EmbeddingModel()

embeddings = embedder.encode(chunks)

db = VectorStore()

db.build(
    embeddings,
    chunks
)

print("Index créé avec succès.")

index, docs = db.load()

print(index.ntotal)

print(len(docs))