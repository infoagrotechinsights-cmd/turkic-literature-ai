# core/intertext.py

INTERTEXT_DB = {

    "baykuş": {
        "tradition": "Divan Şiiri",
        "meaning": "Harabe, yalnızlık, terk edilmişlik",
        "related_authors": [
            "Fuzuli",
            "Baki",
            "Şeyh Galib"
        ],
        "theory": "Bakhtin - Polyphony",
        "academic_note":
            "Baykuş imgesi klasik Türk şiirinde virane ve yalnızlık metaforu olarak kullanılmıştır."
    },

    "nur": {
        "tradition": "Tasavvuf Şiiri",
        "meaning": "İlahi hakikat, vahdet, metafizik aydınlanma",
        "related_authors": [
            "Yunus Emre",
            "Mevlana",
            "İbn Arabi"
        ],
        "theory": "Tasavvufi Metinlerarasılık",
        "academic_note":
            "Nur kavramı Türk-İslam düşüncesinde ilahi hakikatin sembolüdür."
    },

    "kapı": {
        "tradition": "Ontolojik Eşik Metaforu",
        "meaning": "Geçiş, sınır, eşik",
        "related_authors": [
            "Heidegger",
            "Bachelard"
        ],
        "theory": "Mekan Poetikası",
        "academic_note":
            "Kapı imgesi fiziksel değil ontolojik geçiş alanı olarak yorumlanabilir."
    },

    "sarp": {
        "tradition": "Türk Dünyası Şiiri",
        "meaning": "Sınır, ayrılık, kültürel bölünmüşlük",
        "related_authors": [
            "Bahtiyar Vahapzade",
            "Zelimhan Yakup"
        ],
        "theory": "Postkolonyal Türk Dünyası Okuması",
        "academic_note":
            "Sarp sınırı Türk dünyasının parçalanmış hafızasının metaforu olarak okunabilir."
    }
}


def find_intertext(poem: str):

    poem_lower = poem.lower()

    findings = []

    for keyword, data in INTERTEXT_DB.items():

        if keyword in poem_lower:

            findings.append({

                "keyword": keyword,

                "tradition": data["tradition"],

                "meaning": data["meaning"],

                "related_authors": data["related_authors"],

                "theory": data["theory"],

                "academic_note": data["academic_note"]

            })

    return findings
