from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_thesis_pdf(poem: str, analysis: str, citations: str):

    file_path = "thesis_output.pdf"
    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    # =========================
    # 📘 TITLE
    # =========================
    story.append(Paragraph("Turkic Literature AI – Thesis Report", styles["Title"]))
    story.append(Spacer(1, 12))

    # =========================
    # 📜 POEM
    # =========================
    story.append(Paragraph("<b>Şiir:</b>", styles["Heading2"]))
    story.append(Paragraph(poem, styles["Normal"]))
    story.append(Spacer(1, 12))

    # =========================
    # 🧠 ANALYSIS
    # =========================
    story.append(Paragraph("<b>Akademik Analiz:</b>", styles["Heading2"]))
    story.append(Paragraph(analysis, styles["Normal"]))
    story.append(Spacer(1, 12))

    # =========================
    # 📚 CITATIONS
    # =========================
    story.append(Paragraph("<b>Kaynakça:</b>", styles["Heading2"]))
    story.append(Paragraph(str(citations), styles["Normal"]))

    doc.build(story)

    return file_path
