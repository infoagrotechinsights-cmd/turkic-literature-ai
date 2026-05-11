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

            denom = (np.linalg.norm(q) * np.linalg.norm(v)) + 1e-8
            sim = float(np.dot(q, v) / denom)

            scores.append((sim, self.docs[i]))

        scores.sort(key=lambda x: x[0], reverse=True)

        return [
            {
                "text": doc["text"],
                "meta": doc["meta"],
                "score": round(score, 4)
            }
            for score, doc in scores[:top_k]
        ]
