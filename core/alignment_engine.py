from core.embeddings import embed_text
import numpy as np

MOTIF_DB = {
    "nur": "tasavvuf",
    "kapı": "metafor",
    "baykuş": "yalnızlık",
    "sınır": "politik sınır",
    "yer": "kozmik mekan",
    "göy": "kozmoloji"
}

def align_poem(poem: str):

    words = poem.lower().split()
    result = []

    for w in words:
        if w in MOTIF_DB:
            score = float(np.clip(len(w)/10, 0.4, 0.95))

            result.append({
                "term": w,
                "type": MOTIF_DB[w],
                "score": score
            })

    return result
