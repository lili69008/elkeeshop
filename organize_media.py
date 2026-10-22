import os
import csv
import shutil
import re
from pathlib import Path

def clean_filename(filename):
    """Supprime les suffixes Shopify comme _800x800."""
    return re.sub(r'_\d+x\d+', '', filename)

def get_product_mapping():
    """Crée un mapping Filename -> [Handles]."""
    csv_path = Path('localhost_v2/products.csv')
    if not csv_path.exists():
        print("Erreur: products.csv non trouvé.")
        return {}
        
    mapping = {}
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                handle = row.get('Handle')
                if not handle: continue
                
                # On récupère les URLs d'images
                urls = [row.get('Image Src'), row.get('Variant Image')]
                for url in urls:
                    if url and isinstance(url, str):
                        # Extraction du nom de fichier propre
                        fname = url.split('/')[-1].split('?')[0]
                        fname = clean_filename(fname) # On nettoie aussi le nom venant de l'URL
                        if fname:
                            if fname not in mapping:
                                mapping[fname] = set()
                            mapping[fname].add(handle)
    except Exception as e:
        print(f"Erreur lors de la lecture du CSV : {e}")
        
    return mapping

def organize_and_update():
    base_dir = Path('localhost_v2')
    src_media = base_dir / 'shopify_media'
    dest_root = base_dir / 'img' / 'produits'
    
    if not src_media.exists():
        print(f"Erreur: Le dossier {src_media} n'existe pas.")
        return

    mapping = get_product_mapping()
    file_relocations = {} # original_name -> new_rel_path (on prend le 1er handle trouvé pour la redirection globale)

    print("--- Organisation des fichiers ---")
    
    for fname in os.listdir(src_media):
        src_path = src_media / fname
        if not src_path.is_file(): continue
        
        cleaned_fname = clean_filename(fname)
        
        if cleaned_fname in mapping:
            handles = mapping[cleaned_fname]
            
            # On copie le fichier dans chaque dossier produit concerné
            for handle in handles:
                target_dir = dest_root / handle
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, target_dir / cleaned_fname)
                
                # Pour le mapping global (utilisé pour les pages racine), 
                # on garde le chemin du premier handle
                if fname not in file_relocations:
                    file_relocations[fname] = f"img/produits/{handle}/{cleaned_fname}"
        else:
            # Cas des vidéos ou fichiers non listés dans le CSV
            if fname.lower().endswith(('.mp4', '.mov', '.webm')):
                target_dir = base_dir / 'img' / 'videos'
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, target_dir / fname)
                file_relocations[fname] = f"img/videos/{fname}"
            else:
                # Autres médias (logos, icônes, etc.)
                target_dir = base_dir / 'img' / 'site'
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, target_dir / fname)
                file_relocations[fname] = f"img/site/{fname}"

    print(f"Organisation terminée. {len(file_relocations)} fichiers traités.")

    print("--- Mise à jour des fichiers HTML ---")
    html_files = list(base_dir.rglob('*.html'))
    updated_count = 0

    for html_path in html_files:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        
        # On calcule le préfixe relatif (../) selon la profondeur
        depth = len(html_path.relative_to(base_dir).parts) - 1
        prefix = "../" * depth
        
        # Si c'est une page produit, on essaie d'être malin
        current_handle = None
        if "produits/" in str(html_path.as_posix()):
            current_handle = html_path.stem # Le nom du fichier .html est le handle

        # Recherche de patterns "shopify_media/nom_fichier", "img/site/nom_fichier", ou URLs CDN Shopify
        # On utilise une regex pour attraper les variations de chemins relatifs ou URLs absolues
        regex = r'(?:shopify_media|img/site|img/misc|https://cdn\.shopify\.com/[^\s"\'\>]+/files)/([^"\'\s>\?]+)'
        refs = re.findall(regex, content)
        
        for ref_fname in set(refs):
            if ref_fname in file_relocations:
                # Si on est sur la page du produit, on utilise son propre dossier
                if current_handle and ref_fname in mapping and current_handle in mapping[ref_fname]:
                    cleaned = clean_filename(ref_fname)
                    new_ref = f"{prefix}img/produits/{current_handle}/{cleaned}"
                else:
                    # Sinon on utilise le chemin par défaut
                    new_ref = prefix + file_relocations[ref_fname]
                
                # Remplacement agressif du chemin complet trouvé
                # On cherche soit un chemin relatif local, soit une URL CDN Shopify (avec paramètres optionnels)
                pattern = r'([\./]*(?:shopify_media|img/site|img/misc)/' + re.escape(ref_fname) + r'|https://cdn\.shopify\.com/[^\s"\'\>]+/files/' + re.escape(ref_fname) + r'(?:\?[^\s"\'\>]*)?)'
                new_content = re.sub(pattern, new_ref, new_content)

        if new_content != content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_count += 1

    print(f"Mise à jour terminée. {updated_count} fichiers HTML modifiés.")

if __name__ == "__main__":
    organize_and_update()
