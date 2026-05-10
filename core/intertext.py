def detect_intertext(poem):

    keywords = {
        "bayqush": ["Şehriyar", "Fuzuli", "symbol of exile"],
        "kafes": ["freedom", "political oppression"],
        "nur": ["Sufi poetry", "Ibn Arabi"]
    }

    results = []

    for k, v in keywords.items():
        if k in poem.lower():
            results.append({
                "keyword": k,
                "connections": v
            })

    return results
