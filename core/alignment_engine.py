def align_poem(poem: str):
    from core.embeddings import embed_text  # lazy import

    emb = embed_text(poem)

    return {
        "embedding": emb,
        "alignment_score": len(emb) % 100 / 100
    }
