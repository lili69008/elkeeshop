"""
ELKE BERR - DOSSIER DE WIREFRAMES MASTER (V2 COMPLETE MIGRATION)
Expert Swiss Standard Edition - Zero Error Policy.
VERSION CORRIGÉE (Import datetime).
"""
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak, Flowable
)
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ---- CONFIGURATION DES ASSETS GÉNÉRÉS ----
ASSETS = {
    "hero_home": "c:/Users/lyies/.gemini/antigravity/brain/652bc02e-3f32-4751-88c9-8efa401d3edb/elke_berr_hero_sapphire_1778337443079.png",
    "maison": "c:/Users/lyies/.gemini/antigravity/brain/652bc02e-3f32-4751-88c9-8efa401d3edb/elke_berr_atelier_geneva_1778337455885.png",
    "bespoke": "c:/Users/lyies/.gemini/antigravity/brain/652bc02e-3f32-4751-88c9-8efa401d3edb/elke_berr_bespoke_sketch_1778337467779.png"
}

# ---- CONFIGURATION VISUELLE ----
COLORS = {
    'bg': colors.HexColor("#F7F7F2"),
    'text': colors.HexColor("#1A1A1A"),
    'accent': colors.HexColor("#B8860B"),
    'border': colors.HexColor("#E0E0E0")
}

OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Dossier_Master_V2_Final.pdf"

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
        canvas.setStrokeColor(COLORS['border'])
        canvas.rect(0, 0, self.width, self.height, fill=1)
        form = canvas.acroForm
        form.textfield(
            name=self.name,
            tooltip="Espace de validation client",
            x=0, y=0, width=self.width, height=self.height,
            borderStyle='solid', borderColor=COLORS['border'],
            fillColor=colors.whitesmoke, fieldFlags='multiline'
        )
        canvas.restoreState()

# ---- STRUCTURE DES PAGES ----
PAGES = [
    {
        "title": "PAGE D'ACCUEIL",
        "concept": "Immersion dans l'univers Elke Berr. Identité visuelle forte, minimalisme et luxe.",
        "sections": [
            ["HERO", "Visuel Sapphire Sri Lanka. Accroche : 'LÀ OÙ LA PIERRE DICTE L'ŒUVRE'."],
            ["INTRODUCTION", "Paragraphe sur l'héritage genevois et la passion des gemmes."],
            ["COLLECTIONS", "Carrousel interactif Zulay & Paul Pogba + Haute Joaillerie."],
            ["FOOTER", "Navigation simplifiée, réseaux sociaux et mentions légales."]
        ],
        "image": ASSETS["hero_home"]
    },
    {
        "title": "LA MAISON (HÉRITAGE)",
        "concept": "Storytelling historique. Focus sur l'expertise de gemmologue d'Elke Berr.",
        "sections": [
            ["HÉRITAGE", "Texte sur les 35 ans d'expérience. Visuel de l'atelier genevois."],
            ["SAVOIR-FAIRE", "Détail de la fabrication artisanale et de la sélection éthique."],
            ["RESPONSABILITÉ", "Certification RJC, traçabilité des pierres et engagement."]
        ],
        "image": ASSETS["maison"]
    },
    {
        "title": "HAUTE JOAILLERIE",
        "concept": "Galerie de pièces uniques. Mise en avant de l'exclusivité.",
        "sections": [
            ["PIÈCES D'EXCEPTION", "Grille de visuels haute résolution. Focus sur les saphirs et émeraudes."],
            ["CRÉATIONS", "Description détaillée de chaque pièce (métaux, carats, origine)."]
        ]
    },
    {
        "title": "PIERRES DE COULEUR",
        "concept": "Expertise gemmologique. Focus sur l'origine et la rareté des gemmes.",
        "sections": [
            ["EXPERTISE", "Description des critères de sélection (Couleur, Taille, Inclusion)."],
            ["SAPHIRS", "Sélection de saphirs du Sri Lanka et de Birmanie."],
            ["ÉMERAUDES", "Gisements de Colombie et d'Éthiopie."]
        ]
    },
    {
        "title": "COLLECTIONS (BIJOUX)",
        "concept": "Catalogue structuré par catégories. Expérience e-commerce premium.",
        "sections": [
            ["CATÉGORIES", "Bagues, Colliers, Bracelets, Boucles d'oreilles."],
            ["UNBREAKABLE", "Section dédiée à l'édition spéciale Zulay & Paul Pogba."]
        ]
    },
    {
        "title": "BESPOKE (SUR MESURE)",
        "concept": "Service de création personnalisée. Dialogue entre le client et la créatrice.",
        "sections": [
            ["PROCESSUS", "De la gouache à la réalisation finale. Visuel d'un croquis de joaillerie."],
            ["PRISE DE RDV", "Formulaire de contact épuré pour une consultation privée."]
        ],
        "image": ASSETS["bespoke"]
    },
    {
        "title": "NEWS & PRESSE",
        "concept": "Flux d'actualités et publications presse. Dynamisme de la marque.",
        "sections": [
            ["ACTUALITÉS", "Articles sur les salons internationaux (Bâle, Genève) et nouvelles collections."],
            ["PRESSE", "Couvertures de magazines et interviews d'Elke Berr."]
        ]
    },
    {
        "title": "CONTACT & BOUTIQUES",
        "concept": "Localisation et contact direct. Service client de proximité.",
        "sections": [
            ["SHOWROOM GENÈVE", "Adresse, horaires et plan d'accès."],
            ["DISTRIBUTEURS", "Liste des points de vente internationaux."]
        ]
    },
    {
        "title": "LÉGAL (COMPLIANCE)",
        "concept": "Respect de la vie privée et informations contractuelles.",
        "sections": [
            ["MENTIONS LÉGALES", "Éditeur, hébergement et crédits."],
            ["CONFIDENTIALITÉ", "Gestion des données (LPD Suisse / RGPD)."]
        ]
    }
]

