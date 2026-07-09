from src.retriever import Retriever

retrieve = Retriever()

results = retrieve.retrieve("Quels sont les projets de Data Science ?")

for i, result in enumerate(results, start=1):
    print("=" * 80)
    print(f"Resultat {i}")
    print("=" * 80)

    print("Distance :", result["score"])
    print()
    print(result["text"])

