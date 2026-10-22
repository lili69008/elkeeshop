"""
PDF Premium de Revue - Elke Berr.
Structure amelioree, dashboard global et captures parfaites.
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak
)
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
import os
from datetime import datetime

# ---- CONFIG ----
SCREENSHOTS_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Dossier_Validation_Premium.pdf"
PAGE_W, PAGE_H = landscape(A4)

# Definition des sections precises
SECTIONS = [
    {
        "id": "01",
        "title": "HERO & NAVIGATION",
        "file": "01_section_0px_perfect.png",
        "desc": "En-tete, Navigation, Logo et Accroche principale.",
        "points": ["Logo central", "Navigation fluide", "Visuel Bague Saphir", "CTA Heritage"]
    },
    {
        "id": "02",
        "title": "HÉRITAGE (LA MAISON)",
        "file": "02_section_1080px_perfect.png",
        "desc": "Section Storytelling et Savoir-faire.",
        "points": ["Portrait Paul Pogba", "Texte Gemmologue", "Typographie Serife", "Equilibre visuel"]
    },
    {
        "id": "03",
        "title": "COLLECTION UNBREAKABLE",
        "file": "03_section_2160px_perfect.png",
        "desc": "Focus sur la collaboration Zulay & Paul Pogba.",
        "points": ["Grille de 3 bijoux", "Prix et Noms", "Visuel Bracelet", "Bouton Explorer"]
    },
    {
        "id": "04",
        "title": "PHILOSOPHIE & TRANSMISSION",
        "file": "04_section_3240px_perfect.png",
        "desc": "Valeurs de la marque et texte philosophique.",
        "points": ["Art de faconner le temps", "3 colonnes de texte", "Lisibilite sur fond sombre"]
    },
    {
        "id": "05",
        "title": "AUDACE CRÉATIVE",
        "file": "05_section_4320px_perfect.png",
        "desc": "Mise en avant des pieces uniques.",
        "points": ["Visuel Bague large", "Titre Audace Creative", "Texte de droite", "Lien Creations"]
    },
    {
        "id": "06",
        "title": "FOOTER & CONTACT",
        "file": "06_section_5400px_perfect.png",
        "desc": "Pied de page, plans et reseaux.",
        "points": ["Mentions legales", "Coordonnees", "Liens rapides", "Copyright"]
    }
]

def build_premium_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()

    # Styles personnalises
    s_title = ParagraphStyle('S_Title', parent=styles['Title'], fontSize=32, spaceAfter=20, alignment=TA_CENTER)
    s_header = ParagraphStyle('S_Header', parent=styles['Heading2'], fontSize=18, spaceBefore=10, spaceAfter=10, textColor=colors.HexColor("#333"))
    s_normal = ParagraphStyle('S_Normal', parent=styles['Normal'], fontSize=10)
    
    elements = []

    # --- PAGE DE GARDE ---
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph("ELKE BERR", s_title))
    elements.append(Paragraph("DOSSIER DE VALIDATION SITE WEB V2", ParagraphStyle('Sub', parent=s_title, fontSize=18, textColor=colors.grey)))
    elements.append(Spacer(1, 2*cm))
    
    info_data = [
        ["Client :", "Elke Berr Creations"],
        ["Date :", datetime.now().strftime('%d/%m/%Y')],
        ["Version :", "V2.1 - Revue de Detail"],
        ["Format :", "Screenshots HD (1920x1080)"],
        ["Statut :", "A VALIDER"]
    ]
    t_info = Table(info_data, colWidths=[4*cm, 10*cm])
    t_info.setStyle(TableStyle([('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('ALIGN', (0,0), (-1,-1), 'LEFT')]))
    elements.append(t_info)
    elements.append(PageBreak())

    # --- DASHBOARD RÉSUMÉ ---
    elements.append(Paragraph("Dashboard de Validation", s_header))
    elements.append(Spacer(1, 0.5*cm))
    
    dash_data = [["ID", "SECTION", "POINTS CLÉS", "STATUT DE VALIDATION"]]
    for s in SECTIONS:
        dash_data.append([s["id"], s["title"], ", ".join(s["points"][:2]) + "...", "[ ] Validé  [ ] À revoir"])
    
    t_dash = Table(dash_data, colWidths=[1*cm, 6*cm, 12*cm, 6*cm], rowHeights=1*cm)
    t_dash.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BACKGROUND', (0,0), (-1,0), colors.black),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 9)
    ]))
    elements.append(t_dash)
    elements.append(PageBreak())

    # --- PAGES DE DÉTAIL ---
    for s in SECTIONS:
        elements.append(Paragraph(f"{s['id']}. {s['title']}", s_header))
        elements.append(Paragraph(s['desc'], s_normal))
        elements.append(Spacer(1, 0.3*cm))
        
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        if os.path.exists(img_path):
            # Calcul taille optimale (image large)
            img = Image(img_path, width=22*cm, height=11*cm, kind='proportional')
            elements.append(img)
        
        elements.append(Spacer(1, 0.5*cm))
        
        # Tableau de commentaires detaille
        comm_data = [
            ["CATÉGORIE", "ANALYSE / RETOURS DÉTAILLÉS", "NOTE (1-5)"],
            ["Structure & Mise en page", "", ""],
            ["Typographies & Textes", "", ""],
            ["Qualité des images", "", ""],
            ["Animations & Rythme", "", ""]
        ]
        t_comm = Table(comm_data, colWidths=[5*cm, 18*cm, 3*cm], rowHeights=[0.7*cm, 1*cm, 1*cm, 1*cm, 1*cm])
        t_comm.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('FONTSIZE', (0,0), (-1,-1), 8)
        ]))
        elements.append(t_comm)
        elements.append(PageBreak())

    # --- ANNEXE : FULL PAGE ---
    elements.append(Paragraph("ANNEXE - Vue d'ensemble (Scroll Intégral)", s_header))
    full_path = os.path.join(SCREENSHOTS_DIR, "00_FULL_PAGE_PERFECT.png")
    if os.path.exists(full_path):
        # On met le scroll complet en miniature lisible sur une page
        img_full = Image(full_path, width=15*cm, height=16*cm, kind='proportional')
        elements.append(img_full)
    
    doc.build(elements)
    print(f"PDF Premium genere : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_premium_pdf()
