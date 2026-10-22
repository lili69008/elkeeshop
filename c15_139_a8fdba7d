"""
PDF Ultra-Premium de Revue - Elke Berr.
Inclus : Filigrane, Index Visuel Interactif, Dashboard et Annexes HD.
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak, PageTemplate, Frame
)
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
import os
from datetime import datetime
from PIL import Image as PILImage

# ---- CONFIG ----
SCREENSHOTS_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Dossier_Validation_Final.pdf"
PAGE_W, PAGE_H = landscape(A4)
WATERMARK_TEXT = "CONFIDENTIEL - ELKE BERR"

SECTIONS = [
    {"id": "01", "title": "HERO & NAVIGATION", "file": "01_section_0px_perfect.png", "desc": "En-tete et Accroche principale."},
    {"id": "02", "title": "HÉRITAGE (LA MAISON)", "file": "02_section_1080px_perfect.png", "desc": "Section Storytelling."},
    {"id": "03", "title": "COLLECTION UNBREAKABLE", "file": "03_section_2160px_perfect.png", "desc": "Collaboration Zulay & Pogba."},
    {"id": "04", "title": "PHILOSOPHIE & TRANSMISSION", "file": "04_section_3240px_perfect.png", "desc": "Valeurs et Vision."},
    {"id": "05", "title": "AUDACE CRÉATIVE", "file": "05_section_4320px_perfect.png", "desc": "Mise en avant Pieces Uniques."},
    {"id": "06", "title": "FOOTER & CONTACT", "file": "06_section_5400px_perfect.png", "desc": "Pied de page et Coordonnees."}
]

def on_page(canvas, doc):
    canvas.saveState()
    # --- FILIGRANE ---
    canvas.setFont('Helvetica-Bold', 60)
    canvas.setStrokeColor(colors.lightgrey)
    canvas.setFillAlpha(0.1)
    canvas.translate(PAGE_W/2, PAGE_H/2)
    canvas.rotate(45)
    canvas.drawCentredString(0, 0, WATERMARK_TEXT)
    
    # --- BAS DE PAGE ---
    canvas.restoreState()
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(PAGE_W - 1*cm, 0.5*cm, f"Page {doc.page} | {datetime.now().strftime('%d/%m/%Y')}")

def build_final_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()

    # Styles
    s_title = ParagraphStyle('S_Title', parent=styles['Title'], fontSize=34, spaceAfter=20, alignment=TA_CENTER)
    s_header = ParagraphStyle('S_Header', parent=styles['Heading2'], fontSize=18, spaceBefore=10, spaceAfter=10)
    s_toc = ParagraphStyle('S_TOC', parent=styles['Normal'], fontSize=12, leading=16)
    
    elements = []

    # --- 1. COUVERTURE ---
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph("ELKE BERR", s_title))
    elements.append(Paragraph("DOSSIER DE VALIDATION FINAL", ParagraphStyle('Sub', parent=s_title, fontSize=18, textColor=colors.grey)))
    elements.append(Spacer(1, 4*cm))
    
    info_data = [
        [Paragraph(f"<b>{WATERMARK_TEXT}</b>", ParagraphStyle('W', parent=styles['Normal'], textColor=colors.red))],
        [f"Genere le : {datetime.now().strftime('%d/%m/%Y %H:%M')}"],
        ["Document de reference pour validation contractuelle."]
    ]
    t_info = Table(info_data, colWidths=[15*cm])
    elements.append(t_info)
    elements.append(PageBreak())

    # --- 2. INDEX VISUEL INTERACTIF ---
    elements.append(Paragraph("Index Visuel Interactif", s_header))
    elements.append(Spacer(1, 0.5*cm))
    
    index_data = []
    current_row = []
    for i, s in enumerate(SECTIONS):
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        img_w, img_h = 4*cm, 2.2*cm
        if os.path.exists(img_path):
            img_thumb = Image(img_path, width=img_w, height=img_h)
            # Lien interne vers le bookmark de la section
            cell = [img_thumb, Paragraph(f"<link destination='S{s['id']}'>{s['title']}</link>", styles['Normal'])]
            current_row.append(cell)
        
        if len(current_row) == 3 or i == len(SECTIONS)-1:
            index_data.append(current_row)
            current_row = []

    t_index = Table(index_data, colWidths=[8*cm, 8*cm, 8*cm], rowHeights=4*cm)
    t_index.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.1, colors.lightgrey)
    ]))
    elements.append(t_index)
    elements.append(PageBreak())

    # --- 3. SECTIONS ---
    for s in SECTIONS:
        # Bookmark pour l'index
        elements.append(Paragraph(f"<a name='S{s['id']}'/>", styles['Normal']))
        elements.append(Paragraph(f"Section {s['id']} : {s['title']}", s_header))
        
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        if os.path.exists(img_path):
            img = Image(img_path, width=24*cm, height=10*cm, kind='proportional')
            elements.append(img)
        
        elements.append(Spacer(1, 0.5*cm))
        
        # Table de retour
        ret_data = [
            ["ELEMENTS ANALYSES", "COMMENTAIRES DU CLIENT", "STATUT"],
            ["Layout & Structure", "", ""],
            ["Textes & Typographies", "", ""],
            ["Visuels & Medias", "", ""],
            ["Interactions & Flux", "", ""]
        ]
        t_ret = Table(ret_data, colWidths=[6*cm, 16*cm, 4*cm], rowHeights=[0.7*cm, 1.2*cm, 1.2*cm, 1.2*cm, 1.2*cm])
        t_ret.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1a1a1a")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
        ]))
        elements.append(t_ret)
        elements.append(PageBreak())

    # --- 4. ANNEXE FULL PAGE ---
    elements.append(Paragraph("ANNEXE - Capture Integrale (Haute Resolution)", s_header))
    full_path = os.path.join(SCREENSHOTS_DIR, "00_FULL_PAGE_PERFECT.png")
    if os.path.exists(full_path):
        img_full = Image(full_path, width=12*cm, height=16*cm, kind='proportional')
        elements.append(img_full)

    # Build with watermark hook
    doc.build(elements, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF Final genere : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_final_pdf()
