from fastapi import FastAPI
from app.schemas import QuestionRequest
from app.rag import RAGPipeline
from src.indexer import DocumentIndexer
from src.config import PDF_DIR

app = FastAPI(
    title= 'RAG DOcument Assistant',
    version="1.0.0"
)

rag = RAGPipeline()

indexer = DocumentIndexer()

@app.get("/health")
def health():
    return {
        "status": 'ok'
    }

@app.post("/ask")
def ask(request: QuestionRequest):
    return rag.ask(request.question)

@app.post("/upload")
def upload(file: UploadFile = File(...)):

    destination = PDF_DIR / file.filename

    with open(destination, "wb") as buffer:

        copyfileobj(file.file, buffer)

    chunks = indexer.build_index()

    return {

        "message": "Document indexed successfully.",

        "chunks": chunks,

        "filename": file.filename

    }