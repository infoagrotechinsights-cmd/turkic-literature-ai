# core/rag_engine.py

from core.vector_db import VectorDB


db = VectorDB()

# preload corpus
db.add_document("Sınır metaforu Türk dünyasında kültürel ayrışma temsilidir.",
                {"type": "theory"})

db.add_document("Baykuş Divan şiirinde yalnızlık ve harabe sembolüdür.",
                {"type": "motif"})

db.add_document("Nur tasavvufta ilahi hakikatin sembolüdür.",
                {"type": "symbol"})

db.add_document("Kristeva metni alıntılar mozaiği olarak tanımlar.",
                {"type": "theory"})


def retrieve_academic_context(poem: str):

    return db.search(poem, top_k=5)
