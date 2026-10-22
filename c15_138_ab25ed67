"""
PDF professionnel avec captures reelles HD du site Elke Berr.
Chaque section a son screenshot + tableau de commentaires detaille.
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os
from PIL import Image as PILImage
from datetime import datetime

# ---- CONFIG ----
SCREENSHOTS_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Revue_Complete.pdf"
PAGE_W, PAGE_H = landscape(A4)  # landscape for wider screenshots

SECTIONS = [
    {
        "file": "01_section_0px.png",
        "title": "01. Hero - Accueil",
        "desc": "Navigation principale, Logo Elke Berr, Image d'accroche plein ecran, Titre + sous-titre, CTA 'Decouvrir notre heritage'.",
        "details": [
            "Navigation : LA MAISON | HAUTE JOAILLERIE | ELKE BERR | UNBREAKABLE | BESPOKE",
            "Baseline : Geneve - Depuis 2003",
            "Accroche : 'La ou la pierre dicte l'oeuvre.'",
            "Visuel : Bague saphir bleu, fond gris",
        ]
    },
    {
        "file": "02_section_1080px.png",
        "title": "02. La Maison - Heritage",
        "desc": "Section dediee a l'histoire et au savoir-faire de la maison.",
        "details": [
            "Layout 2 colonnes : image a gauche, texte a droite",
            "Titre de section : 'L'heritage Elke Berr'",
            "Texte de presentation et philosophie",
            "Image immersive d'atelier ou de creation",
        ]
    },
    {
        "file": "03_section_2160px.png",
        "title": "03. Haute Joaillerie - Collections",
        "desc": "Presentation des collections et pieces d'exception.",
        "details": [
            "Grille de produits ou mise en avant",
            "Titres des collections",
            "Visuels haute qualite des bijoux",
            "Eventuels boutons 'Decouvrir'",
        ]
    },
    {
        "file": "04_section_3240px.png",
        "title": "04. Unbreakable - Collaboration",
        "desc": "Section dediee a la collection Unbreakable (Zulay & Paul Pogba).",
        "details": [
            "Portraits des ambassadeurs",
            "Nom de la collection 'UNBREAKABLE'",
            "Description de la collaboration",
            "Visuels des pieces de la collection",
        ]
    },
    {
        "file": "05_section_4320px.png",
        "title": "05. Bespoke - Sur-mesure",
        "desc": "Philosophie Bespoke et processus de creation personnalisee.",
        "details": [
            "Titre 'Bespoke' ou 'Philosophie'",
            "Description du processus sur-mesure",
            "Visuels d'etapes ou de pierres",
            "Eventuel CTA de prise de contact",
        ]
    },
    {
        "file": "06_section_5400px.png",
        "title": "06. Footer & Contact",
        "desc": "Pied de page, coordonnees, reseaux sociaux, mentions legales.",
        "details": [
            "Coordonnees et adresse (Geneve)",
            "Liens reseaux sociaux",
            "Newsletter / inscription",
            "Mentions legales et copyright",
        ]
    },
]


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1.5*cm,
        rightMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
    )
    styles = getSampleStyleSheet()

    # Custom styles
    title_main = ParagraphStyle('TitleMain', parent=styles['Title'],
                                fontSize=28, alignment=TA_CENTER, spaceAfter=10)
    subtitle = ParagraphStyle('Subtitle', parent=styles['Normal'],
                              fontSize=14, alignment=TA_CENTER, textColor=colors.grey)
    section_title = ParagraphStyle('SectionTitle', parent=styles['Heading1'],
                                   fontSize=20, spaceBefore=5, spaceAfter=5,
                                   textColor=colors.HexColor("#1a1a1a"))
    section_desc = ParagraphStyle('SectionDesc', parent=styles['Normal'],
                                  fontSize=11, spaceAfter=5, textColor=colors.HexColor("#555"))
    detail_style = ParagraphStyle('Detail', parent=styles['Normal'],
                                  fontSize=9, textColor=colors.HexColor("#333"),
                                  bulletIndent=10, leftIndent=15)
    
    elements = []

    # ========== COVER PAGE ==========
    elements.append(Spacer(1, 4*cm))
    elements.append(Paragraph("ELKE BERR", title_main))
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph("Revue Complete du Site Web - ecran par ecran", subtitle))
    elements.append(Spacer(1, 1*cm))
    elements.append(Paragraph(f"Date de generation : {datetime.now().strftime('%d/%m/%Y')}", subtitle))
    elements.append(Paragraph("URL : https://elke-berr-v2-feedback.netlify.app/", subtitle))
    elements.append(Spacer(1, 2*cm))
    
    # Cover table of contents
    toc_data = [["N.", "Section", "Description"]]
    for s in SECTIONS:
        toc_data.append([s["title"][:3], s["title"][4:], s["desc"][:60] + "..."])
    
    toc_table = Table(toc_data, colWidths=[2*cm, 8*cm, 14*cm])
    toc_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.3, colors.lightgrey),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1a1a1a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f9f9f9")]),
    ]))
    elements.append(toc_table)
    elements.append(PageBreak())

    # ========== SECTION PAGES ==========
    usable_w = PAGE_W - 3*cm  # ~26.7cm in landscape A4

    for section in SECTIONS:
        img_path = os.path.join(SCREENSHOTS_DIR, section["file"])

        # --- Section Header ---
        elements.append(Paragraph(section["title"], section_title))
        elements.append(Paragraph(section["desc"], section_desc))
        elements.append(Spacer(1, 0.3*cm))

        # --- Screenshot ---
        if os.path.exists(img_path):
            pil_img = PILImage.open(img_path)
            iw, ih = pil_img.size
            ratio = ih / iw
            display_w = usable_w
            display_h = display_w * ratio
            max_h = 11 * cm  # Keep room for comment table
            if display_h > max_h:
                display_h = max_h
                display_w = display_h / ratio
            img = Image(img_path, width=display_w, height=display_h)
            elements.append(img)
        else:
            elements.append(Paragraph(f"[IMAGE MANQUANTE : {section['file']}]", styles['Normal']))

        elements.append(Spacer(1, 0.3*cm))

        # --- Detail list ---
        for d in section["details"]:
            elements.append(Paragraph(f"- {d}", detail_style))

        elements.append(Spacer(1, 0.3*cm))

        # --- Comment Table ---
        comment_data = [
            [
                Paragraph("<b>CATEGORIE</b>", styles['Normal']),
                Paragraph("<b>COMMENTAIRE DU CLIENT</b>", styles['Normal']),
                Paragraph("<b>PRIORITE</b>", styles['Normal']),
                Paragraph("<b>VALIDE</b>", styles['Normal']),
            ],
            ["Structure / Layout", "", "", ""],
            ["Contenu / Textes", "", "", ""],
            ["Design / Couleurs", "", "", ""],
            ["Images / Visuels", "", "", ""],
            ["Animations / Interactions", "", "", ""],
            ["Responsive / Mobile", "", "", ""],
            ["Autres remarques", "", "", ""],
        ]
        ct = Table(comment_data, colWidths=[5*cm, 14*cm, 3.5*cm, 2.5*cm],
                   rowHeights=[0.7*cm] + [1*cm]*7)
        ct.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e8e8e8")),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('ALIGN', (2,0), (3,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        elements.append(ct)
        elements.append(PageBreak())

    # ========== FULL PAGE (bonus) ==========
    full_path = os.path.join(SCREENSHOTS_DIR, "00_FULL_PAGE.png")
    if os.path.exists(full_path):
        elements.append(Paragraph("ANNEXE - Vue complete du site (scroll integral)", section_title))
        elements.append(Spacer(1, 0.5*cm))
        pil_img = PILImage.open(full_path)
        iw, ih = pil_img.size
        ratio = ih / iw
        display_w = 12*cm
        display_h = display_w * ratio
        max_h = 16*cm
        if display_h > max_h:
            display_h = max_h
            display_w = display_h / ratio
        img = Image(full_path, width=display_w, height=display_h)
        elements.append(img)

    doc.build(elements)
    print(f"PDF genere : {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
