import openai
from app.utils.file_loader import load_documents
from app.utils.chroma_manager import get_chroma
from app.config import OPENAI_API_KEY, DOCS_DIR, EMBED_MODEL
from langchain_text_splitters import RecursiveCharacterTextSplitter

openai.api_key = OPENAI_API_KEY

def embed_text(texts):
    response = openai.embeddings.create(
        model=EMBED_MODEL,
        input=texts
    )
    return [e.embedding for e in response.data]

def ingest_docs():
    docs = load_documents(DOCS_DIR)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = []

    for doc in docs:
        chunks.extend(splitter.split_text(doc))

    embeddings = embed_text(chunks)

    chroma = get_chroma()
    collection = chroma.get_or_create_collection("rag_insight")

    for idx, chunk in enumerate(chunks):
        collection.add(documents=[chunk], embeddings=[embeddings[idx]], ids=[str(idx)])

    chroma.persist()
    print("Documents successfully ingested!")
