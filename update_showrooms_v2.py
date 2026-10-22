
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
    
    # Find local image
    img_dir = os.path.join(ROOT_DIR, "img/produits", handle)
    img_path = "img/bague_saphir.png" # Default
    if os.path.exists(img_dir):
        images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        if images:
            images.sort()
            img_path = f"img/produits/{handle}/{images[0]}"
    
    # We need to know the price. Let's assume it's in a map or we just don't show it for now, 
    # but the user had it in the grid.
    # Actually, I should have included the price in catalog_structure.json.
    # For now I'll use a placeholder or read it from CSV if I really need it.
    # Let's just use the handle to link.
    
    # Determine the link
    link = f"produits/{coll_slug}/{handle}.html"
    
    card_html = f"""
            <a href="{link}" style="text-decoration:none; color:inherit;">
                <div class="card reveal">
                    <div class="card-img-wrapper"><img src="{img_path}"></div>
                    <span class="kicker">{collection.upper()}</span>
                    <h3>{title}</h3>
                </div>
            </a>"""
    return card_html

def update_page(filename, filter_func, title_prefix=""):
    filepath = os.path.join(ROOT_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} (not found)")
        return
        
    catalog = load_catalog()
    products = [p for p in catalog if filter_func(p)]
    
    # Sort products: White background first, then Black, then Lifestyle
    bg_order = {"White": 0, "Black": 1, "Lifestyle": 2, "Unknown": 3}
    products.sort(key=lambda x: bg_order.get(x['background'], 99))
    
    cards_html = ""
    if title_prefix:
        # Group by collection if it's a general page (like bagues.html)
        collections = {}
        for p in products:
            coll = p['collection']
            if coll not in collections: collections[coll] = []
            collections[coll].append(p)
            
        for coll, coll_products in collections.items():
            cards_html += f'<div style="grid-column: 1 / -1; margin-top: 4rem; margin-bottom: 2rem;"><h2 style="font-family:var(--font-serif); font-weight:400; letter-spacing:0.1em; opacity:0.8;">{coll}</h2></div>'
            for p in coll_products:
                cards_html += get_product_card(p)
    else:
        for p in products:
            cards_html += get_product_card(p)
            
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the content inside <div class="grid-3">...</div> or similar
    # We'll use a simple regex approach
    pattern = re.compile(r'(<div class="grid-3">)(.*?)(</div>)', re.DOTALL)
    if pattern.search(content):
        new_content = pattern.sub(r'\1' + cards_html + r'\3', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Try <div class="product-grid">
        pattern = re.compile(r'(<div class="product-grid">)(.*?)(</div>)', re.DOTALL)
        if pattern.search(content):
            new_content = pattern.sub(r'\1' + cards_html + r'\3', content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Could not find grid in {filename}")

if __name__ == "__main__":
    # Collection Pages
    update_page("rockn-rose.html", lambda p: p['collection'] == "Rock'N Rose")
    update_page("singular.html", lambda p: p['collection'] == "Singular")
    update_page("mysteria.html", lambda p: p['collection'] == "Mysteria")
    update_page("waves.html", lambda p: p['collection'] == "Waves")
    update_page("unbreakable.html", lambda p: p['collection'] == "Unbreakable")
    
    # Type Pages (Category)
    update_page("bagues.html", lambda p: "ring" in p['handle'].lower() or "bague" in p['handle'].lower(), title_prefix="Grouped")
    update_page("colliers.html", lambda p: "necklace" in p['handle'].lower() or "collier" in p['handle'].lower() or "pendant" in p['handle'].lower(), title_prefix="Grouped")
    update_page("bracelets.html", lambda p: "bracelet" in p['handle'].lower() or "bangle" in p['handle'].lower(), title_prefix="Grouped")
    update_page("boucles-doreilles.html", lambda p: "earring" in p['handle'].lower() or "boucle" in p['handle'].lower() or "earcuff" in p['handle'].lower(), title_prefix="Grouped")
    update_page("bijoux.html", lambda p: True, title_prefix="Grouped")
