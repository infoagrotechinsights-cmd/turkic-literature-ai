def find_intertext(text: str):

    base_terms = [
        "nur",
        "baykuş",
        "kapı",
        "sınır",
        "yer",
        "göy"
    ]

    results = []

    lower = text.lower()

    for term in base_terms:
        if term in lower:
            results.append({
                "term": term,
                "type": "intertext_motif"
            })

    return results
