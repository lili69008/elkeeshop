
import json
import os
import re

CATALOG_JSON = "catalog_structure.json"
ROOT_DIR = "localhost_v2"

def load_catalog():
    with open(CATALOG_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_product_card(product):
    handle = product['handle']
    title = product['title']
    collection = product['collection']
    coll_slug = collection.lower().replace(" ", "-").replace("'", "")
    
    img_dir = os.path.join(ROOT_DIR, "img/produits", handle)
    img_path = "img/bague_saphir.png"
    if os.path.exists(img_dir):
        images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        if images:
            images.sort()
            img_path = f"img/produits/{handle}/{images[0]}"
    
    link = f"produits/{coll_slug}/{handle}.html"
    
    bg_class = f"bg-{product['background'].lower()}"
    
    card_html = f"""
            <a href="{link}" style="text-decoration:none; color:inherit;" class="{bg_class}">
                <div class="card reveal">
                    <div class="card-img-wrapper"><img src="{img_path}"></div>
                    <span class="kicker">{collection.upper()}</span>
                    <h3>{title}</h3>
                </div>
            </a>"""
    return card_html

def update_page(filename, filter_func, group_by_collection=False):
    filepath = os.path.join(ROOT_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} (not found)")
        return
        
    catalog = load_catalog()
    products = [p for p in catalog if filter_func(p)]
    
    bg_order = {"White": 0, "Black": 1, "Lifestyle": 2, "Unknown": 3}
    products.sort(key=lambda x: bg_order.get(x['background'], 99))
    
    cards_html = ""
    if group_by_collection:
        collections = {}
        for p in products:
            coll = p['collection']
            if coll not in collections: collections[coll] = []
            collections[coll].append(p)
            
        for coll, coll_products in collections.items():
            cards_html += f'<div style="grid-column: 1 / -1; margin-top: 6rem; margin-bottom: 2rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem;"><h2 style="font-family:var(--font-serif); font-weight:400; letter-spacing:0.1em; opacity:0.8;">{coll}</h2></div>'
            for p in coll_products:
                cards_html += get_product_card(p)
    else:
        for p in products:
            cards_html += get_product_card(p)
            
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Improved Search for grid markers (div or section)
    grid_found = False
    for tag in ['div', 'section']:
        for marker in ['grid-3', 'product-grid']:
            pattern = re.compile(f'(<{tag} class="{marker}">)(.*?)(</{tag}>)', re.DOTALL)
            if pattern.search(content):
                content = pattern.sub(r'\1' + cards_html + r'\3', content)
                grid_found = True
                break
        if grid_found: break
            
    if grid_found:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        # If it's unbreakable.html and no grid found, we append it before footer
        if filename == "unbreakable.html":
            insertion_point = content.find('<footer>')
            if insertion_point != -1:
                grid_section = f'\n    <section class="product-grid" style="padding: 10rem 8vw;">\n        {cards_html}\n    </section>\n'
                content = content[:insertion_point] + grid_section + content[insertion_point:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Injected and Updated {filename}")
            else:
                print(f"Could not find footer in {filename}")
        else:
            print(f"Could not find grid in {filename}")

if __name__ == "__main__":
    update_page("rockn-rose.html", lambda p: p['collection'] == "Rock'N Rose")
    update_page("singular.html", lambda p: p['collection'] == "Singular")
    update_page("mysteria.html", lambda p: p['collection'] == "Mysteria")
    update_page("waves.html", lambda p: p['collection'] == "Waves")
    update_page("unbreakable.html", lambda p: p['collection'] == "Unbreakable")
    
    update_page("unbreakable-paul.html", lambda p: p['collection'] == "Unbreakable" and ("silver" in p['handle'].lower() or "black" in p['handle'].lower() or "bracelet-unbreakable" in p['handle'].lower()))
    update_page("unbreakable-zulay.html", lambda p: p['collection'] == "Unbreakable" and ("gold" in p['handle'].lower() or "diamond" in p['handle'].lower() or "epure" in p['handle'].lower()))

    update_page("bagues.html", lambda p: "ring" in p['handle'].lower() or "bague" in p['handle'].lower(), group_by_collection=True)
    update_page("colliers.html", lambda p: "necklace" in p['handle'].lower() or "collier" in p['handle'].lower() or "pendant" in p['handle'].lower(), group_by_collection=True)
    update_page("bracelets.html", lambda p: "bracelet" in p['handle'].lower() or "bangle" in p['handle'].lower(), group_by_collection=True)
    update_page("boucles-doreilles.html", lambda p: "earring" in p['handle'].lower() or "boucle" in p['handle'].lower() or "earcuff" in p['handle'].lower(), group_by_collection=True)
    
    update_page("bijoux.html", lambda p: p['collection'] != "High Jewelry", group_by_collection=True)
    update_page("haute-joaillerie.html", lambda p: p['collection'] == "High Jewelry", group_by_collection=True)
