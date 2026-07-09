from app.rag import RAGPipeline

rag = RAGPipeline()

question = "Quels sont les projets réalisés ?"

response = rag.ask(question)

print("=" * 80)
print("QUESTION")
print("=" * 80)
print(question)

print()

print("=" * 80)
print("REPONSE")
print("=" * 80)
print(response["answer"])

print()

print("=" * 80)
print("SOURCES")
print("=" * 80)

for source in response["sources"]:

    print()

    print(source["text"][:250])

    print("-" * 80)