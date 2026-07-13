from fastapi import FastAPI
from app.schemas import QuestionRequest
from app.rag import RAGPipeline

app = FastAPI(
    title= 'RAG DOcument Assistant',
    version="1.0.0"
)

rag = RAGPipeline()

@app.get("/health")
def health():
    return {
        "status": 'ok'
    }

@app.post("/ask")
def ask(request: QuestionRequest):
    return rag.ask(request.question)