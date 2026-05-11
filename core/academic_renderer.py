# core/academic_renderer.py

def render_academic_output(poem, result):

    intertext = result.get("intertext", [])

    citations = result.get("citations", [])

    rag = result.get("rag", [])


    text = f"""
# 📚 Akademik Analiz

## 1. Giriş

Bu şiir, metinlerarasılık kuramı çerçevesinde değerlendirildiğinde yalnız bireysel bir duygu aktarımı değil; tarihsel, kültürel ve ontolojik katmanlar içeren çok düzlemli bir söylem üretmektedir.

Julia Kristeva’nın metinlerarasılık yaklaşımına göre her metin, daha önceki söylemlerin dönüşümüyle oluşan bir anlam ağının parçasıdır.

---

## 2. Metinlerarasılık Analizi
"""

    for item in intertext:

        text += f"""
### {item['term']} Motifi

Bu motif, Türk şiir geleneğinde {item['type']} olarak değerlendirilmektedir. Metin içinde kullanılan bu unsur, doğrudan kültürel hafızaya referans verir ve anlamı genişleten bir sembolik yapı oluşturur.
"""

    text += """

---

## 3. Kuramsal Bağlam

Şiir, Bakhtin’in çok seslilik (polyphony) kavramı açısından değerlendirildiğinde farklı söylemsel katmanların bir arada bulunduğu bir yapı sergiler. Ayrıca Kristeva’nın “alıntılar mozaiği” yaklaşımı metnin yapısal temelini açıklar.

---

## 4. Sonuç

Bu şiir, sınır, özgürlük ve ontolojik açılım temaları üzerinden Türk dünyası poetik hafızasında yer alan kolektif bir bilinç alanını temsil eder.
"""

    return text
