"""
PDF Premium INTERACTIF - Elke Berr.
Dashboard visuel + Champs de saisie interactifs.
VERSION CORRIGÉE (fieldFlags='multiline').
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
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Premium_INTERACTIF.pdf"
PAGE_W, PAGE_H = landscape(A4)

class InteractiveTextField(Flowable):
    def __init__(self, width, height, name):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.name = name

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFillColor(colors.whitesmoke)
        canvas.setStrokeColor(colors.lightgrey)
        canvas.rect(0, 0, self.width, self.height, fill=1)
        
        form = canvas.acroForm
        form.textfield(
            name=self.name,
            tooltip="Cliquez pour écrire vos retours",
            x=0, y=0,
            width=self.width,
            height=self.height,
            borderStyle='solid',
            borderColor=colors.grey,
            fillColor=colors.whitesmoke,
            fieldFlags='multiline' # MULTILIGNE ICI
        )
        canvas.restoreState()

def build_premium_interactive():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()
    s_title = ParagraphStyle('S_Title', parent=styles['Title'], fontSize=32, spaceAfter=20, alignment=TA_CENTER)
    s_header = ParagraphStyle('S_Header', parent=styles['Heading2'], fontSize=18, spaceBefore=10, spaceAfter=10)
    
    elements = []

    # --- 1. COUVERTURE ---
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph("ELKE BERR", s_title))
    elements.append(Paragraph("DOSSIER DE VALIDATION INTERACTIF (PREMIUM)", ParagraphStyle('Sub', parent=s_title, fontSize=18, textColor=colors.grey)))
    elements.append(PageBreak())

    # --- 2. DASHBOARD ---
    elements.append(Paragraph("Dashboard de Validation", s_header))
    dash_data = [
        ["ID", "SECTION", "POINTS CLÉS", "STATUT (Cochez pour valider)"],
        ["01", "HERO", "Navigation, Logo", "[ ] Validé  [ ] À revoir"],
        ["02", "HÉRITAGE", "Portrait Pogba", "[ ] Validé  [ ] À revoir"],
        ["03", "COLLECTION", "Grille bijoux", "[ ] Validé  [ ] À revoir"],
        ["04", "PHILOSOPHIE", "3 colonnes", "[ ] Validé  [ ] À revoir"],
        ["05", "AUDACE", "Visuel Bague", "[ ] Validé  [ ] À revoir"],
        ["06", "FOOTER", "Mentions", "[ ] Validé  [ ] À revoir"]
    ]
    t_dash = Table(dash_data, colWidths=[1*cm, 4*cm, 10*cm, 8*cm], rowHeights=0.8*cm)
    t_dash.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BACKGROUND', (0,0), (-1,0), colors.black),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(t_dash)
    elements.append(PageBreak())

    # --- 3. SECTIONS ---
    SECTIONS = [
        {"id": "01", "title": "HERO & NAVIGATION", "file": "01_section_0px_perfect.png"},
        {"id": "02", "title": "HÉRITAGE", "file": "02_section_1080px_perfect.png"},
        {"id": "03", "title": "COLLECTION", "file": "03_section_2160px_perfect.png"},
        {"id": "04", "title": "PHILOSOPHIE", "file": "04_section_3240px_perfect.png"},
        {"id": "05", "title": "AUDACE", "file": "05_section_4320px_perfect.png"},
        {"id": "06", "title": "FOOTER", "file": "06_section_5400px_perfect.png"}
    ]

    for s in SECTIONS:
        elements.append(Paragraph(f"{s['id']}. {s['title']}", s_header))
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        if os.path.exists(img_path):
            img = Image(img_path, width=24*cm, height=9*cm, kind='proportional')
            elements.append(img)
        
        elements.append(Spacer(1, 0.5*cm))
        
        # Champs interactifs
        elements.append(Paragraph("<b>Commentaires détaillés du client :</b>", styles['Normal']))
        elements.append(InteractiveTextField(width=26*cm, height=3*cm, name=f"comm_{s['id']}"))
        elements.append(PageBreak())

    # --- 4. ANNEXE ---
    elements.append(Paragraph("ANNEXE - Vue d'ensemble", s_header))
    full_path = os.path.join(SCREENSHOTS_DIR, "00_FULL_PAGE_PERFECT.png")
    if os.path.exists(full_path):
        img_full = Image(full_path, width=12*cm, height=16*cm, kind='proportional')
        elements.append(img_full)

    doc.build(elements)
    print(f"PDF Premium Interactif genere : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_premium_interactive()
