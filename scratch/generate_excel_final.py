"""
Excel Ultra-Premium de Pilotage - Elke Berr.
Inclus : Change Log (Historique), Audit Detaille, Menus deroulants.
"""
import pandas as pd
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from datetime import datetime

OUTPUT = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Pilotage_Final.xlsx"

def create_final_excel():
    wb = Workbook()
    
    # --- FEUILLE 1 : RÉSUMÉ & DASHBOARD ---
    ws_dash = wb.active
    ws_dash.title = "Dashboard"
    ws_dash["B2"] = "PROJET : ELKE BERR SITE WEB V2"
    ws_dash["B2"].font = Font(size=14, bold=True)
    ws_dash["B4"] = "Statut Global du Projet"
    ws_dash["B4"].font = Font(bold=True)
    
    stats = [
        ["Total Elements Audit", 12],
        ["Points Validés ✅", 0],
        ["À modifier 🛠️", 0],
        ["Dernière Mise à jour", datetime.now().strftime('%d/%m/%Y')],
        ["Version du Document", "V2.2 - FINAL"]
    ]
    for r_idx, (label, val) in enumerate(stats, 6):
        ws_dash.cell(row=r_idx, column=2, value=label)
        ws_dash.cell(row=r_idx, column=3, value=val)

    # --- FEUILLE 2 : AUDIT DÉTAILLÉ ---
    ws_audit = wb.create_sheet("Audit de Détail")
    headers = ["ID", "Section", "Composant", "Statut", "Priorité", "Commentaire Client", "Action Plan"]
    ws_audit.append(headers)
    
    data = [
        ["01", "Hero", "Navigation", "A VALIDER", "Haute", "", ""],
        ["01", "Hero", "Boutons CTA", "A VALIDER", "Moyenne", "", ""],
        ["02", "Heritage", "Textes", "A VALIDER", "Basse", "", ""],
        ["03", "Collections", "Grille Produits", "A VALIDER", "Haute", "", ""],
        ["04", "Philosophie", "Textes colonnes", "A VALIDER", "Moyenne", "", ""],
        ["05", "Audace", "Image Bague", "A VALIDER", "Basse", "", ""],
        ["06", "Footer", "Coordonnees", "A VALIDER", "Moyenne", "", ""]
    ]
    for r in data:
        ws_audit.append(r)

    # Menus deroulants
    dv_status = DataValidation(type="list", formula1='"A VALIDER,VALIDÉ ✅,À MODIFIER 🛠️,REFUSÉ ❌"', allow_blank=True)
    dv_priority = DataValidation(type="list", formula1='"Haute,Moyenne,Basse"', allow_blank=True)
    ws_audit.add_data_validation(dv_status)
    ws_audit.add_data_validation(dv_priority)
    dv_status.add(f"D2:D100")
    dv_priority.add(f"E2:E100")

    # Style Audit
    header_fill = PatternFill(start_color="1a1a1a", end_color="1a1a1a", fill_type="solid")
    white_font = Font(color="FFFFFF", bold=True)
    for cell in ws_audit[1]:
        cell.fill = header_fill
        cell.font = white_font
    
    ws_audit.column_dimensions['B'].width = 15
    ws_audit.column_dimensions['C'].width = 25
    ws_audit.column_dimensions['F'].width = 60

    # --- FEUILLE 3 : CHANGE LOG (HISTORIQUE) ---
    ws_log = wb.create_sheet("Historique des Révisions")
    log_headers = ["DATE", "VERSION", "AUTEUR", "DESCRIPTION DES MODIFICATIONS", "NB POINTS REVUS"]
    ws_log.append(log_headers)
    
    # Pre-remplissage du premier log
    ws_log.append([datetime.now().strftime('%d/%m/%Y'), "V2.2", "Antigravity AI", "Creation du dossier de validation final avec filigrane et index interactif.", "Tous"])
    
    for cell in ws_log[1]:
        cell.fill = header_fill
        cell.font = white_font
    
    ws_log.column_dimensions['A'].width = 15
    ws_log.column_dimensions['D'].width = 80
    
    wb.save(OUTPUT)
    print(f"Excel Final genere : {OUTPUT}")

if __name__ == "__main__":
    create_final_excel()
