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

        score = r.get("score", 0.5)
        meta = r.get("meta", {})

        output.append({
            "term": r["text"].split()[0],
            "type": meta.get("type", "motif"),
            "weight": score
        })

    # fallback (boş sistem engeli)
    if not output:
        output.append({
            "term": "genel metaforik yapı",
            "type": "poetik sistem",
            "weight": 0.4
        })

    return output
