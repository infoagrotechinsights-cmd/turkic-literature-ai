from core.vector_db import search_vectors
from core.embeddings import embed_text
from core.similarity import cosine_similarity

def find_intertext(poem, top_k=7):

    query_vec = embed_text(poem)

    results = search_vectors(query_vec, top_k=top_k)

    enriched = []

    for r in results:

        score = cosine_similarity(query_vec, r["vector"])

        enriched.append({
            "text": r["text"],
            "author": r.get("author", "unknown"),
            "language": r.get("language", "unknown"),
            "score": float(score),
            "motifs": r.get("motifs", []),
            "type": "semantic_similarity"
        })

    return sorted(enriched, key=lambda x: x["score"], reverse=True)
