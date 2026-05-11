import numpy as np
from core.embeddings import embed_text


class VectorDB:

    def __init__(self):
        self.vectors = []
        self.docs = []

    def add(self, text: str, metadata=None):
        vec = embed_text(text)
        self.vectors.append(vec)
        self.docs.append({"text": text, "meta": metadata or {}})

    def search(self, query: str, top_k=3):

        if not self.vectors:
            return []

        q = embed_text(query)

        scores = []

        for i, v in enumerate(self.vectors):

            # 🔥 FIX 1: numerical stability + real cosine
            denom = (np.linalg.norm(q) * np.linalg.norm(v))
            if denom == 0:
                continue

            sim = float(np.dot(q, v) / denom)

            scores.append((sim, self.docs[i]))

        # 🔥 FIX 2: NO artificial flattening
        scores.sort(key=lambda x: x[0], reverse=True)

        return [
            {
                "text": doc["text"],
                "meta": doc["meta"],
                "score": round(score, 6)
            }
            for score, doc in scores[:top_k]
        ]
