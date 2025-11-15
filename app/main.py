from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.rag.retriever import retrieve_context
from app.rag.generator import generate_answer

app = FastAPI(title="RAG Insight – Retrieval Augmented API")

@app.get("/")
def root():
    return {"message": "RAG Insight API Running"}

@app.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):
    context = retrieve_context(request.question)
    answer = generate_answer(request.question, context)
    return QueryResponse(
        question=request.question,
        answer=answer,
        retrieved_context=context
    )
