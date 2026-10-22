"""
Excel detaille de suivi de validation - Elke Berr.
Avec colonnes par categorie de commentaire.
"""
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUTPUT = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Suivi_Complet.xlsx"

sections = [
    ("01", "Hero - Accueil", "Navigation, Logo, Image plein ecran, Titre, CTA", "01_section_0px.png"),
    ("02", "La Maison - Heritage", "Histoire, Savoir-faire, Layout 2 colonnes", "02_section_1080px.png"),
    ("03", "Haute Joaillerie", "Collections, Grille produits, Visuels HD", "03_section_2160px.png"),
    ("04", "Unbreakable", "Collaboration Zulay & Pogba, Portraits", "04_section_3240px.png"),
    ("05", "Bespoke - Sur-mesure", "Philosophie, Processus, Pierres", "05_section_4320px.png"),
    ("06", "Footer & Contact", "Coordonnees, Reseaux, Newsletter, Mentions", "06_section_5400px.png"),
]

# Categories de retour
categories = [
    "Structure / Layout",
    "Contenu / Textes",
    "Design / Couleurs",
    "Images / Visuels",
    "Animations",
    "Responsive / Mobile",
    "Autres remarques",
]

rows = []
for num, name, desc, img in sections:
    for cat in categories:
        rows.append({
            "Section N.": num,
            "Section": name,
            "Description": desc,
            "Fichier Screenshot": img,
            "Categorie": cat,
            "Commentaire Client": "",
            "Priorite (Haute/Moyenne/Basse)": "",
            "Statut (A faire / En cours / Fait)": "",
            "Valide (O/N)": "",
        })

df = pd.DataFrame(rows)

with pd.ExcelWriter(OUTPUT, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Suivi Detaille")
    
    wb = writer.book
    ws = wb["Suivi Detaille"]
    
    # Header styling
    header_fill = PatternFill(start_color="1a1a1a", end_color="1a1a1a", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True, size=10)
    thin_border = Border(
        left=Side(style='thin', color='CCCCCC'),
        right=Side(style='thin', color='CCCCCC'),
        top=Side(style='thin', color='CCCCCC'),
        bottom=Side(style='thin', color='CCCCCC'),
    )

    for col_idx, col in enumerate(ws.iter_cols(min_row=1, max_row=1), 1):
        for cell in col:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

    # Column widths
    col_widths = [12, 25, 40, 25, 25, 45, 20, 25, 12]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # Alternating row colors per section
    alt_fill = PatternFill(start_color="F5F5F5", end_color="F5F5F5", fill_type="solid")
    for row_idx in range(2, ws.max_row + 1):
        section_num = ws.cell(row=row_idx, column=1).value
        if section_num and int(section_num) % 2 == 0:
            for col_idx in range(1, len(col_widths) + 1):
                ws.cell(row=row_idx, column=col_idx).fill = alt_fill
        for col_idx in range(1, len(col_widths) + 1):
            ws.cell(row=row_idx, column=col_idx).border = thin_border
            ws.cell(row=row_idx, column=col_idx).alignment = Alignment(vertical='center', wrap_text=True)

    # Freeze header
    ws.freeze_panes = "A2"

print(f"Excel genere : {OUTPUT}")
