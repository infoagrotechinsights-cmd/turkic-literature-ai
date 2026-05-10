from core.vector_db import search
from core.llm_engine import ask_gpt

def rag_answer(query):

    results = search(query)

    docs = results.get("documents", [[]])[0]

    context = "\n".join(docs)

    prompt = f"""
You are an academic Turkic literature expert.

Context:
{context}

Question:
{query}

Answer in academic style.
"""

    return ask_gpt(prompt)
