"""
ELKE BERR - MASTER WIREFRAME GENERATOR (Expert Swiss Edition)
Ce script génère un dossier de validation complet, écran par écran, 
en déclinant l'identité visuelle V2 sur l'ensemble des contenus de l'ancien site.
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
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# ---- CONFIGURATION VISUELLE (Style V2 Audité) ----
COLORS = {
    'background': colors.HexColor("#F7F7F2"), # Crème soyeuse
    'text': colors.HexColor("#1A1A1A"),       # Anthracite profond
    'accent': colors.HexColor("#B8860B"),     # Or / Bronze
    'white': colors.white,
    'grey': colors.grey,
    'light_grey': colors.HexColor("#E0E0E0")
}

FONTS = {
    'serif': 'Helvetica-Bold', # Placeholder pour EB Garamond (standard ReportLab)
    'sans': 'Helvetica'
}

OUTPUT_PDF = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Wireframes_Complets_V2.pdf"

# ---- COMPOSANT INTERACTIF ----
class InteractiveFeedbackField(Flowable):
    def __init__(self, width, height, name):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.name = name

    def draw(self):
        canvas = self.canv
        canvas.saveState()
        canvas.setFillColor(colors.whitesmoke)
        canvas.setStrokeColor(COLORS['light_grey'])
        canvas.rect(0, 0, self.width, self.height, fill=1)
        form = canvas.acroForm
        form.textfield(
            name=self.name,
            tooltip="Espace de retour client",
            x=0, y=0,
            width=self.width,
            height=self.height,
            borderStyle='solid',
            borderColor=COLORS['light_grey'],
            fillColor=colors.whitesmoke,
            fieldFlags='multiline'
        )
        canvas.restoreState()

# ---- MAPPING DES PAGES (Migration V1 -> V2) ----
PAGES_STRUCTURE = [
    {
        "page_title": "PAGE D'ACCUEIL",
        "sections": [
            {"type": "hero", "title": "LÀ OÙ LA PIERRE DICTE L'ŒUVRE", "desc": "Visuel : Saphir Sri Lanka. Identité visuelle forte."},
            {"type": "text_image", "title": "D'ABORD GEMMOLOGUE", "desc": "Portrait Paul Pogba & Texte Héritage."},
            {"type": "grid", "title": "COLLECTION UNBREAKABLE", "desc": "3 Produits phares : Bracelet, Collier, Bague."}
        ]
    },
    {
        "page_title": "LA MAISON / HÉRITAGE",
        "sections": [
            {"type": "hero", "title": "UNE HISTOIRE DE FAMILLE", "desc": "Visuel : Atelier de Genève, plan rapproché sur les mains."},
            {"type": "text", "title": "NOTRE MISSION", "desc": "Texte sur l'éthique, la certification RJC et la sélection des gemmes."},
            {"type": "text_image", "title": "ELKE BERR", "desc": "Portrait de la fondatrice et son approche créative."}
        ]
    },
    {
        "page_title": "HAUTE JOAILLERIE",
        "sections": [
            {"type": "hero", "title": "PIÈCES UNIQUES", "desc": "Visuel : Bague Saphir Haute Joaillerie sur fond minimaliste."},
            {"type": "grid_large", "title": "CRÉATIONS D'EXCEPTION", "desc": "Galerie immersive des pièces de collection (Saphirs, Émeraudes)."}
        ]
    },
    {
        "page_title": "BESPOKE (SUR MESURE)",
        "sections": [
            {"type": "hero", "title": "VOTRE RÊVE, NOTRE SAVOIR-FAIRE", "desc": "Visuel : Dessin gouaché en cours de réalisation."},
            {"type": "text", "title": "LE PROCESSUS CRÉATIF", "desc": "De la sélection de la pierre à la monture finale."},
            {"type": "form", "title": "DEMANDE DE CONSULTATION", "desc": "Formulaire épuré pour prise de rendez-vous."}
        ]
    },
    {
        "page_title": "CONTACT & BOUTIQUES",
        "sections": [
            {"type": "hero", "title": "NOUS RENCONTRER", "desc": "Visuel : Boutique de Genève ou vue sur le jet d'eau."},
            {"type": "grid", "title": "NOS POINTS DE VENTE", "desc": "Genève, Paris, International. Adresses et horaires."}
        ]
    }
]

def build_expert_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=landscape(A4),
        leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm,
    )
    styles = getSampleStyleSheet()

    # Styles personnalisés (Audit Suisse)
    s_main_title = ParagraphStyle('MainTitle', parent=styles['Title'], fontSize=34, fontName=FONTS['serif'], spaceAfter=30, alignment=TA_CENTER)
    s_page_header = ParagraphStyle('PageHeader', parent=styles['Heading1'], fontSize=20, fontName=FONTS['serif'], spaceBefore=20, spaceAfter=10, textColor=COLORS['text'])
    s_section_title = ParagraphStyle('SectionTitle', parent=styles['Heading2'], fontSize=14, fontName=FONTS['serif'], textColor=COLORS['accent'])
    s_body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, fontName=FONTS['sans'], leading=14)
    s_meta = ParagraphStyle('Meta', parent=styles['Normal'], fontSize=8, fontName=FONTS['sans'], textColor=colors.grey)

    elements = []

    # --- 1. PAGE DE GARDE ---
    elements.append(Spacer(1, 5*cm))
    elements.append(Paragraph("ELKE BERR GENÈVE", s_main_title))
    elements.append(Paragraph("DOSSIER DE WIREFRAMES COMPLETS - V2", ParagraphStyle('S', parent=s_main_title, fontSize=16, textColor=colors.grey)))
    elements.append(Spacer(1, 4*cm))
    
    meta_data = [
        ["CLIENT :", "Elke Berr Creations (Suisse)"],
        ["DATE :", datetime.now().strftime('%d/%m/%Y')],
        ["OBJET :", "Migration Intégrale V1 -> V2 (Identité Visuelle)"],
        ["STANDARD :", "Expert / Haute Joaillerie"]
    ]
    t_meta = Table(meta_data, colWidths=[4*cm, 10*cm])
    t_meta.setStyle(TableStyle([('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('ALIGN', (0,0), (-1,-1), 'LEFT')]))
    elements.append(t_meta)
    elements.append(PageBreak())

    # --- 2. INDEX DES PAGES ---
    elements.append(Paragraph("Sommaire des Écrans", s_page_header))
    elements.append(Spacer(1, 1*cm))
    for i, page in enumerate(PAGES_STRUCTURE):
        elements.append(Paragraph(f"{i+1}. {page['page_title']}", s_body))
    elements.append(PageBreak())

    # --- 3. GÉNÉRATION ÉCRAN PAR ÉCRAN ---
    for p_idx, page in enumerate(PAGES_STRUCTURE):
        # Titre de la page
        elements.append(Paragraph(f"ÉCRAN {p_idx+1:02d} : {page['page_title']}", s_page_header))
        elements.append(Spacer(1, 0.5*cm))

        # Conteneur pour le Wireframe (Simulé par un tableau structuré)
        wireframe_data = []
        for section in page["sections"]:
            wireframe_data.append([
                Paragraph(f"<b>[{section['type'].upper()}]</b><br/>{section['title']}", s_section_title),
                Paragraph(section['desc'], s_body)
            ])
        
        t_wireframe = Table(wireframe_data, colWidths=[7*cm, 19*cm], rowHeights=2.5*cm)
        t_wireframe.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, COLORS['light_grey']),
            ('BACKGROUND', (0,0), (0,-1), COLORS['background']),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 15),
        ]))
        elements.append(t_wireframe)
        
        elements.append(Spacer(1, 1*cm))
        
        # ZONE DE FEEDBACK CLIENT INTERACTIVE
        elements.append(Paragraph("ESPACE DE VALIDATION CLIENT :", ParagraphStyle('F', parent=s_meta, bold=True)))
        elements.append(InteractiveFeedbackField(width=26*cm, height=3*cm, name=f"feedback_page_{p_idx}"))
        
        elements.append(PageBreak())

    # --- 4. ANNEXE : DESIGN SYSTEM V2 ---
    elements.append(Paragraph("ANNEXE : RÈGLES DE DESIGN V2 (SUISSE)", s_page_header))
    elements.append(Spacer(1, 0.5*cm))
    ds_data = [
        ["ÉLÉMENT", "SPÉCIFICATION V2"],
        ["Couleur Fond", "#F7F7F2 (Crème)"],
        ["Texte Principal", "#1A1A1A (Anthracite)"],
        ["Accents Or", "#B8860B"],
        ["Typo Titres", "Serif Contrastée (Italique ponctuel)"],
        ["Typo Corps", "Sans-Serif Géométrique (Light/Regular)"],
        ["Grilles", "Espacement 40px, Pas de bordures"]
    ]
    t_ds = Table(ds_data, colWidths=[6*cm, 15*cm], rowHeights=0.8*cm)
    t_ds.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('BACKGROUND', (0,0), (-1,0), COLORS['text']),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
    ]))
    elements.append(t_ds)

    doc.build(elements)
    print(f"Dossier Expert PDF généré avec succès : {OUTPUT_PDF}")

if __name__ == "__main__":
    build_expert_pdf()
