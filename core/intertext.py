from core.vector_db import VectorDB

db = VectorDB()

# mini knowledge base
db.add("nur ilahi ışık ve tasavvuf sembolüdür", {"type": "tasavvuf"})
db.add("baykuş yalnızlık ve harabe sembolüdür", {"type": "sembol"})
db.add("kapı sınır ve geçiş metaforudur", {"type": "metafor"})
db.add("sınır kimlik ve politik ayrım üretir", {"type": "politika"})


def find_intertext(text: str):

    results = db.search(text, top_k=4)

    output = []

    for r in results:

        output.append({
            "term": r["text"].split()[0],
            "type": r["meta"].get("type", "motif"),
            "weight": 0.85
        })

    return output
