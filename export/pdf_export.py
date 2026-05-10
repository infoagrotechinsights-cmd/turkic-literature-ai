# export/pdf_export.py

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from reportlab.platypus.tables import Table
from reportlab.platypus.tables import TableStyle

from reportlab.lib import colors


def create_thesis_pdf(
    filename,
    title,
    poem,
    analysis,
    citations
):

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # =========================
    # TITLE
    # =========================

    elements.append(
        Paragraph(
            f"<b>{title}</b>",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # =========================
    # ABSTRACT
    # =========================

    abstract = """
    This study examines the poem through
    intertextual, ontological and
    comparative Turkic literature approaches.
    """

    elements.append(
        Paragraph(
            "<b>Abstract</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            abstract,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # =========================
    # POEM
    # =========================

    elements.append(
        Paragraph(
            "<b>Poem</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            poem.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # =========================
    # ANALYSIS
    # =========================

    elements.append(
        Paragraph(
            "<b>Academic Analysis</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            analysis.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # =========================
    # REFERENCES
    # =========================

    elements.append(
        Paragraph(
            "<b>References (APA 7)</b>",
            styles["Heading2"]
        )
    )

    for src in citations:

        apa = src.get("apa", "")

        elements.append(
            Paragraph(
                apa,
                styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 8))

    # =========================
    # BUILD PDF
    # =========================

    doc.build(elements)

    return filename
