from src.loader import PDFLoader
from src.chunking import TextChunker
from src.embeddings import EmbeddingModel
from src.vector_db import VectorStore
from src.config import PDF_DIR


class DocumentIndexer:

    def __init__(self):

        self.chunker = TextChunker()
        self.embedder = EmbeddingModel()
        self.db = VectorStore()

    def build_index(self):

        documents = []

        for pdf in PDF_DIR.glob("*.pdf"):

            loader = PDFLoader(pdf)

            text = loader.load()

            chunks = self.chunker.split(text)

            documents.extend(chunks)

        embeddings = self.embedder.encode(documents)

        self.db.build(
            embeddings,
            documents
        )

        return len(documents)