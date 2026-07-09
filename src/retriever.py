from src.embeddings import EmbeddingModel
from src.vector_db import VectorStore

class Retriever:

    def __init__(self):
        
        self.embedder = EmbeddingModel()
        self.vector_db = VectorStore()

    def retrieve(self, question, k=3):
        query_embedding = self.embedder.encode([question])[0]

        return self.vector_db.search(
            query_embedding = query_embedding,
            k=k
        )