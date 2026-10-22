
import csv
import os
import json
import shutil

TEMPLATE_PATH = "localhost_v2/templates/product_template.html"
CSV_PATH = "localhost_v2/products.csv"
OUTPUT_DIR = "localhost_v2/produits"
CATALOG_JSON = "catalog_structure.json"

def load_catalog():
    with open(CATALOG_JSON, 'r', encoding='utf-8') as f:
        return {item['handle']: item for item in json.load(f)}

def generate_pages():
    catalog = load_catalog()
    
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    # Clear old produits dir? Or just overwrite.
    # We might want to clear it to avoid stale files.
    # But let's be careful.
    
    print("Generating product pages in hierarchical structure...")
    
    processed_handles = set()
    
    with open(CSV_PATH, "r", encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            handle = row.get("Handle", "")
            if not handle or handle in processed_handles:
                continue
            
            processed_handles.add(handle)
            info = catalog.get(handle)
            if not info:
                continue
                
            collection = info['collection']
            # Safe folder name
            coll_folder = collection.lower().replace(" ", "-").replace("'", "")
            
            target_dir = os.path.join(OUTPUT_DIR, coll_folder)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            save_product_page(row, info, template, target_dir)

def save_product_page(row, info, template, target_dir):
    handle = info['handle']
    title = info['title']
    collection = info['collection']
    
    html = template
    html = html.replace("{{PRODUCT_TITLE}}", title)
    
    # Body (HTML) might be empty in the current row if it's a variant row, 
    # but we filtered unique handles in catalog_structure.
    # Actually, analyze_catalog.py already has the title. 
    # Let's get the description from the CSV row.
    desc = row.get("Body (HTML)", "Description non disponible.")
    html = html.replace("{{PRODUCT_DESC}}", desc)
    html = html.replace("{{PRODUCT_COLLECTION}}", collection.upper())
    
    price = row.get("Variant Price", "0")
    try:
        price_val = float(str(price).replace(",", ""))
        price_display = f"{price_val:,.2f} CHF".replace(",", "'") if price_val > 0 else "Sur demande"
    except:
        price_display = "Sur demande"
    
    html = html.replace("{{PRODUCT_PRICE}}", price_display)
    
    # Fix relative paths (CSS, JS, Links)
    # The template has ../ for one level. We are at produits/coll/handle.html (3 levels from root)
    # Wait, the template is at localhost_v2/templates/product_template.html.
    # If the page is at localhost_v2/produits/collection/handle.html, then:
    # index.html is at ../../../index.html
    # css/ is at ../../../css/
    # img/ is at ../../../img/
    
    html = html.replace('href="../', 'href="../../../')
    html = html.replace('src="../', 'src="../../../')
    
    # Local Images
    img_dir_rel = f"../../img/produits/{handle}"
    img_dir_abs = os.path.join("localhost_v2/img/produits", handle)
    
    images = []
    if os.path.exists(img_dir_abs):
        images = [f for f in os.listdir(img_dir_abs) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        images.sort()
    
    if images:
        img1 = f"{img_dir_rel}/{images[0]}"
        html = html.replace("{{PRODUCT_IMAGE_1}}", img1)
        
        if len(images) > 1:
            img2 = f"{img_dir_rel}/{images[1]}"
            img2_block = f'<img src="{img2}" alt="{title} vue 2" class="reveal" style="margin-top:2rem;">'
            html = html.replace("{{PRODUCT_IMAGE_2_BLOCK}}", img2_block)
        else:
            html = html.replace("{{PRODUCT_IMAGE_2_BLOCK}}", "")
    else:
        html = html.replace("{{PRODUCT_IMAGE_1}}", "../../../img/bague_saphir.png")
        html = html.replace("{{PRODUCT_IMAGE_2_BLOCK}}", "")

    filename = os.path.join(target_dir, f"{handle}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    generate_pages()
