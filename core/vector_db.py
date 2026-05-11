# core/vector_db.py

import math


class VectorDB:

    def __init__(self):

        self.documents = []
        self.vectors = []

    # -------------------------
    # SIMPLE EMBEDDING
    # -------------------------

    def embed(self, text: str):

        # deterministic pseudo embedding (production-ready later swap)
        return [hash(word) % 1000 for word in text.lower().split()]

    # -------------------------
    # COSINE SIMILARITY
    # -------------------------

    def cosine(self, a, b):

        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))

        if norm_a == 0 or norm_b == 0:
            return 0

        return dot / (norm_a * norm_b)

    # -------------------------
    # ADD DOCUMENT
    # -------------------------

    def add_document(self, text: str, metadata=None):

        vec = self.embed(text)

        self.documents.append({
            "text": text,
            "metadata": metadata or {}
        })

        self.vectors.append(vec)

    # -------------------------
    # SEARCH
    # -------------------------

    def search(self, query: str, top_k=5):

        q_vec = self.embed(query)

        scores = []

        for i, vec in enumerate(self.vectors):

            score = self.cosine(q_vec, vec)

            scores.append({
                "text": self.documents[i]["text"],
                "metadata": self.documents[i]["metadata"],
                "score": round(score, 4)
            })

        scores = sorted(
            scores,
            key=lambda x: x["score"],
            reverse=True
        )

        return scores[:top_k]
