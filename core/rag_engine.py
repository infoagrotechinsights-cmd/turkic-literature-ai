from core.vector_db import VectorDB

db = VectorDB()

db.add("Kristeva: metinlerarasılık bir alıntılar mozaiğidir")
db.add("Bakhtin: anlam diyalojik etkileşimle oluşur")
db.add("Sınır metaforu postkolonyal kimlik üretir")
db.add("Tasavvufta nur ilahi hakikatin sembolüdür")
db.add("Edebiyatta motifler kültürel hafıza üretir")


def retrieve_academic_context(text: str):

    results = db.search(text, top_k=3)

    # 🔥 FIX: diversity (aynı şeyleri döndürmesin)
    seen = set()
    filtered = []

    for r in results:

        t = r["text"]

        if t not in seen:
            filtered.append(r)
            seen.add(t)

    return filtered
