import csv
import os
import re
import requests
from io import BytesIO
from PIL import Image
import json
import time
import urllib3
urllib3.disable_warnings()

CSV_PATH = "products.csv"
CACHE_FILE = "color_cache.json"

# Official Mappings from ElkeBerr.com
MAPPINGS = {
    "Rock'N Rose": ["twilight", "sensuelle", "rockn-rose"],
    "Singular": ["orbis-lacteus", "orchid", "diabolo", "ouranos", "deep-blue"],
    "Mysteria": ["ophidia", "mysteria", "ondara", "celeste", "nefertity", "lotus"],
    "Waves": ["aqua", "ondes", "mermaid", "recif", "coral", "icefall"],
    "Pour Lui": ["l-anamour", "twilight-elegance-single-ring", "sensuelle-bracelet", "rockn-rose", "kiss-me", "ardoise", "initials", "negative-blues", "lanthracite", "cufflink", "manchette"]
}

def get_category(handle, title, ptype):
    handle = handle.lower()
    title = title.lower()
    ptype = ptype.lower()
    combined = handle + " " + title + " " + ptype
    
    if "earring" in combined or "boucle" in combined or "stud" in combined or "ear-cuff" in combined or "earcuff" in combined:
        return "Boucles d'oreilles"
    if "cufflink" in combined or "manchette" in combined:
        return "Boutons de manchette"
    if "ring" in combined or "bague" in combined or "phalanx" in combined:
        return "Bagues"
    if "necklace" in combined or "collier" in combined or "choker" in combined or "pendant" in combined or "pendentif" in combined:
        return "Colliers" 
    if "bracelet" in combined or "bangle" in combined:
        return "Bracelets"
    return "Bagues"

def get_image_brightness(img_url, cache):
    if not img_url: return 255.0
    if img_url in cache: return cache[img_url]
    print(f"Analyzing color for: {img_url}")
    try:
        r = requests.get(img_url, timeout=5, verify=False)
        img = Image.open(BytesIO(r.content)).convert('RGB')
        img = img.resize((10, 10))
        width, height = img.size
        top_edge = [img.getpixel((x, 0)) for x in range(width)]
        avg_r = sum(p[0] for p in top_edge) / len(top_edge)
        avg_g = sum(p[1] for p in top_edge) / len(top_edge)
        avg_b = sum(p[2] for p in top_edge) / len(top_edge)
        brightness = (avg_r * 299 + avg_g * 587 + avg_b * 114) / 1000
        cache[img_url] = brightness
        time.sleep(0.02)
        return brightness
    except:
        cache[img_url] = 255.0
        return 255.0

