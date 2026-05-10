def clean_output(text: str):

    bad_patterns = [
        "Türk'ümüz gösteriyoruz",
        "BURA (COLOra",
        "femeyra",
        "issinden geçmiş",
        "aracı kelimelerden biri"
    ]

    for b in bad_patterns:
        if b in text:
            return "⚠️ Model çıktısı bozuldu. Lütfen yeniden deneyin."

    return text
