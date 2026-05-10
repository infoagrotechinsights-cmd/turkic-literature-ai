from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

memory = []

def add(text):
    emb = model.encode(text)
    memory.append((text, emb))

def search(query, top_k=5):
    q_emb = model.encode(query)

    scored = []

    for text, emb in memory:
        score = (q_emb @ emb)
        scored.append((score, text))

    scored.sort(reverse=True)

    return [t for _, t in scored[:top_k]]
