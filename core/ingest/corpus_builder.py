import json

def build_parallel_corpus():

    corpus = [
        {
            "az": "Sarp qapısı, məni darlığa salma",
            "tr": "Sarp kapısı, beni darlığa sokma"
        },
        {
            "az": "Qoy nur yağsın yerə",
            "tr": "Nur yağsın yere"
        }
    ]

    with open("data/corpus_az_tr.json", "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)

    return corpus
