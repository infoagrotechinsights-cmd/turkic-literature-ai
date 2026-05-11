from core.vector_db import VectorDB

db = VectorDB()

db.add("Kristeva metinlerarasılığı alıntılar mozaiği olarak açıklar")
db.add("Bakhtin söylem teorisi diyalojik yapı üzerine kuruludur")
db.add("Postkolonyal teori sınır ve kimlik krizini analiz eder")
db.add("Tasavvufta nur ilahi hakikatin sembolüdür")


def retrieve_academic_context(text: str):

    results = db.search(text, top_k=3)

    return sorted(results, key=lambda x: x["score"], reverse=True)
