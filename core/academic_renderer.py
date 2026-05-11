# core/academic_renderer.py

def render_academic_output(poem: str, result: dict):

    intertext = result.get("intertext", []) or []
    citations = result.get("citations", []) or []
    rag = result.get("rag", []) or []

    def safe_get(item, key, default="unknown"):
        if isinstance(item, dict):
            return item.get(key, default)
        return default

    text = f"""
# 📚 Akademik Analiz

## 1. Giriş

Bu metin, metinlerarasılık kuramı çerçevesinde değerlendirildiğinde çok katmanlı bir anlam yapısı üretmektedir. Kristeva’nın yaklaşımına göre her metin, önceki söylemlerin dönüşümüyle oluşan bir “alıntılar mozaiği”dir.

---

## 2. Metinlerarasılık Katmanı
"""

    # =========================
    # SAFE INTERTEXT LOOP
    # =========================
    if intertext:

        for item in intertext:

            term = safe_get(item, "term")
            typ = safe_get(item, "type", "motif")

            text += f"""
### {term}

Bu öğe metin içinde **{typ}** olarak işlev görmektedir. Türk şiir geleneğinde bu tür yapılar kültürel hafızayı aktive eden sembolik göstergeler olarak değerlendirilir.
"""

    else:

        text += """
Metin içinde belirgin intertextual öğe tespit edilememiştir; ancak şiirin yapısal düzeyi metaforik ve sembolik okumaya açıktır.
"""

    # =========================
    # RAG CONTEXT
    # =========================
    text += """

---

## 3. Kuramsal Arka Plan (RAG Destekli)

"""

    if rag:

        for r in rag[:5]:

            if isinstance(r, dict):
                text += f"- {r.get('text', '')}\n"

    else:

        text += "Kuramsal veri bulunamadı, genel edebi çerçeve kullanılmıştır.\n"

    # =========================
    # CITATIONS
    # =========================
    text += """

---

## 4. Kaynaklar ve Doğrulama

"""

    if citations:

        for c in citations:

            if isinstance(c, dict):

                text += f"""
- {c.get('title', 'Unknown')}
  DOI: {c.get('doi', 'N/A')}
"""

    else:

        text += "Doğrulanmış akademik kaynak tespit edilemedi.\n"

    # =========================
    # CONCLUSION
    # =========================
    text += """

---

## 5. Sonuç

Bu şiir, kültürel hafıza, metaforik sınır algısı ve sembolik dil yapısı üzerinden değerlendirildiğinde Türk dünyası edebiyatında çok katmanlı bir poetik yapı sunmaktadır.
"""

    return text
