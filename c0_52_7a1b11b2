import csv
import os
import re

CSV_PATH = "products.csv"
TEMPLATE_PATH = "bagues.html"

# Titles and descriptions for collections
COLLECTIONS_INFO = {
    "Bagues": {
        "kicker": "COLLECTIONS",
        "title": "LES BAGUES",
        "desc": "Les bagues Elke Berr sont des créations d'exception où la pierre précieuse est au cœur de l'œuvre. Chaque bague raconte une histoire unique, mêlant expertise gemmologique et design raffiné."
    },
    "Colliers": {
        "kicker": "COLLECTIONS",
        "title": "LES COLLIERS",
        "desc": "Découvrez notre sélection de colliers, alliant la délicatesse de l'or aux éclats vibrants de pierres précieuses soigneusement sourcées."
    },
    "Bracelets": {
        "kicker": "COLLECTIONS",
        "title": "LES BRACELETS",
        "desc": "Des créations fluides et élégantes qui épousent le poignet avec grâce. Chaque bracelet est une déclaration d'indépendance et de style."
    },
    "Boucles d'oreilles": {
        "kicker": "COLLECTIONS",
        "title": "LES BOUCLES D'OREILLES",
        "desc": "Illuminez votre visage avec nos boucles d'oreilles. Des pièces majestueuses où la lumière danse à travers des gemmes rares."
    },
    "Pendentifs": {
        "kicker": "COLLECTIONS",
        "title": "LES PENDENTIFS",
        "desc": "Portés près du cœur, nos pendentifs sont des talismans précieux, sertis de pierres aux couleurs profondes et envoûtantes."
    },
    "Boutons de manchette": {
        "kicker": "COLLECTIONS",
        "title": "BOUTONS DE MANCHETTE",
        "desc": "L'élégance masculine sublimée. Des créations intemporelles pour parfaire les silhouettes les plus exigeantes."
    }
}

def generate_collections():
    if not os.path.exists(CSV_PATH) or not os.path.exists(TEMPLATE_PATH):
        print("Erreur: products.csv ou bagues.html introuvable.")
        return

    # Read the base template from bagues.html
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract header up to <section id="bagues-hero">
    header_match = re.search(r'(.*?)<section id="bagues-hero".*?</section>', content, re.DOTALL)
    footer_match = re.search(r'(</section>\s*<footer>.*)', content, re.DOTALL)

    if not header_match or not footer_match:
        print("Impossible de parser bagues.html comme template.")
        return

    header_html = header_match.group(1)
    footer_html = footer_match.group(1)

    # Read products
    collections = {
        "Bagues": [],
        "Colliers": [],
        "Bracelets": [],
        "Boucles d'oreilles": [],
        "Pendentifs": [],
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
                    add_to_collection(current_product, collections)

                ptype = row.get("Type", "").strip()
                if not ptype:
                    if "ring" in handle.lower() or "bague" in handle.lower(): ptype = "Bagues"
                    elif "necklace" in handle.lower() or "collier" in handle.lower(): ptype = "Colliers"
                    elif "bracelet" in handle.lower() or "bangle" in handle.lower(): ptype = "Bracelets"
                    elif "earring" in handle.lower() or "boucle" in handle.lower(): ptype = "Boucles d'oreilles"
                    elif "pendant" in handle.lower(): ptype = "Pendentifs"
                    elif "cufflink" in handle.lower(): ptype = "Boutons de manchette"
                    else: ptype = "Bagues" # Default fallback
                
                type_mapping = {
                    "Ring": "Bagues", "Bague": "Bagues",
                    "Necklace": "Colliers", "Collier": "Colliers",
                    "Bracelet": "Bracelets", "Bangle": "Bracelets",
                    "Earring": "Boucles d'oreilles", "Boucles d'oreilles": "Boucles d'oreilles", "Earrings": "Boucles d'oreilles",
                    "Pendant": "Pendentifs", "Pendentif": "Pendentifs",
                    "Cufflink": "Boutons de manchette", "Cufflinks": "Boutons de manchette"
                }
                ptype_fr = type_mapping.get(ptype, ptype)
                
                # If it's a completely unknown type, default to Bagues or create a new dict entry
                if ptype_fr not in collections:
                    collections[ptype_fr] = []

                current_product = {
                    "handle": handle,
                    "title": row.get("Title", handle.replace("-", " ").title()),
                    "type": ptype_fr,
                    "price": row.get("Variant Price", "Sur demande"),
                    "image": ""
                }
            
            img_src = row.get("Image Src", "")
            if img_src and not current_product["image"]:
                current_product["image"] = img_src
                
        if current_product is not None:
            add_to_collection(current_product, collections)

    # Generate Pages
    print("Génération des pages de collection...")
    for coll_name, products in collections.items():
        if not products: continue

        info = COLLECTIONS_INFO.get(coll_name, {
            "kicker": "COLLECTION",
            "title": coll_name.upper(),
            "desc": f"Découvrez notre collection de {coll_name}."
        })

        # Build hero
        hero_html = f"""
    <section id="bagues-hero" style="padding-top: 18rem; text-align: center;">
        <span class="kicker">{info['kicker']}</span>
        <h1 style="font-size: 3.5rem; letter-spacing: 0.2em;">{info['title']}</h1>
        <div style="width: 60px; height: 1px; background: var(--text); margin: 3rem auto;"></div>
        <p style="max-width: 700px; margin: 0 auto; line-height: 1.8; color: var(--muted); font-weight: 300;">
            {info['desc']}
        </p>
    </section>"""

        # Build grid
        grid_html = '\n    <section id="bagues-grid" style="padding: 6rem 5% 12rem;">\n        <div class="grid-3">\n'
        for p in products:
            img = p['image'] if p['image'] else "img/bague_saphir.png"
            price = p['price'] if p['price'] and p['price'] != "0" else "Sur demande"
            price_display = f"{price} CHF" if price != "Sur demande" else price
            
            grid_html += f"""            <a href="produits/{p['handle']}.html" style="text-decoration:none; color:inherit;">
                <div class="card reveal">
                    <div class="card-img-wrapper"><img src="{img}"></div>
                    <span class="kicker">{p['type'].upper()}</span>
                    <h3>{p['title']}</h3>
                    <p style="color:var(--muted); font-size:0.8rem;">{price_display}</p>
                </div>
            </a>\n"""
        
        grid_html += '        </div>'

        # Assemble
        filename = coll_name.lower().replace(" ", "-").replace("'", "").replace("é", "e") + ".html"
        full_html = header_html + hero_html + grid_html + footer_html
        
        # Ensure the page title is correct
        full_html = re.sub(r'<title>.*?</title>', f'<title>{info["title"]} — Elke Berr Genève</title>', full_html)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Page générée: {filename} ({len(products)} produits)")

def add_to_collection(product, collections):
    t = product["type"]
    if t in collections:
        collections[t].append(product)
    else:
        # Fallback if unmapped
        collections["Bagues"].append(product)

if __name__ == "__main__":
    generate_collections()