def build_master_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF, pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm
    )
    styles = getSampleStyleSheet()
    
    # Styles Expert
    s_title = ParagraphStyle('T', parent=styles['Title'], fontSize=34, fontName='Helvetica-Bold', alignment=TA_CENTER)
    s_h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=20, fontName='Helvetica-Bold', spaceBefore=20, spaceAfter=10)
    s_h2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=12, fontName='Helvetica-Bold', textColor=COLORS['accent'])
    s_body = ParagraphStyle('B', parent=styles['Normal'], fontSize=10, fontName='Helvetica', leading=14)
    s_meta = ParagraphStyle('M', parent=styles['Normal'], fontSize=8, fontName='Helvetica', textColor=colors.grey)

    elements = []

    # --- GARDE ---
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph("ELKE BERR GENÈVE", s_title))
    elements.append(Paragraph("DOSSIER DE MIGRATION INTÉGRALE V2 - MASTER", ParagraphStyle('Sub', parent=s_title, fontSize=16, textColor=colors.grey)))
    elements.append(Spacer(1, 4*cm))
    
    meta_info = [["CLIENT", "Elke Berr Creations"], ["DATE", datetime.now().strftime('%d/%m/%Y')], ["STATUT", "Dossier Complet pour Signature"]]
    t_meta = Table(meta_info, colWidths=[4*cm, 10*cm])
    elements.append(t_meta)
    elements.append(PageBreak())

    # --- SOMMAIRE ---
    elements.append(Paragraph("Sommaire des Écrans (Migration V1 -> V2)", s_h1))
    elements.append(Spacer(1, 1*cm))
    for i, p in enumerate(PAGES):
        elements.append(Paragraph(f"{i+1}. {p['title']}", s_body))
    elements.append(PageBreak())

    # --- PAGES ---
    for i, p in enumerate(PAGES):
        elements.append(Paragraph(f"ÉCRAN {i+1:02d} : {p['title']}", s_h1))
        elements.append(Paragraph(f"<i>Concept : {p['concept']}</i>", s_body))
        elements.append(Spacer(1, 0.5*cm))

        # Wireframe Content Grid
        grid_data = []
        for sect in p["sections"]:
            grid_data.append([Paragraph(f"<b>[{sect[0]}]</b>", s_h2), Paragraph(sect[1], s_body)])
        
        t_grid = Table(grid_data, colWidths=[5*cm, 10*cm], rowHeights=1.8*cm)
        t_grid.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, COLORS['border']),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BACKGROUND', (0,0), (0,-1), COLORS['bg'])
        ]))

        # Image if available
        if "image" in p and os.path.exists(p["image"]):
            img = Image(p["image"], width=11*cm, height=8*cm, kind='proportional')
            main_row = [[t_grid, img]]
            t_main = Table(main_row, colWidths=[15.5*cm, 11.5*cm])
        else:
            main_row = [[t_grid, Paragraph("[Concept Visuel V2 - En attente de shooting]", s_meta)]]
            t_main = Table(main_row, colWidths=[15.5*cm, 11.5*cm])
        
        elements.append(t_main)
        elements.append(Spacer(1, 0.8*cm))

        # Validation Field
        elements.append(Paragraph("<b>RETOURS CLIENTS :</b>", s_meta))
        elements.append(InteractiveTextField(width=27*cm, height=3*cm, name=f"fb_{i}"))
        elements.append(PageBreak())

    doc.build(elements)
    print(f"Dossier Master Final généré : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_master_pdf()
