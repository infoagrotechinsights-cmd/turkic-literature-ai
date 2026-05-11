def find_intertext(text: str):

    text = text.lower()

    lexicon = {
        "nur": ("tasavvuf motifi", 0.9),
        "qapı": ("sınır metaforu", 0.85),
        "kapı": ("sınır metaforu", 0.85),
        "baykuş": ("yalnızlık sembolü", 0.8),
        "bayquş": ("yalnızlık sembolü", 0.8),
        "darlığa": ("ontolojik sıkışma", 0.75)
    }

    results = []

    for k, (t, w) in lexicon.items():

        if k in text:

            results.append({
                "term": k,
                "type": t,
                "weight": w
            })

    # ❗ boş kalmasın (fallback)
    if not results:
        results.append({
            "term": "genel metaforik yapı",
            "type": "poetik yapı",
            "weight": 0.5
        })

    return results
