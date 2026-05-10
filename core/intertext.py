def find_intertext(poem: str):
    keywords = ["kapı", "baykuş", "nur", "sarp"]

    found = []
    for k in keywords:
        if k in poem.lower():
            found.append({"term": k, "type": "motif"})

    return found
