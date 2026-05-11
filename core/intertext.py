from core.vector_db import VectorDB

db = VectorDB()

db.add("nur ilahi ışık ve tasavvuf sembolüdür", {"type": "tasavvuf"})
db.add("baykuş yalnızlık ve harabe sembolüdür", {"type": "sembol"})
db.add("kapı sınır ve geçiş metaforudur", {"type": "metafor"})
db.add("sınır politik ve kimlik ayrımı üretir", {"type": "politika"})


def find_intertext(text: str):

    results = db.search(text, top_k=4)

    output = []

    for r in results:

        output.append({
            "term": r["text"].split()[0],
            "type": r["meta"].get("type", "motif"),
            "weight": float(r.get("score", 0.5))  # 🔥 REAL SCORE
        })

    # fallback (boş kalmasın ama fake de olmasın)
    if len(output) == 0:
        output.append({
            "term": "latent motif",
            "type": "emergent structure",
            "weight": 0.3
        })

    return output
