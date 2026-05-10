from core.vector_db import search_similar

def find_similar_poems(poem):

    results = search_similar(poem, k=5)

    return results["documents"][0]
