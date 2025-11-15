import openai
from app.utils.chroma_manager import get_chroma
from app.config import OPENAI_API_KEY, EMBED_MODEL

openai.api_key = OPENAI_API_KEY

def embed_query(question):
    return openai.embeddings.create(model=EMBED_MODEL, input=question).data[0].embedding

def retrieve_context(question: str) -> str:
    chroma = get_chroma()
    collection = chroma.get_collection("rag_insight")

    q_embed = embed_query(question)
    results = collection.query(query_embeddings=[q_embed], n_results=3)

    contexts = results["documents"][0]
    return "\n\n".join(contexts)
