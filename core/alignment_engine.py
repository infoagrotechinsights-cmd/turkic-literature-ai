from core.llm_engine import ask_gpt


def align_poetry(text: str, mode: str = "academic"):
    """
    Multilingual Poetry Alignment Engine
    - Farsça / Azerice / Türkçe metni çözer
    - Türkçeye çevirir
    - akademik analiz üretir
    """

    prompt = f"""
Sen Türk akademik edebiyat uzmanısın.

GÖREVİN:
Aşağıdaki şiiri analiz et ve SADECE TÜRKÇE yaz.

ZORUNLU ADIMLAR:
1. Metni diline bakmadan Türkçeye çevir
2. Anlam katmanlarını çıkar
3. Şairin duygusal yapısını analiz et
4. Metinlerarasılık kur
5. Tarihsel / kültürel bağlam ver

EK KURALLAR:
- Azerice, Farsça, İngilizce KULLANMA
- sadece akademik Türkçe
- tez formatına uygun yaz

MOD: {mode}

ŞİİR:
{text}

ÇIKTI:
- Türkçe çeviri
- Tematik analiz
- Sembolik çözümleme
- Akademik yorum
"""

    return ask_gpt(prompt)
