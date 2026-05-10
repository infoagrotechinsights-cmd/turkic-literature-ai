from core.crossref_client import search_crossref

def rag_answer(query):

    sources = search_crossref(query)

    response = {
        "analysis_query": query,
        "real_sources": sources
    }

    return response
