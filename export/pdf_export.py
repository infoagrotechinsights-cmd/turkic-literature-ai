from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_journal_pdf(title, abstract, analysis, citations):

    file_path = "academic_paper.pdf"
    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(title, styles["Title"]))
    story.append(Paragraph("Abstract: " + abstract, styles["Normal"]))
    story.append(Paragraph("Analysis: " + analysis, styles["Normal"]))
    story.append(Paragraph("References: " + str(citations), styles["Normal"]))

    doc.build(story)

    return file_path
