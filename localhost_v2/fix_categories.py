import csv
import os
import re

CSV_PATH = "products.csv"
PROD_DIR = "produits"

# Shared logic for categorizing
def get_category(handle, title, ptype):
    handle = handle.lower()
    title = title.lower()
    ptype = ptype.lower()
    
    combined = handle + " " + title + " " + ptype
    
    if "earring" in combined or "boucle" in combined or "stud" in combined or "ear-cuff" in combined or "earcuff" in combined:
        return "Boucles d'oreilles"
    if "cufflink" in combined:
        return "Boutons de manchette"
    if "ring" in combined or "bague" in combined or "phalanx" in combined:
        return "Bagues"
    if "necklace" in combined or "collier" in combined or "choker" in combined or "pendant" in combined or "pendentif" in combined:
        return "Colliers" # Merging Pendentifs into Colliers is usually best unless requested separately. Let's keep them in Colliers for simplicity or map strictly.
    if "bracelet" in combined or "bangle" in combined:
        return "Bracelets"
        
    # Manual Fallbacks based on typical Elke Berr catalog
    if "olympia" in combined: return "Colliers"
    if "imperium" in combined: return "Colliers"
    if "phoenix" in combined: return "Colliers" # the handle "phoenix" is a necklace
    if "unbreakable" in combined and "silver" in combined: return "Colliers"
    if "unbreakable" in combined and "black" in combined: return "Colliers"
    
    return "Bagues" # Absolute fallback

def fix_all():
    collections = {
        "Bagues": [],
        "Colliers": [],
        "Bracelets": [],
        "Boucles d'oreilles": [],
        "Boutons de manchette": []
    }

    with open(CSV_PATH, "r", encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        current_product = None

        for row in reader:
            handle = row.get("Handle", "")
            if not handle: continue

            if current_product is None or current_product["handle"] != handle:
                if current_product is not None:
                    cat = get_category(current_product["handle"], current_product["title"], current_product["type"])
                    collections[cat].append(current_product)

                current_product = {
                    "handle": handle,
                    "title": row.get("Title", handle.replace("-", " ").title()),
                    "type": row.get("Type", ""),
                    "price": row.get("Variant Price", "Sur demande"),
                    "image": ""
                }
            
            img_src = row.get("Image Src", "")
            if img_src and not current_product["image"]:
                current_product["image"] = img_src
                
        if current_product is not None:
            cat = get_category(current_product["handle"], current_product["title"], current_product["type"])
            collections[cat].append(current_product)

    # 1. Update Collection Pages
    with open("bagues.html", 'r', encoding='utf-8') as f:
        content = f.read()

    header_match = re.search(r'(.*?)<section id="bagues-hero"', content, re.DOTALL)
    footer_match = re.search(r'(</section>\s*<footer>.*)', content, re.DOTALL)
    
    if not header_match or not footer_match:
        print("Could not parse template for collections")
        return

    header_html = header_match.group(1)
    footer_html = footer_match.group(1)
    
    COLLECTIONS_INFO = {
        "Bagues": ("LES BAGUES", "Des créations d'exception où la pierre précieuse est au cœur de l'œuvre."),
        "Colliers": ("LES COLLIERS", "Découvrez notre sélection de colliers, alliant la délicatesse de l'or aux éclats vibrants."),
        "Bracelets": ("LES BRACELETS", "Des créations fluides et élégantes qui épousent le poignet avec grâce."),
        "Boucles d'oreilles": ("LES BOUCLES D'OREILLES", "Des pièces majestueuses où la lumière danse à travers des gemmes rares."),
        "Boutons de manchette": ("BOUTONS DE MANCHETTE", "L'élégance masculine sublimée. Des créations intemporelles.")
    }

    for cat_name, prods in collections.items():
        if not prods: continue
        title, desc = COLLECTIONS_INFO[cat_name]
        
        hero_html = f'''<section id="bagues-hero" class="reveal" style="padding-top: 18rem; text-align: center;">
        <span class="kicker">COLLECTIONS</span>
        <h1 style="font-size: 3.5rem; letter-spacing: 0.2em;">{title}</h1>
        <div style="width: 60px; height: 1px; background: var(--text); margin: 3rem auto;"></div>
        <p style="max-width: 700px; margin: 0 auto; line-height: 1.8; color: var(--muted); font-weight: 300;">
            {desc}
        </p>
    </section>'''

        grid_html = '\n    <section id="bagues-grid" class="reveal" style="padding: 6rem 5% 12rem;">\n        <div class="grid-3">\n'
        for p in prods:
            img = p['image'] if p['image'] else "img/bague_saphir.png"
            price = p['price'] if p['price'] and p['price'] != "0" else "Sur demande"
            price_display = f"{price} CHF" if price != "Sur demande" else price
            
            grid_html += f"""            <a href="produits/{p['handle']}.html" style="text-decoration:none; color:inherit;">
                <div class="card reveal">
                    <div class="card-img-wrapper"><img src="{img}"></div>
                    <span class="kicker">{cat_name.upper()}</span>
                    <h3>{p['title']}</h3>
                    <p style="color:var(--muted); font-size:0.8rem;">{price_display}</p>
                </div>
            </a>\n"""
        grid_html += '        </div>'
        
        filename = cat_name.lower().replace(" ", "-").replace("'", "").replace("é", "e") + ".html"
        full_html = header_html + hero_html + grid_html + footer_html
        full_html = re.sub(r'<title>.*?</title>', f'<title>{title} — Elke Berr Genève</title>', full_html)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Updated collection: {filename} ({len(prods)} items)")

        # 2. Update individual product pages in /produits/
        for p in prods:
            p_file = os.path.join(PROD_DIR, f"{p['handle']}.html")
            if os.path.exists(p_file):
                with open(p_file, 'r', encoding='utf-8') as f:
                    p_html = f.read()
                # Update breadcrumb kicker
                p_html = re.sub(r'<span class="product-collection">.*?</span>', f'<span class="product-collection">{cat_name.upper()}</span>', p_html)
                with open(p_file, 'w', encoding='utf-8') as f:
                    f.write(p_html)

if __name__ == "__main__":
    fix_all()
