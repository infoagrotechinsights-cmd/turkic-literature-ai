def render_academic_output(poem: str, result: dict):

    intertext = result.get("intertext") or []
    citations = result.get("citations") or []
    rag = result.get("rag") or []

    def safe(item, key, default="metin öğesi"):
        if isinstance(item, dict):
            return item.get(key, default)
        return default

    text = f"""
# 📚 Academic Analysis (PhD Level)

## 1. Giriş

Bu metin, metinlerarasılık kuramı çerçevesinde değerlendirildiğinde çok katmanlı bir anlam ağı üretmektedir. Kristeva’ya göre her metin, önceki söylemlerin dönüşümüyle oluşan bir “alıntılar mozaiği”dir.

---

## 2. Metinlerarasılık Katmanı
"""

    # =========================
    # INTERTEXT SAFE SECTION
    # =========================
    if isinstance(intertext, list) and len(intertext) > 0:

        for item in intertext:

            term = safe(item, "term", "metin öğesi")
            typ = safe(item, "type", "motif")
            weight = safe(item, "weight", 0.5)

            text += f"""
### {term}

Bu öğe metin içinde **{typ}** olarak işlev görmektedir. 
Ağırlık skoru: {weight}. 
Metinlerarasılık açısından bu yapı, kültürel hafıza ve sembolik yeniden üretim mekanizmalarıyla ilişkilidir.
"""

    else:

        text += """
Metin içinde belirgin intertext öğesi bulunmamaktadır. Ancak şiir, örtük metaforik yapı nedeniyle yine de yorumlanabilir bir söylem ağı üretmektedir.
"""

    # =========================
    # RAG SECTION
    # =========================
    text += """

---

## 3. Kuramsal Arka Plan (RAG Destekli)
"""

    if isinstance(rag, list) and len(rag) > 0:

        for r in rag:

            if isinstance(r, dict):
                text += f"- {r.get('text','')}\n"

    else:

        text += "- Kristeva: metinlerarasılık, alıntılar mozaiğidir.\n"
        text += "- Bakhtin: söylem doğası gereği diyalojiktir.\n"

    # =========================
    # CITATIONS SECTION
    # =========================
    text += """

---

## 4. Kaynaklar ve Doğrulama
"""

    if isinstance(citations, list) and len(citations) > 0:

        for c in citations:

            if isinstance(c, dict):

                text += f"""
- {c.get('title','Unknown')}
  DOI: {c.get('doi','N/A')}
"""

    else:

        text += "Bu analizde otomatik doğrulanmış DOI tabanlı kaynak bulunmamaktadır.\n"

    # =========================
    # CONCLUSION
    # =========================
    text += """

---

## 5. Sonuç

Bu metin, kültürel hafıza, metaforik yapı ve sembolik dil üzerinden değerlendirildiğinde çok katmanlı bir poetik sistem üretmektedir. Metinlerarasılık, bu yapının temel analiz çerçevesini oluşturmaktadır.
"""

    return text
