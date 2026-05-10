def embed_text(text: str):

    if not text:
        return []

    return [hash(text) % 10000]
