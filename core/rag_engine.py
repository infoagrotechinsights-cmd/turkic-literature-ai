# core/rag_engine.py

from difflib import SequenceMatcher


ACADEMIC_CORPUS = [

    {
        "title": "Türk Dünyası Şiirinde Sınır Metaforu",
        "content":
            "Sınır kavramı modern Türk dünyası şiirinde ontolojik ayrılık ve kültürel parçalanmışlık metaforu olarak kullanılır."
    },

    {
        "title": "Tasavvuf Şiirinde Nur İmgesi",
        "content":
            "Nur kavramı tasavvuf düşüncesinde ilahi hakikatin görünümü olarak değerlendirilir."
    },

    {
        "title": "Divan Şiirinde Baykuş Motifi",
        "content":
            "Baykuş klasik şiirde harabe, yalnızlık ve terk edilmişliğin sembolüdür."
    },

    {
        "title": "Bakhtin ve Çok Seslilik",
        "content":
            "Bakhtin'e göre metinler farklı söylemlerin kesişim alanıdır."
    },

    {
        "title": "Kristeva ve Metinlerarasılık",
        "content":
            "Kristeva her metni bir alıntılar mozaiği olarak tanımlar."
    }

]


def similarity(a, b):

    return SequenceMatcher(
        None,
        a.lower(),
        b.lower()
    ).ratio()


def retrieve_academic_context(poem):

    results = []

    for doc in ACADEMIC_CORPUS:

        score = similarity(
            poem,
            doc["content"]
        )

        if score > 0.10:

            results.append({

                "title": doc["title"],
                "content": doc["content"],
                "score": round(score, 3)

            })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:5]
