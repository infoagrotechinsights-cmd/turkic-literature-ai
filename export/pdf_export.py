from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_thesis_pdf(thesis, filename="thesis.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph(thesis["title"], styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Abstract", styles["Heading2"]))
    content.append(Paragraph(thesis["abstract"], styles["BodyText"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Introduction", styles["Heading2"]))
    content.append(Paragraph(thesis["introduction"], styles["BodyText"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Analysis", styles["Heading2"]))
    content.append(Paragraph(str(thesis["analysis"]), styles["BodyText"]))

    doc.build(content)

    return filename
