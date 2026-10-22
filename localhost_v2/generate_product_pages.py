import csv
import os
import time
from deep_translator import GoogleTranslator

TEMPLATE_PATH = "templates/product_template.html"
CSV_PATH = "products.csv"
OUTPUT_DIR = "produits"

# Helper for translation to French
def translate_to_fr(text):
    if not text or text.strip() == "":
        return ""
    try:
        # Simple chunking if text is too long, though usually not for jewelry
        translator = GoogleTranslator(source='auto', target='fr')
        # deep-translator handles HTML decently, but we might need to be careful.
        # We will translate the raw text to ensure perfect French orthography.
        translated = translator.translate(text)
        time.sleep(0.1) # Be nice to the API
        return translated
    except Exception as e:
        print(f"Erreur de traduction pour '{text[:30]}': {e}")
        return text

def generate_pages():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Erreur : Le template {TEMPLATE_PATH} est introuvable.")
        return
        
    if not os.path.exists(CSV_PATH):
        print(f"Erreur : Le fichier CSV {CSV_PATH} est introuvable.")
        return
        
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    print("Début de la génération des pages produits en local (avec traduction Française)...")
    
    generated_count = 0
    with open(CSV_PATH, "r", encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        current_product = None
        
        for row in reader:
            handle = row.get("Handle", "")
            if not handle:
                continue
                
            if current_product is None or current_product["handle"] != handle:
                if current_product is not None:
                    save_product_page(current_product, template)
                    generated_count += 1
                    print(f"Généré : {current_product['title']}")
                
                raw_desc = row.get("Body (HTML)", "Description non disponible.")
                
                # Translate description
                print(f"Traduction en cours pour : {handle}...")
                fr_desc = translate_to_fr(raw_desc)
                
                # Ensure correct categories
                ptype = row.get("Type", "").strip()
                if not ptype:
                    if "ring" in handle.lower() or "bague" in handle.lower(): ptype = "Bagues"
                    elif "necklace" in handle.lower() or "collier" in handle.lower(): ptype = "Colliers"
                    elif "bracelet" in handle.lower() or "bangle" in handle.lower(): ptype = "Bracelets"
                    elif "earring" in handle.lower() or "boucle" in handle.lower(): ptype = "Boucles d'oreilles"
                    elif "pendant" in handle.lower(): ptype = "Pendentifs"
                    else: ptype = "Collection Elke Berr"
                
                # Format the type correctly for French
                type_mapping = {
                    "Ring": "Bagues", "Bague": "Bagues",
                    "Necklace": "Colliers", "Collier": "Colliers",
                    "Bracelet": "Bracelets", "Bangle": "Bracelets",
                    "Earring": "Boucles d'oreilles", "Boucles d'oreilles": "Boucles d'oreilles", "Earrings": "Boucles d'oreilles",
                    "Pendant": "Pendentifs", "Pendentif": "Pendentifs"
                }
                ptype_fr = type_mapping.get(ptype, ptype)

                title = row.get("Title", handle.replace("-", " ").title())

                current_product = {
                    "handle": handle,
                    "title": title,
                    "desc": fr_desc,
                    "type": ptype_fr,
                    "price": row.get("Variant Price", "Sur demande"),
                    "images": []
                }
            
            img_src = row.get("Image Src", "")
            if img_src and img_src not in current_product["images"]:
                current_product["images"].append(img_src)
                
        if current_product is not None:
            save_product_page(current_product, template)
            generated_count += 1
            print(f"Généré : {current_product['title']}")

    print(f"Terminé ! {generated_count} pages produits (en Français) générées dans '{OUTPUT_DIR}'.")

def save_product_page(product, template):
    html = template
    html = html.replace("{{PRODUCT_TITLE}}", product["title"])
    html = html.replace("{{PRODUCT_DESC}}", product["desc"])
    html = html.replace("{{PRODUCT_COLLECTION}}", product["type"].upper())
    
    price = product["price"]
    try:
        price_val = float(str(price).replace(",", ""))
        if price_val == 0:
            price_display = "Sur demande"
        else:
            price_display = f"{price} CHF"
    except:
        price_display = "Sur demande"
    
    html = html.replace("{{PRODUCT_PRICE}}", price_display)
    
    img1 = product["images"][0] if len(product["images"]) > 0 else "../img/bague_saphir.png"
    html = html.replace("{{PRODUCT_IMAGE_1}}", img1)
    
    if len(product["images"]) > 1:
        img2 = product["images"][1]
        img2_block = f'<img src="{img2}" alt="{product["title"]} vue 2" class="reveal" style="margin-top:2rem;">'
        html = html.replace("{{PRODUCT_IMAGE_2_BLOCK}}", img2_block)
    else:
        html = html.replace("{{PRODUCT_IMAGE_2_BLOCK}}", "")

    filename = os.path.join(OUTPUT_DIR, f"{product['handle']}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    generate_pages()
