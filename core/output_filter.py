def clean(text: str):

    banned = [
        "COLOra",
        "femeyra",
        "Türk'ümüz",
        "issinden",
        "aracı kelimeler"
    ]

    for b in banned:
        if b in text:
            return "⚠️ Model çıktısı bozuldu (filter triggered)"

    return text
