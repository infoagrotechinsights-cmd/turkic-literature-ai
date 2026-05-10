# core/analysis_engine.py


def generate_academic_analysis(poem: str, intertexts: list):

    intro = """
# Akademik Analiz

Bu şiir, metinlerarasılık kuramı bağlamında değerlendirildiğinde yalnız bireysel bir duygu aktarımı değil; aynı zamanda kültürel hafıza, tarihsel aidiyet ve poetik bilinç katmanları üreten çok yönlü bir söylem alanı oluşturmaktadır.

Julia Kristeva'nın ortaya koyduğu metinlerarasılık yaklaşımına göre her metin, başka metinlerin dönüştürülmesiyle oluşan bir “alıntılar mozaiği”dir. Bu bağlamda şiirde kullanılan imgeler, Türk şiir geleneğiyle doğrudan ilişki kurmaktadır.
"""

    body = ""

    for item in intertexts:

        body += f"""

## {item['keyword'].upper()} İMGESİ

Şiirde geçen “{item['keyword']}” kavramı, {item['tradition']} içerisinde değerlendirilebilecek önemli bir sembolik katman oluşturmaktadır.

Bu imge metin içerisinde:
- {item['meaning']}

anlam alanları üretmektedir.

Metinlerarası bağlamda şiir:
{", ".join(item['related_authors'])}

gibi isimlerin poetik geleneğiyle ilişki kurmaktadır.

Kuramsal açıdan bu kullanım:
{item['theory']}

çerçevesinde değerlendirilebilir.

Akademik Değerlendirme:
{item['academic_note']}
"""

    conclusion = """

# Sonuç

Sonuç olarak şiir; sınır, aidiyet, ontolojik özgürlük ve kültürel hafıza kavramlarını aynı poetik yapı içerisinde birleştiren çok katmanlı bir metin görünümündedir.

Şiirde kullanılan imgeler yalnız estetik unsurlar değil; aynı zamanda tarihsel bilinç ve kolektif hafızanın taşıyıcılarıdır. Bu yönüyle metin, klasik Türk şiiri, tasavvuf geleneği ve modern Türk dünyası şiiri arasında güçlü bir metinlerarası ilişki ağı kurmaktadır.
"""

    return intro + body + conclusion
