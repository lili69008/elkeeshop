"""
PDF Interactif Suisse - Elke Berr.
Inclus des champs de texte saisissables (Formulaires PDF) pour le client.
VERSION CORRIGÉE (acroForm).
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak, Flowable
)
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
import os
from datetime import datetime

# ---- CONFIG ----
SCREENSHOTS_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Revue_INTERACTIVE_Suisse.pdf"
PAGE_W, PAGE_H = landscape(A4)

class InteractiveTextField(Flowable):
    """Un champ de formulaire PDF saisissable."""
    def __init__(self, width, height, name):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.name = name

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        
        # Fond leger pour montrer que c'est une zone saisissable
        canvas.setFillColor(colors.HexColor("#F9F9F9"))
        canvas.setStrokeColor(colors.lightgrey)
        canvas.rect(0, 0, self.width, self.height, fill=1)
        
        # Creation du champ de texte interactif (AcroForm)
        form = canvas.acroForm
        form.textfield(
            name=self.name,
            tooltip="Tapez vos retours ici",
            x=self.canv._x, y=self.canv._y, # On utilise les coordonnees du canvas
            width=self.width,
            height=self.height,
            borderStyle='underlined',
            borderColor=colors.grey,
            fillColor=colors.whitesmoke,
            textColor=colors.black,
            fontSize=10,
            annotationFlags='print'
        )
        canvas.restoreState()

def on_page_interactive(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7)
    canvas.drawString(1*cm, 0.8*cm, "DOCUMENT INTERACTIF - Cliquez dans les zones grises pour écrire vos commentaires.")
    canvas.drawRightString(PAGE_W - 1*cm, 0.8*cm, f"Genève | {datetime.now().strftime('%d/%m/%Y')}")
    canvas.restoreState()

def build_interactive_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()
    s_h1 = ParagraphStyle('S_H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18)
    s_body = ParagraphStyle('S_Body', parent=styles['Normal'], fontSize=10)

    elements = []

    # --- COUVERTURE ---
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph("ELKE BERR - DOSSIER INTERACTIF", ParagraphStyle('T', parent=styles['Title'], fontSize=28)))
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph("Ce document est dynamique. Vous pouvez taper vos retours directement dans les cadres prévus.", s_body))
    elements.append(PageBreak())

    # --- SECTIONS ---
    SECTIONS = [
        {"id": "01", "title": "HERO & NAVIGATION", "file": "01_section_0px_perfect.png"},
        {"id": "02", "title": "HÉRITAGE", "file": "02_section_1080px_perfect.png"},
        {"id": "03", "title": "COLLECTIONS", "file": "03_section_2160px_perfect.png"},
        {"id": "04", "title": "PHILOSOPHIE", "file": "04_section_3240px_perfect.png"},
        {"id": "05", "title": "AUDACE", "file": "05_section_4320px_perfect.png"},
        {"id": "06", "title": "FOOTER", "file": "06_section_5400px_perfect.png"}
    ]

    for s in SECTIONS:
        elements.append(Paragraph(f"{s['id']}. {s['title']}", s_h1))
        
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        if os.path.exists(img_path):
            img = Image(img_path, width=24*cm, height=10*cm, kind='proportional')
            elements.append(img)
        
        elements.append(Spacer(1, 0.5*cm))
        
        # On ajoute les zones saisissables
        elements.append(Paragraph("<b>Vos retours sur le Design et l'UI :</b>", s_body))
        elements.append(InteractiveTextField(width=26*cm, height=2*cm, name=f"design_{s['id']}"))
        elements.append(Spacer(1, 0.3*cm))
        
        elements.append(Paragraph("<b>Vos retours sur les Textes et le Contenu :</b>", s_body))
        elements.append(InteractiveTextField(width=26*cm, height=2*cm, name=f"content_{s['id']}"))
        
        elements.append(PageBreak())

    doc.build(elements, onFirstPage=on_page_interactive, onLaterPages=on_page_interactive)
    print(f"PDF Interactif genere : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_interactive_pdf()
