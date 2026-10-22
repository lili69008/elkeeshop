import re
import csv
import os

CSV_PATH = "products.csv"
HJ_LANDING = "haute-joaillerie.html"

# Titles, kickers and descriptions for High Jewelry collections
HJ_COLLECTIONS = {
    "Bagues": {
        "title": "LES BAGUES D'EXCEPTION",
        "kicker": "HAUTE JOAILLERIE",
        "desc": "Les bagues Elke Berr sont des créations d'exception où la pierre précieuse est au cœur de l'œuvre. Chaque bague raconte une histoire unique, mêlant expertise gemmologique et design raffiné.",
        "filename": "haute-joaillerie-bagues.html"
    },
    "Colliers": {
        "title": "LES COLLIERS D'EXCEPTION",
        "kicker": "HAUTE JOAILLERIE",
        "desc": "Découvrez nos colliers et pendentifs d'exception, alliant la rareté de pierres précieuses minutieusement sélectionnées par Elke Berr à la pureté des lignes de Haute Joaillerie.",
        "filename": "haute-joaillerie-colliers.html"
    },
    "Boucles d'oreilles": {
        "title": "LES BOUCLES D'OREILLES D'EXCEPTION",
        "kicker": "HAUTE JOAILLERIE",
        "desc": "Des pièces majestueuses et des boucles d'oreilles uniques façonnées autour de gemmes exceptionnelles, capturant la lumière avec éclat et grâce.",
        "filename": "haute-joaillerie-boucles-doreilles.html"
    },
    "Bracelets": {
        "title": "LES BRACELETS D'EXCEPTION",
        "kicker": "HAUTE JOAILLERIE",
        "desc": "Des bracelets et parures de poignet uniques, où la fluidité du métal précieux sublime l'éclat des plus belles gemmes naturelles.",
        "filename": "haute-joaillerie-bracelets.html"
    }
}

