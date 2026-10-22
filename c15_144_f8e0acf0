"""
PDF Suisse INTERACTIF - Elke Berr.
Meme design que la version Suisse, mais avec des champs de saisie dans les tableaux.
VERSION CORRIGÉE : Suppression de "ton de voix".
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
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Revue_Qualite_Suisse_INTERACTIF.pdf"
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
        form = canvas.acroForm
        form.textfield(
            name=self.name,
            tooltip="Saisissez vos retours ici",
            x=0, y=0,
            width=self.width,
            height=self.height,
            borderStyle='solid',
            borderColor=colors.lightgrey,
            fillColor=colors.whitesmoke,
            fieldFlags='multiline'
        )
        canvas.restoreState()

def on_page_clean(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7)
    canvas.setStrokeColor(colors.lightgrey)
    canvas.line(1*cm, 1.2*cm, PAGE_W - 1*cm, 1.2*cm)
    canvas.drawString(1*cm, 0.8*cm, "Elke Berr - Revue de Qualité INTERACTIVE")
    canvas.drawRightString(PAGE_W - 1*cm, 0.8*cm, f"Genève | {datetime.now().strftime('%d/%m/%Y')}")
    canvas.restoreState()

def build_swiss_interactive_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()
    s_title = ParagraphStyle('S_Title', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=28, alignment=TA_CENTER)
    s_h1 = ParagraphStyle('S_H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18)
    s_body = ParagraphStyle('S_Body', parent=styles['Normal'], fontSize=10)
    
    elements = []

    # --- COUVERTURE ---
    elements.append(Spacer(1, 4*cm))
    elements.append(Paragraph("ELKE BERR CREATIONS", s_title))
    elements.append(Paragraph("RAPPORT DE VALIDATION INTERACTIF", ParagraphStyle('Sub', parent=s_title, fontSize=12, textColor=colors.grey)))
    elements.append(Spacer(1, 3*cm))
    cover_data = [["DATE DU RAPPORT", datetime.now().strftime('%d %B %Y')], ["LIEU", "Genève, Suisse"], ["STATUT", "A SAISIR PAR LE CLIENT"]]
    t_cover = Table(cover_data, colWidths=[6*cm, 10*cm])
    elements.append(t_cover)
    elements.append(PageBreak())

    # --- SECTIONS ---
    SECTIONS = [
        {"id": "01", "title": "HERO & IDENTITY", "file": "01_section_0px_perfect.png"},
        {"id": "02", "title": "STORYTELLING", "file": "02_section_1080px_perfect.png"},
        {"id": "03", "title": "COLLECTIONS", "file": "03_section_2160px_perfect.png"},
        {"id": "04", "title": "PHILOSOPHY", "file": "04_section_3240px_perfect.png"},
        {"id": "05", "title": "CREATIVE AUDACITY", "file": "05_section_4320px_perfect.png"},
        {"id": "06", "title": "FOOTER & LEGAL", "file": "06_section_5400px_perfect.png"}
    ]

    for s in SECTIONS:
        elements.append(Paragraph(f"{s['id']}. {s['title']}", s_h1))
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        if os.path.exists(img_path):
            img = Image(img_path, width=24*cm, height=10*cm, kind='proportional')
            elements.append(img)
        elements.append(Spacer(1, 0.5*cm))
        
        # TABLEAU IDENTIQUE MAIS SANS "TON DE VOIX"
        fb_data = [
            ["CATÉGORIE", "ANALYSE TECHNIQUE ET VISUELLE", "RETOUR CLIENT (Saisissable)"],
            ["DESIGN & UI", "Respect de la charte, alignements, contrastes.", InteractiveTextField(12*cm, 1.5*cm, f"ui_{s['id']}")],
            ["CONTENU", "Typographie, orthographe, rédactionnel.", InteractiveTextField(12*cm, 1.5*cm, f"cont_{s['id']}")],
            ["TECH / UX", "Vitesse d'affichage, animations, liens.", InteractiveTextField(12*cm, 1.5*cm, f"tech_{s['id']}")]
        ]
        t_fb = Table(fb_data, colWidths=[4*cm, 9*cm, 13*cm], rowHeights=[0.7*cm, 1.8*cm, 1.8*cm, 1.8*cm])
        t_fb.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.3, colors.lightgrey),
            ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('FONTSIZE', (0,0), (-1,-1), 8)
        ]))
        elements.append(t_fb)
        elements.append(PageBreak())

    # --- ANNEXE ---
    elements.append(Paragraph("Annexe A : Vue d'ensemble du Site", s_h1))
    full_path = os.path.join(SCREENSHOTS_DIR, "00_FULL_PAGE_PERFECT.png")
    if os.path.exists(full_path):
        img_full = Image(full_path, width=13*cm, height=16*cm, kind='proportional')
        elements.append(img_full)
    
    doc.build(elements, onFirstPage=on_page_clean, onLaterPages=on_page_clean)
    print(f"PDF Suisse Interactif (Cleaned Content) genere : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_swiss_interactive_pdf()
