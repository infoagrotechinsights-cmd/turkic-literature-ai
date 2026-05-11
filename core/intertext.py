def find_intertext(text: str):

    text = text.lower()

    motifs = []

    lexicon = {
        "nur": ("tasavvuf motifi", 0.9),
        "qapı": ("sınır metaforu", 0.85),
        "kapı": ("sınır metaforu", 0.85),
        "bayquş": ("yalnızlık sembolü", 0.8),
        "baykuş": ("yalnızlık sembolü", 0.8),
        "darlığa": ("ontolojik sıkışma", 0.75),
        "yer": ("kozmik mekan", 0.6),
        "göy": ("kozmik üst dünya", 0.6)
    }

    for key, (typ, weight) in lexicon.items():

        if key in text:

            motifs.append({
                "term": key,
                "type": typ,
                "weight": weight
            })

    return motifs
