def find_intertext(poem: str):

    # placeholder semantic engine (RAG-ready)
    keywords = ["nur", "baykuş", "kapı", "sınır"]

    relations = []

    for k in keywords:
        if k in poem.lower():
            relations.append({
                "term": k,
                "type": "intertextual_motif"
            })

    return relations
