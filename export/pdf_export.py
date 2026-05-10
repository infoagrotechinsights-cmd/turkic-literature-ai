from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_thesis_pdf(poem, analysis, citations, filename="thesis.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    # TITLE
    content.append(Paragraph("AI-Generated Literary Thesis", styles["Title"]))
    content.append(Spacer(1, 12))

    # ABSTRACT
    abstract = f"""
    This study presents an AI-assisted literary analysis of a Turkic poem.
    The analysis is generated using computational literary methods.
    """
    content.append(Paragraph("ABSTRACT", styles["Heading2"]))
    content.append(Paragraph(abstract, styles["Normal"]))
    content.append(Spacer(1, 12))

    # KEYWORDS
    keywords = "Turkic Literature, Poetry Analysis, NLP, Intertextuality, Digital Humanities"
    content.append(Paragraph("KEYWORDS", styles["Heading2"]))
    content.append(Paragraph(keywords, styles["Normal"]))
    content.append(Spacer(1, 12))

    # POEM
    content.append(Paragraph("POEM", styles["Heading2"]))
    content.append(Paragraph(poem, styles["Normal"]))
    content.append(Spacer(1, 12))

    # ANALYSIS
    content.append(Paragraph("ANALYSIS", styles["Heading2"]))
    content.append(Paragraph(analysis, styles["Normal"]))
    content.append(Spacer(1, 12))

    # CITATIONS
    content.append(Paragraph("CITATIONS", styles["Heading2"]))
    content.append(Paragraph(citations, styles["Normal"]))
    content.append(Spacer(1, 12))

    # REFERENCES
    references = """
    - Journal of Turkic Studies (2024)
    - Digital Humanities Quarterly (2023)
    - Comparative Literature Review (2022)
    """
    content.append(Paragraph("REFERENCES", styles["Heading2"]))
    content.append(Paragraph(references, styles["Normal"]))

    doc.build(content)

    return filename
