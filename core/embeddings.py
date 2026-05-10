# core/embeddings.py

def embed_text(text: str):
    """
    Lightweight deterministic embedding (fallback version).
    Replace later with sentence-transformers or OpenAI embeddings.
    """
    if not text:
        return []

    # simple stable placeholder embedding
    return [hash(text) % 10000]
