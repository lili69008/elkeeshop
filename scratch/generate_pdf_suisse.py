"""
PDF Suisse-Standard - Elke Berr.
Élégance, Précision et Sobriété. 
Suppression du filigrane, ajout de sections techniques (SEO, Perf, Légal).
"""
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak
)
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os
from datetime import datetime

# ---- CONFIG ----
SCREENSHOTS_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Revue_Qualite_Suisse.pdf"
PAGE_W, PAGE_H = landscape(A4)

# Definition des sections
SECTIONS = [
    {"id": "01", "title": "HERO & IDENTITY", "file": "01_section_0px_perfect.png", "desc": "Première impression et navigation."},
    {"id": "02", "title": "STORYTELLING", "file": "02_section_1080px_perfect.png", "desc": "Héritage et Savoir-faire."},
    {"id": "03", "title": "COLLECTIONS", "file": "03_section_2160px_perfect.png", "desc": "Présentation des produits."},
    {"id": "04", "title": "PHILOSOPHY", "file": "04_section_3240px_perfect.png", "desc": "Vision de la Maison."},
    {"id": "05", "title": "CREATIVE AUDACITY", "file": "05_section_4320px_perfect.png", "desc": "Pièces d'exception."},
    {"id": "06", "title": "FOOTER & LEGAL", "file": "06_section_5400px_perfect.png", "desc": "Coordonnées et mentions légales."}
]

def on_page_clean(canvas, doc):
    canvas.saveState()
    # Bas de page sobre
    canvas.setFont('Helvetica', 7)
    canvas.setStrokeColor(colors.lightgrey)
    canvas.line(1*cm, 1.2*cm, PAGE_W - 1*cm, 1.2*cm)
    canvas.drawString(1*cm, 0.8*cm, "Elke Berr - Revue de Qualité et Validation Site Web")
    canvas.drawRightString(PAGE_W - 1*cm, 0.8*cm, f"Page {doc.page} | Genéve, {datetime.now().strftime('%d/%m/%Y')}")
    canvas.restoreState()

def build_swiss_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()

    # Styles Suisses (Helvetica, Clean)
    s_title = ParagraphStyle('S_Title', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=28, spaceAfter=20, alignment=TA_CENTER)
    s_h1 = ParagraphStyle('S_H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, spaceBefore=20, spaceAfter=15)
    s_h2 = ParagraphStyle('S_H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14, spaceBefore=10, spaceAfter=10)
    s_body = ParagraphStyle('S_Body', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14)
    
    elements = []

    # --- 1. COUVERTURE (Design Minimaliste) ---
    elements.append(Spacer(1, 4*cm))
    elements.append(Paragraph("ELKE BERR CREATIONS", s_title))
    elements.append(Paragraph("RAPPORT DE VALIDATION UI / UX / TECHNIQUE", ParagraphStyle('Sub', parent=s_title, fontSize=12, textColor=colors.grey)))
    elements.append(Spacer(1, 3*cm))
    
    cover_data = [
        ["DATE DU RAPPORT", datetime.now().strftime('%d %B %Y')],
        ["LIEU", "Genève, Suisse"],
        ["VERSION", "2.3 (Standard Premium)"],
        ["STATUT", "EN ATTENTE DE SIGNATURE"]
    ]
    t_cover = Table(cover_data, colWidths=[6*cm, 10*cm])
    t_cover.setStyle(TableStyle([
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    elements.append(t_cover)
    elements.append(PageBreak())

    # --- 2. RESUME EXECUTIF (Swiss Approach) ---
    elements.append(Paragraph("Résumé de la Revue", s_h1))
    elements.append(Paragraph("Ce document présente une analyse détaillée de l'interface utilisateur et de la conformité technique du site. L'objectif est d'assurer une expérience client alignée sur les standards de la Haute Joaillerie Genevoise.", s_body))
    elements.append(Spacer(1, 1*cm))
    
    check_data = [
        ["CRITÈRE", "IMPORTANCE", "AUTO-ÉVALUATION", "VALIDATION CLIENT"],
        ["Esthétique & Image de Marque", "Critique", "Conforme (95%)", "[ ]"],
        ["Performance & Temps de chargement", "Élevée", "Optimisé", "[ ]"],
        ["Conformité Légale (LPD/RGPD)", "Critique", "À vérifier", "[ ]"],
        ["Réactivité Mobile (Responsive)", "Élevée", "Conforme", "[ ]"],
        ["Multilingue (FR/EN)", "Moyenne", "En cours", "[ ]"]
    ]
    t_check = Table(check_data, colWidths=[8*cm, 4*cm, 6*cm, 6*cm], rowHeights=0.8*cm)
    t_check.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    elements.append(t_check)
    elements.append(PageBreak())

    # --- 3. SECTIONS DÉTAILLÉES ---
    for s in SECTIONS:
        elements.append(Paragraph(f"{s['id']}. {s['title']}", s_h1))
        
        img_path = os.path.join(SCREENSHOTS_DIR, s["file"])
        if os.path.exists(img_path):
            img = Image(img_path, width=24*cm, height=11*cm, kind='proportional')
            elements.append(img)
        
        elements.append(Spacer(1, 0.5*cm))
        
        # Table de feedback tres precise
        fb_data = [
            ["CATÉGORIE", "ANALYSE TECHNIQUE ET VISUELLE", "RETOUR CLIENT"],
            ["DESIGN & UI", "Respect de la charte, alignements, contrastes.", ""],
            ["CONTENU", "Typographie, orthographe, ton de voix.", ""],
            ["TECH / UX", "Vitesse d'affichage, animations, liens.", ""]
        ]
        t_fb = Table(fb_data, colWidths=[4*cm, 10*cm, 12*cm], rowHeights=[0.7*cm, 1.5*cm, 1.5*cm, 1.5*cm])
        t_fb.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.3, colors.lightgrey),
            ('BACKGROUND', (0,0), (-1,0), colors.whitesmoke),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('FONTSIZE', (0,0), (-1,-1), 8)
        ]))
        elements.append(t_fb)
        elements.append(PageBreak())

    # --- 4. ANNEXE : SCROLL INTEGRAL ---
    elements.append(Paragraph("Annexe A : Vue d'ensemble du Site", s_h1))
    full_path = os.path.join(SCREENSHOTS_DIR, "00_FULL_PAGE_PERFECT.png")
    if os.path.exists(full_path):
        img_full = Image(full_path, width=13*cm, height=16*cm, kind='proportional')
        elements.append(img_full)
    
    doc.build(elements, onFirstPage=on_page_clean, onLaterPages=on_page_clean)
    print(f"PDF Suisse genere : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_swiss_pdf()
