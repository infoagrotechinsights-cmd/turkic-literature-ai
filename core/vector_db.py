# =========================
# SIMPLE IN-MEMORY VECTOR DB
# (NO chromadb, NO protobuf issues)
# =========================

db = []


def add_poem(id, text, metadata=None):
    """
    Add poem to in-memory database
    """

    db.append({
        "id": id,
        "text": text,
        "metadata": metadata or {}
    })


def search(query, k=5):
    """
    Simple keyword-based retrieval (RAG fallback version)
    """

    if not db:
        return {"documents": [[]]}

    query_words = set(query.lower().split())

    scored = []

    for item in db:

        text_words = set(item["text"].lower().split())

        # simple overlap score
        score = len(query_words.intersection(text_words))

        scored.append((score, item["text"]))

    # sort by relevance
    scored.sort(reverse=True, key=lambda x: x[0])

    top_k = [text for _, text in scored[:k]]

    return {
        "documents": [top_k]
    }

    return results
