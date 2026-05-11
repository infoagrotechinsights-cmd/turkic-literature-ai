def render_academic_output(poem: str, result: dict):

    intertext = result.get("intertext", []) or []
    rag = result.get("rag", []) or []

    def safe(item, key, default):
        return item.get(key, default) if isinstance(item, dict) else default

    text = "# 📚 Academic Analysis (Semantic Engine)\n\n"

    text += "## 1. Metinlerarasılık Analizi\n"

    for item in intertext:

        term = safe(item, "term", "öğe")
        typ = safe(item, "type", "motif")
        weight = safe(item, "weight", 0.0)

        text += f"- **{term}** → {typ} (score: {round(weight,3)})\n"

    text += "\n## 2. Kuramsal Bağlam\n"

    for r in rag:

        if isinstance(r, dict):
            text += f"- {r.get('text','')}\n(score: {r.get('score',0)})\n"

    text += "\n## 3. Sonuç\n"

    text += "Bu analiz sabit şablon değil, semantic similarity tabanlı üretimle oluşturulmuştur.\n"

    return text
