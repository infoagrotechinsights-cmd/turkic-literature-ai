def align_poem(poem: str):

    from core.embeddings import embed_text

    emb = embed_text(poem)

    return {
        "embedding": emb,
        "score": 0.95
    }
