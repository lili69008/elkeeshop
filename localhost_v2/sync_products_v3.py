import csv
import os
import re
import html
import json
from deep_translator import GoogleTranslator

TEMPLATE_PATH = "templates/product_template.html"
CSV_PATH = "products.csv"
OUTPUT_ROOT = "produits"
IMG_ROOT = "img/produits"
CACHE_PATH = "translation_cache.json"

# Material extraction rules
METALS = ["Or 18K", "Or Gris", "Or Blanc", "Or Jaune", "Or Rose", "Argent 925", "Argent Rhodié", "Platine", "Rhodium-plated"]
STONES = ["Diamant", "Saphir", "Rubis", "Émeraude", "Onyx", "Spinel", "Spinelle", "Zirconia", "Topaze", "Perle", "Nacre", "Tourmaline", "Tanzanite", "Quartz"]

def load_cache():
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            try: return json.load(f)
            except: return {}
    return {}

def save_cache(cache):
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

TRANSLATION_CACHE = load_cache()

def extract_metal(text, shopify_metal=""):
    if shopify_metal and shopify_metal.strip():
        m_val = shopify_metal.strip()
        if m_val.lower() == "argent": return "Argent 925 Rhodié"
        return m_val
    for m in METALS:
        if re.search(rf"\b{m}\b", text, re.IGNORECASE):
            return m
    return "Or 18K / Argent Rhodié"

def extract_stones(text):
    found = []
    for s in STONES:
        if re.search(rf"\b{s}\b", text, re.IGNORECASE):
            found.append(s)
    return ", ".join(list(set(found))) if found else "Pierres fines"

def translate_to_fr(text):
    if not text or text.strip() == "": return ""
    if text in TRANSLATION_CACHE: return TRANSLATION_CACHE[text]
    try:
        translator = GoogleTranslator(source='auto', target='fr')
        translated = translator.translate(text)
        TRANSLATION_CACHE[text] = translated
        return translated
    except: return text

def sync():
    if not os.path.exists(TEMPLATE_PATH): return
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    products = {}
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            handle = row.get("Handle")
            if not handle: continue
            
            if handle not in products:
                raw_body = row.get("Body (HTML)", "")
                shopify_metal = row.get("Jewelry material (product.metafields.shopify.jewelry-material)", "")
                
                # Special cases
                if "unbreakable" in handle.lower() or "phoenix" in handle.lower():
                    if not shopify_metal: shopify_metal = "Argent 925 Rhodié"
                
                products[handle] = {
                    "handle": handle,
                    "title": row.get("Title", handle),
                    "desc": translate_to_fr(raw_body),
                    "price": row.get("Variant Price", "0"),
                    "type": row.get("Type", "Bijoux"),
                    "metal": extract_metal(raw_body, shopify_metal),
                    "stones": extract_stones(raw_body),
                    "shopify_imgs": []
                }
            
            img = row.get("Image Src")
            if img: products[handle]["shopify_imgs"].append(img)

    for handle, p in products.items():
        if "unbreakable" in handle.lower() or "phoenix" in handle.lower() or "imperium" in handle.lower() or "olympia" in handle.lower():
            target_dir = os.path.join(OUTPUT_ROOT, "unbreakable")
            base_url = "../../"
        else:
            target_dir = OUTPUT_ROOT
            base_url = "../"

        if not os.path.exists(target_dir): os.makedirs(target_dir)

        local_img_dir = os.path.join(IMG_ROOT, handle)
        final_images = []
        if os.path.exists(local_img_dir):
            local_files = [f for f in os.listdir(local_img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for lf in sorted(local_files):
                final_images.append(f"{base_url}img/produits/{handle}/{lf}")
        
        for si in p["shopify_imgs"]:
            if len(final_images) >= 6: break
            if si not in final_images: final_images.append(si)

        html_content = template
        html_content = html_content.replace("{{PRODUCT_TITLE}}", p["title"])
        html_content = html_content.replace("{{PRODUCT_DESC}}", p["desc"])
        html_content = html_content.replace("{{PRODUCT_COLLECTION}}", p["type"].upper())
        
        try:
            val = float(p["price"].replace(",", ""))
            price_str = f"{val:,.2f} CHF" if val > 0 else "Sur demande"
        except: price_str = "Sur demande"
        html_content = html_content.replace("{{PRODUCT_PRICE}}", price_str)
        
        html_content = html_content.replace("{{PRODUCT_METAL}}", p["metal"])
        html_content = html_content.replace("{{PRODUCT_PIERRES}}", p["stones"])
        html_content = html_content.replace("{{PRODUCT_ORIGINE}}", "Ateliers Genevois")
        
        img1 = final_images[0] if final_images else f"{base_url}img/bague_saphir.png"
        html_content = html_content.replace("{{PRODUCT_IMAGE_1}}", img1)
        
        img_blocks = ""
        for i in range(1, len(final_images)):
            img_blocks += f'<img src="{final_images[i]}" alt="{p["title"]} vue {i+1}" class="reveal" style="margin-top:2rem;">\n'
        html_content = html_content.replace("{{PRODUCT_IMAGE_2_BLOCK}}", img_blocks)

        html_content = html_content.replace('href="../', f'href="{base_url}')
        html_content = html_content.replace('src="../', f'src="{base_url}')

        filename = os.path.join(target_dir, f"{handle}.html")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Synced: {handle}")

    save_cache(TRANSLATION_CACHE)
    print("Full Sync Complete.")

if __name__ == "__main__":
    sync()
