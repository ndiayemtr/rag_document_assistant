from ollama import Client

from src.retriever import Retriever


class RAGPipeline:

    def __init__(self):

        self.client = Client(host="http://localhost:11434")

        self.retriever = Retriever()

        self.model = "llama3.2:3b"

    def build_prompt(self, question, contexts):

        context = "\n\n".join(
            [item["text"] for item in contexts]
        )

        prompt = f"""
You are an AI assistant.

Answer ONLY using the information contained in the context.

If the answer is not present in the context,
say that you cannot answer.

Context:

{context}

Question:

{question}

Answer:
"""

        return prompt

    def ask(self, question):

        contexts = self.retriever.retrieve(
            question,
            k=3
        )

        prompt = self.build_prompt(
            question,
            contexts
        )

        response = self.client.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return {
            "answer": response["message"]["content"],
            "sources": contexts
        }