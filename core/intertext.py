from core.motif_engine import extract_motifs

def find_intertext(poem, top_k=7):

    query_vec = embed_text(poem)
    results = search_vectors(query_vec, top_k=top_k)

    poem_motifs = extract_motifs(poem)

    enriched = []

    for r in results:

        score = cosine_similarity(query_vec, r["vector"])
        motifs = extract_motifs(r["text"])

        enriched.append({
            "text": r["text"],
            "author": r.get("author", "unknown"),
            "score": float(score),
            "motifs": motifs,
            "shared_structure": len(set([m["term"] for m in motifs]) &
                                    set([m["term"] for m in poem_motifs])),
            "type": "semantic+motif_similarity"
        })

    return enriched
