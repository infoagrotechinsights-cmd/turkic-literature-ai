import numpy as np

MOTIF_DB = {
    "nur": "tasavvuf",
    "kapı": "metafor",
    "baykuş": "yalnızlık",
    "sınır": "politik yapı",
    "yer": "mekan",
    "göy": "kozmoloji"
}

def align_poem(poem: str):

    words = poem.lower().split()
    result = []

    for w in words:
        if w in MOTIF_DB:
            result.append({
                "term": w,
                "type": MOTIF_DB[w],
                "score": float(np.clip(len(w)/10, 0.4, 0.95))
            })

    return result
