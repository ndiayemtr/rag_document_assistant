import faiss
import joblib
import numpy as np

from src.config import VECTOR_STORE


class VectorStore:

    def __init__(self):

        VECTOR_STORE.mkdir(exist_ok=True)

        self.index_path = VECTOR_STORE / "index.faiss"
        self.doc_path = VECTOR_STORE / "documents.pkl"

    def build(self, embeddings, documents):

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(np.array(embeddings).astype("float32"))

        faiss.write_index(index, str(self.index_path))

        joblib.dump(documents, self.doc_path)

    def load(self):

        index = faiss.read_index(str(self.index_path))

        docs = joblib.load(self.doc_path)

        return index, docs
    
    def search(self, query_embedding, k=3):

        index, docs = self.load()

        distances, indices = index.search(
            np.array([query_embedding]).astype("float32"),
            k
        )

        results = []

        for score, idx in zip(distances[0], indices[0]):

            results.append(
                {
                    "score": float(score),
                    "text": docs[idx]
                }
            )

        return results