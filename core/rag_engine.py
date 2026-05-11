from core.vector_db import VectorDB

db = VectorDB()

db.add("Kristeva intertextuality is mosaic of quotations")
db.add("Bakhtin dialogism defines meaning through interaction")
db.add("Postcolonial borders shape identity fragmentation")
db.add("Sufism uses light (nur) as divine metaphor")


def retrieve_academic_context(text: str):

    return db.search(text, top_k=3)
