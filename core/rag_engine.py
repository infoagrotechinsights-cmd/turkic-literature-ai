def retrieve_academic_context(text: str):

    text = text.lower()

    corpus = [
        {
            "text": "Kristeva’ya göre metinler bir alıntılar mozaiğidir.",
            "score": 0.92
        },
        {
            "text": "Bakhtin çok seslilik kavramı ile metin içi diyalojiyi açıklar.",
            "score": 0.88
        },
        {
            "text": "Sınır metaforu postkolonyal edebiyatta kimlik parçalanmasını temsil eder.",
            "score": 0.86
        },
        {
            "text": "Tasavvufta ‘nur’ ilahi hakikatin sembolüdür.",
            "score": 0.9
        }
    ]

    results = []

    keywords = ["nur", "kapı", "qapı", "baykuş", "bayquş", "sınır"]

    if any(k in text for k in keywords):
        results = corpus
    else:
        results = [corpus[0], corpus[1]]

    return results
