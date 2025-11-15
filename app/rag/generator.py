import openai
from app.config import OPENAI_API_KEY, LLM_MODEL

openai.api_key = OPENAI_API_KEY

def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are a RAG-based assistant. Use ONLY the provided context.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
    response = openai.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