def generate_sorted_collections():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f: color_cache = json.load(f)
    else: color_cache = {}

    collections = {
        "Bagues": [], "Colliers": [], "Bracelets": [], "Boucles d'oreilles": [], "Boutons de manchette": [],
        "Rock'N Rose": [], "Singular": [], "Mysteria": [], "Waves": [], "Pour Elle": [], "Pour Lui": [], "Sélections": []
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
                    current_product["brightness"] = get_image_brightness(current_product["image"], color_cache)
                    
                    # 1. Main category
                    collections[cat].append(current_product)
                    
                    # 2. Specific Collections (Mappings from official site)
                    h_l = current_product["handle"].lower()
                    for col_name, keywords in MAPPINGS.items():
                        if any(k in h_l for k in keywords):
                            collections[col_name].append(current_product)
                    
                    # 3. Pour Elle (Everything except strictly masculine or just add most things)
                    if "Boutons de manchette" not in cat:
                        collections["Pour Elle"].append(current_product)
                    
                    # 4. Sélections (Top 16 items)
                    if len(collections["Sélections"]) < 16:
                        collections["Sélections"].append(current_product)

                current_product = {
                    "handle": handle, "title": row.get("Title", handle.replace("-", " ").title()),
                    "type": row.get("Type", ""), "price": row.get("Variant Price", "0"), "image": ""
                }
            img_src = row.get("Image Src", "")
            if img_src and not current_product["image"]: current_product["image"] = img_src
                
        if current_product is not None:
            cat = get_category(current_product["handle"], current_product["title"], current_product["type"])
            current_product["brightness"] = get_image_brightness(current_product["image"], color_cache)
            collections[cat].append(current_product)

    with open(CACHE_FILE, 'w') as f: json.dump(color_cache, f)

    with open("index.html", 'r', encoding='utf-8') as f: content = f.read()
    # Scrape nav and head
    header_match = re.search(r'(.*?)<div class="hero-video-container"', content, re.DOTALL)
    # Scrape footer
    footer_match = re.search(r'(<footer>.*)', content, re.DOTALL)
    header_html, footer_html = header_match.group(1), footer_match.group(1)
    
    # Add closing body/html to footer if missing from match
    if "</body>" not in footer_html:
        footer_html += "\n</body>\n</html>"
    
    COL_INFO = {
        "Bagues": ("LES BAGUES", "Des créations d'exception où la pierre précieuse est au cœur de l'œuvre."),
        "Colliers": ("LES COLLIERS", "Découvrez notre sélection de colliers, alliant la délicatesse de l'or aux éclats vibrants."),
        "Bracelets": ("LES BRACELETS", "Des créations fluides et élégantes qui épousent le poignet avec grâce."),
        "Boucles d'oreilles": ("LES BOUCLES D'OREILLES", "Des pièces majestueuses où la lumière danse à travers des gemmes rares."),
        "Boutons de manchette": ("BOUTONS DE MANCHETTE", "L'élégance masculine sublimée. Des créations intemporelles."),
        "Rock'N Rose": ("COLLECTION ROCK'N ROSE", "Une alliance audacieuse entre l'esprit rock et la délicatesse de la rose."),
        "Singular": ("COLLECTION SINGULAR", "Des pièces uniques pour des personnalités singulières."),
        "Mysteria": ("COLLECTION MYSTERIA", "L'énigme de la beauté capturée dans des pierres aux reflets mystérieux."),
        "Waves": ("COLLECTION WAVES", "La fluidité du mouvement de l'eau immortalisée dans l'or."),
        "Pour Elle": ("SÉLECTION POUR ELLE", "Le cadeau parfait pour sublimer sa féminité."),
        "Pour Lui": ("SÉLECTION POUR LUI", "L'élégance au masculin, entre force et raffinement."),
        "Sélections": ("NOTRE SÉLECTION", "Les pièces iconiques et les coups de cœur de la Maison.")
    }

    for cat_name, prods in collections.items():
        if not prods: continue
        title, desc = COL_INFO[cat_name]
        prods.sort(key=lambda x: x["brightness"], reverse=True)
        
        hero_html = f'''<section id="bagues-hero" class="reveal" style="padding-top: 18rem; padding-bottom: 8rem; text-align: center;">
        <span class="kicker">Maison Elke Berr</span>
        <h1 style="font-size: clamp(2.5rem, 5vw, 4rem); letter-spacing: 0.25em; font-weight: 400; margin-bottom: 3rem;">{title}</h1>
        <div style="width: 40px; height: 1px; background: var(--fg); margin: 0 auto 3rem;"></div>
        <p style="max-width: 650px; margin: 0 auto; line-height: 2; color: var(--muted); font-weight: 300; font-size: 0.95rem; letter-spacing: 0.02em;">{desc}</p>
    </section>'''

        grid_html = '\n    <section id="bagues-grid" class="reveal" style="padding: 0 8vw 15rem;">\n        <div class="grid-3">\n'
        for p in prods:
            img = p['image'] if p['image'] else "img/bague_saphir.png"
            try:
                p_val = float(str(p['price']).replace(",", ""))
                price_display = f"{p['price']} CHF" if p_val > 0 else "Sur demande"
            except: price_display = "Sur demande"
            
            grid_html += f'''            <a href="produits/{p['handle']}.html" style="text-decoration:none; color:inherit;">
                <div class="card reveal">
                    <div class="card-img-wrapper"><img src="{img}"></div>
                    <span class="kicker" style="font-size: 0.6rem; letter-spacing: 0.3em; opacity: 0.7;">{cat_name.upper()}</span>
                    <h3 style="margin-top: 0.5rem;">{p['title']}</h3>
                    <p style="color:var(--muted); font-size:0.7rem; margin-top: 0.5rem; opacity: 0.8;">{price_display}</p>
                </div>
            </a>\n'''
        grid_html += '        </div>'
        
        filename = cat_name.lower().replace(" ", "-").replace("'", "").replace("é", "e").replace("à", "a") + ".html"
        full_html = header_html + hero_html + grid_html + footer_html
        full_html = re.sub(r'<title>.*?</title>', f'<title>{title} — Elke Berr Genève</title>', full_html)
        with open(filename, 'w', encoding='utf-8') as f: f.write(full_html)
        print(f"Generated: {filename} ({len(prods)} items)")

if __name__ == "__main__":
    generate_sorted_collections()
