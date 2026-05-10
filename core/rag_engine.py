from core.vector_db import search
from core.llm_engine import ask_gpt

def rag_answer(query):

    results = search(query)

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are an academic literary researcher.

Use context below:

{context}

Question:
{query}

Provide:
- academic analysis
- intertextual links
- historical interpretation
"""

    return ask_gpt(prompt)
