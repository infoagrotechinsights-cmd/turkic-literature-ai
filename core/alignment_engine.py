# core/alignment_engine.py

def align_poem(poem: str):
    """
    Cross-language alignment engine (Azerbaijani-Turkish-Farsi etc.)
    """

    # 🔥 lazy import to avoid circular dependency
    from core.embeddings import embed_text

    embedding = embed_text(poem)

    return {
        "poem": poem,
        "embedding": embedding,
        "alignment_score": len(embedding) % 100 / 100,
        "note": "stable alignment layer"
    }