def clean_hj_landing():
    if not os.path.exists(HJ_LANDING):
        print(f"Error: {HJ_LANDING} not found.")
        return False
        
    with open(HJ_LANDING, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if there is duplication by counting occurrences of 'white-black-blues-ring.html'
    occurrences = content.count("white-black-blues-ring.html")
    if occurrences > 1:
        print(f"Detected duplication in {HJ_LANDING} ({occurrences} occurrences). Cleaning...")
        end_first_grid = content.find("white-black-blues-ring.html")
        if end_first_grid != -1:
            idx_close = content.find("</a></div>", end_first_grid)
            if idx_close != -1:
                grid_end_pos = idx_close + len("</a></div>")
                footer_pos = content.find('<footer class="site-footer">')
                if footer_pos != -1:
                    cleaned_content = content[:grid_end_pos] + "\n    </section>\n\n    " + content[footer_pos:]
                    with open(HJ_LANDING, "w", encoding="utf-8") as out:
                        out.write(cleaned_content)
                    print(f"Successfully cleaned {HJ_LANDING} and removed duplicate product grid block.")
                    return True
    return False

def get_hj_category(handle, title):
    h = handle.lower()
    t = title.lower()
    combined = h + " " + t
    
    if "earring" in combined or "boucle" in combined or "stud" in combined or "ear-cuff" in combined or "earcuff" in combined or "ear cuff" in combined:
        return "Boucles d'oreilles"
    if "necklace" in combined or "collier" in combined or "choker" in combined or "pendant" in combined or "pendentif" in combined:
        return "Colliers"
    if "ring" in combined or "bague" in combined or "phalanx" in combined or "finger-top" in combined or "amore" in combined:
        return "Bagues"
    if "bracelet" in combined or "bangle" in combined or "cuff" in combined or "cufflinks" in combined or "manchette" in combined or "recif" in combined or "sensuelle" in combined or "tegula" in combined:
        return "Bracelets"
        
    # Default fallbacks
    if "olympia" in combined: return "Colliers"
    if "imperium" in combined: return "Colliers"
    if "phoenix" in combined: return "Colliers"
    
    return "Bagues"

def run_hj_generation():
    # First clean landing page if duplicated
    clean_hj_landing()
    
    with open(HJ_LANDING, "r", encoding="utf-8") as f:
        landing_html = f.read()
        
    # Extract header up to the first section of landing page
    header_match = re.search(r'(.*?)<section class="reveal"\s+style="padding-top:\s*18rem;', landing_html, re.DOTALL)
    if not header_match:
        print("Could not find header pattern in haute-joaillerie.html")
        return
    header_html = header_match.group(1)
    
    # Extract footer starting from footer element
    footer_match = re.search(r'(<footer class="site-footer">.*)', landing_html, re.DOTALL)
    if not footer_match:
        print("Could not find footer pattern in haute-joaillerie.html")
        return
    footer_html = footer_match.group(1)
    
    # Let's read products.csv to get prices
    prices = {}
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r", encoding="utf-8", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                handle = row.get("Handle", "")
                price = row.get("Variant Price", "")
                if handle and price:
                    if handle not in prices or (prices[handle] == "0" or prices[handle] == ""):
                        prices[handle] = price

    # Parse all product cards in haute-joaillerie.html
    card_regex = re.compile(
        r'<a\s+href="produits/high-jewelry/(?P<handle>[\w-]+)\.html"\s+style="text-decoration:none;\s*color:inherit;"\s+class="(?P<bg_class>[^"]+)">\s*'
        r'<div class="card reveal">\s*'
        r'<div class="card-img-wrapper"><img src="(?P<img_src>[^"]+)"></div>\s*'
        r'<span class="kicker">[^<]+</span>\s*'
        r'<h3>(?P<title>[^<]+)</h3>',
        re.DOTALL
    )
    
    cards = []
    for m in card_regex.finditer(landing_html):
        cards.append({
            "handle": m.group("handle"),
            "bg_class": m.group("bg_class"),
            "img_src": m.group("img_src"),
            "title": m.group("title").strip()
        })
        
    print(f"Found {len(cards)} High Jewelry product cards in {HJ_LANDING}")
    
    # Categorize cards
    categorized = {
        "Bagues": [],
        "Colliers": [],
        "Boucles d'oreilles": [],
        "Bracelets": []
    }
    
    for c in cards:
        cat = get_hj_category(c["handle"], c["title"])
        if cat in categorized:
            categorized[cat].append(c)
        else:
            categorized["Bagues"].append(c) # fallback
            
    # For each category, generate page
    for cat_name, items in categorized.items():
        info = HJ_COLLECTIONS[cat_name]
        print(f"Category '{cat_name}': {len(items)} items")
        
        # Build hero section with class="reveal" to ensure it's immediately visible
        # Note: both hero and grid sections will have class="reveal" for bulletproof visibility
        hero_html = f"""    <section class="reveal" style="padding-top: 18rem; padding-bottom: 8rem; text-align: center;">
        <span class="kicker">{info['kicker']}</span>
        <h1 style="font-size: clamp(2.5rem, 5vw, 4rem); letter-spacing: 0.25em; font-weight: 400; margin-bottom: 3rem;">{info['title']}</h1>
        <div style="width: 40px; height: 1px; background: var(--fg); margin: 0 auto 3rem;"></div>
        <p style="max-width: 650px; margin: 0 auto; line-height: 2; color: var(--muted); font-weight: 300; font-size: 0.95rem; letter-spacing: 0.02em;">{info['desc']}</p>
    </section>\n"""
    
        # Build grid section with class="reveal" to ensure it's immediately visible
        grid_html = '    <section id="catalog-grid" class="reveal" style="padding: 0 8vw 15rem;">\n        <div class="grid-3">\n'
        
        for item in items:
            handle = item["handle"]
            bg_class = item["bg_class"]
            img = item["img_src"]
            title = item["title"]
            
            # Fetch price from CSV
            price_raw = prices.get(handle, "Sur demande")
            if price_raw and price_raw != "0" and price_raw != "Sur demande":
                try:
                    price_val = float(price_raw)
                    price_display = f"{price_val:,.2f} CHF".replace(",", "'")
                except ValueError:
                    price_display = price_raw
            else:
                price_display = "Sur demande"
                
            grid_html += f"""            <a href="produits/high-jewelry/{handle}.html" style="text-decoration:none; color:inherit;" class="{bg_class}">
                <div class="card reveal">
                    <div class="card-img-wrapper"><img src="{img}"></div>
                    <span class="kicker">{cat_name.upper()}</span>
                    <h3>{title}</h3>
                    <p style="color:var(--muted); font-size:0.8rem; margin-top:0.5rem; letter-spacing:0.05em;">{price_display}</p>
                </div>
            </a>\n"""
            
        grid_html += '        </div>\n    </section>\n'
        
        # Assemble full HTML
        full_html = header_html + hero_html + grid_html + footer_html
        
        # Update page title in <head>
        full_html = re.sub(r'<title>.*?</title>', f'<title>{info["title"]} — Elke Berr Genève</title>', full_html)
        
        # Write to file
        with open(info["filename"], "w", encoding="utf-8") as out_f:
            out_f.write(full_html)
        print(f"Generated {info['filename']}")

if __name__ == "__main__":
    run_hj_generation()
