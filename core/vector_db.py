import numpy as np
from core.embeddings import embed_text


class VectorDB:

    def __init__(self):
        self.vectors = []
        self.docs = []

    def add(self, text: str, metadata=None):

        vec = embed_text(text)

        self.vectors.append(vec)
        self.docs.append({
            "text": text,
            "meta": metadata or {}
        })

    def search(self, query: str, top_k=3):

        if len(self.vectors) == 0:
            return []

        q = embed_text(query)

        scores = []

        for i, v in enumerate(self.vectors):

            sim = np.dot(q, v) / (
                np.linalg.norm(q) * np.linalg.norm(v)
            )

            scores.append((sim, self.docs[i]))

        scores.sort(reverse=True, key=lambda x: x[0])

        return [doc for _, doc in scores[:top_k]]
