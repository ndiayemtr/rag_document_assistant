from src.embeddings import EmbeddingModel
from src.vector_db import VectorStore

embedder = EmbeddingModel()

db = VectorStore()

question = "Quels sont les projets de Data Science ?"

query_embedding = embedder.encode([question])[0]

results = db.search(
    query_embedding,
    k=3
)

print("=" * 80)

print("QUESTION")

print(question)

print("=" * 80)

for result in results:

    print("=" * 80)

    print("Distance :", result["score"])

    print()

    print(result["text"])