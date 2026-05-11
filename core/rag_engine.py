def retrieve_academic_context(text: str):

    corpus = [
        {
            "text": "Kristeva: Metinlerarasılık bir alıntılar mozaiğidir.",
            "score": 0.95
        },
        {
            "text": "Bakhtin: Her söylem başka söylemlerle diyalog halindedir.",
            "score": 0.93
        },
        {
            "text": "Sınır metaforu postkolonyal literatürde kimlik krizini temsil eder.",
            "score": 0.89
        },
        {
            "text": "Tasavvufta 'nur' ilahi hakikatin sembolüdür.",
            "score": 0.92
        }
    ]

    text = text.lower()

    keywords = ["nur", "kapı", "qapı", "baykuş", "sınır", "darlık"]

    # ❗ HER ZAMAN GERİ DÖN (boş kalma yok)
    if any(k in text for k in keywords):
        return corpus
    else:
        return corpus[:2]
