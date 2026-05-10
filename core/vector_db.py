db = []

def add_poem(id, text, metadata=None):

    db.append({
        "id": id,
        "text": text,
        "metadata": metadata or {}
    })


def search(query, k=5):

    if not db:
        return {"documents": [[]]}

    q = query.lower().split()

    scored = []

    for item in db:

        text = item["text"].lower()

        score = sum(1 for w in q if w in text)

        scored.append((score, item["text"]))

    scored.sort(reverse=True, key=lambda x: x[0])

    return {
        "documents": [[t for _, t in scored[:k]]]
    }
