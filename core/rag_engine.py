from core.vector_db import search
from core.crossref_client import search_crossref

def rag_answer(query: str):

    # 1. Vector DB retrieval (internal corpus)
    local_results = search(query)

    # 2. Real academic sources (CrossRef)
    external_results = search_crossref(query)

    # 3. Merge context
    context = {
        "local": local_results,
        "external": external_results
    }

    return context
