from core.vector_db import search
from core.llm_engine import ask_gpt


def rag_answer(query):

    results = search(query)

    documents = results.get("documents", [[]])

    retrieved_docs = documents[0] if documents else []

    context = "\n\n".join(retrieved_docs)

    prompt = f"""
You are an expert academic researcher specializing in:

- Turkic literature
- Azerbaijani poetry
- Ottoman poetry
- Persian literary traditions
- Digital humanities
- Intertextuality

Use the academic context below to answer the question.

ACADEMIC CONTEXT:
{context}

QUESTION:
{query}

Instructions:
- Use academic tone
- Mention literary traditions
- Explain historical background
- Include intertextual observations
- Be analytical and structured
"""

    answer = ask_gpt(prompt)

    return answer
