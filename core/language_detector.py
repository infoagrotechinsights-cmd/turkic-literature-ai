from langdetect import detect

def detect_language(text: str):

    try:
        lang = detect(text)

        if lang in ["az", "tr"]:
            return lang

        return "foreign"

    except:
        return "unknown"


def force_turkish_output(text: str):

    # basit güvenlik filtresi
    forbidden = [" the ", " and ", " of ", " Azerbaycan", "Azərbaycan"]

    for f in forbidden:
        if f.lower() in text.lower():
            return "⚠️ Dil ihlali tespit edildi. Türkçe yeniden üretim gerekli."

    return text
