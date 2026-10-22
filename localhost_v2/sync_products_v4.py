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

# Extraction Lists
METALS = ["Or Blanc", "Or Jaune", "Or Rose", "Or Gris", "Argent 925", "Argent Rhodié", "Platine", "Rhodium", "Silver", "Gold", "Or 18K"]
STONES = ["Diamant", "Saphir", "Rubis", "Émeraude", "Onyx", "Spinel", "Spinelle", "Zirconia", "Topaze", "Perle", "Nacre", "Tourmaline", "Tanzanite", "Quartz", "Lapis", "Malachite", "Turquoise"]

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
    s_low = (shopify_metal or "").lower()
    t_low = text.lower()
    
    if "argent" in s_low or "silver" in s_low or "rhodium" in s_low or "rhodié" in s_low: return "Argent 925 Rhodié"
    if "or blanc" in s_low or "white gold" in s_low or "or blanc" in t_low: return "Or Blanc 18K"
    if "or jaune" in s_low or "yellow gold" in s_low or "or jaune" in t_low: return "Or Jaune 18K"
    if "or rose" in s_low or "rose gold" in s_low or "or rose" in t_low: return "Or Rose 18K"
    if "platine" in s_low or "platinum" in s_low: return "Platine 950"
    
    for m in METALS:
        if re.search(rf"\b{m}\b", text, re.IGNORECASE):
            if "Argent" in m or "Silver" in m: return "Argent 925 Rhodié"
            return m
    return "Or 18K / Argent Rhodié"

def extract_stones(text, title=""):
    found = []
    combined = (text + " " + title).lower()
    mapping = {"spinel": "Spinelle", "zirconia": "Zirconia", "diamond": "Diamant", "sapphire": "Saphir", "ruby": "Rubis", "emerald": "Émeraude"}
    
    for key, val in mapping.items():
        if key in combined: found.append(val)
    
    for s in STONES:
        if s.lower() in combined: found.append(s)
            
    return ", ".join(list(set(found))) if found else "Pierres Précieuses"

def translate_to_fr(text):
    if not text or text.strip() == "": return ""
    if text in TRANSLATION_CACHE: return TRANSLATION_CACHE[text]
    try:
        translator = GoogleTranslator(source='auto', target='fr')
        translated = translator.translate(text)
        TRANSLATION_CACHE[text] = translated
        return translated
    except: return text

def classify_option(opt_name, values):
    name_low = opt_name.lower()
    color_keywords = ['color', 'colour', 'couleur', 'metal', 'métal', 'or', 'gold', 'pierre', 'stone']
    size_keywords = ['size', 'taille', 'longueur', 'length', 'tour', 'dimension']
    
    if any(k in name_low for k in color_keywords):
        return 'color'
    if any(k in name_low for k in size_keywords):
        return 'size'
        
    color_val_keywords = ['gold', 'rose', 'jaune', 'blanc', 'white', 'yellow', 'silver', 'argent', 'rhodium', 'platinum', 'platine', 'onyx', 'spinel', 'spinelle']
    if any(any(cv in str(val).lower() for cv in color_val_keywords) for val in values):
        return 'color'
        
    return 'other'

def get_base_filename(url):
    if not url: return ''
    clean_url = url.split('?')[0]
    return clean_url.split('/')[-1].lower()

def find_image_index(row, final_images):
    vimg = row.get('Variant Image')
    isrc = row.get('Image Src')
    
    for img_url in [vimg, isrc]:
        if not img_url: continue
        base_target = get_base_filename(img_url)
        if not base_target: continue
        
        for idx, img in enumerate(final_images):
            if base_target == get_base_filename(img):
                return idx
    return -1

def get_metallic_hex_and_label(val):
    val_low = val.lower()
    
    if 'rose' in val_low or 'pink' in val_low:
        return '#EBC4B7', 'Or Rose 18ct', 'Or Rose 18k'
    if 'jaune' in val_low or 'yellow' in val_low or ('or' in val_low and 'blanc' not in val_low and 'rose' not in val_low):
        return '#DCA637', 'Or Jaune 18ct', 'Or Jaune 18k'
    if 'blanc' in val_low or 'white' in val_low or 'rhodium' in val_low or 'gris' in val_low:
        return '#DCDCDC', 'Or Blanc 18ct', 'Or Blanc 18k'
    if 'argent' in val_low or 'silver' in val_low:
        return '#CCCCCC', 'Argent 925', 'Argent 925 Rhodié'
    if 'platine' in val_low or 'platinum' in val_low:
        return '#E5E5E5', 'Platine 950', 'Platine 950'
    if 'onyx' in val_low or 'black' in val_low or 'noir' in val_low:
        return '#111111', 'Onyx Noir', 'Onyx'
    if 'nacre' in val_low or 'white' in val_low or 'blanc' in val_low:
        return '#F0EFEA', 'Nacre Blanche', 'Nacre'
    if 'spinelle' in val_low or 'spinel' in val_low:
        return '#4A1525', 'Spinelle Noir', 'Spinelle'
    if 'saphir' in val_low or 'sapphire' in val_low:
        return '#0F2C59', 'Saphir Bleu', 'Saphir'
    if 'rubis' in val_low or 'ruby' in val_low:
        return '#9B111E', 'Rubis', 'Rubis'
    if 'emeraude' in val_low or 'emerald' in val_low:
        return '#097969', 'Émeraude', 'Émeraude'
        
    return '#D4AF37', val, val

def sync():
    if not os.path.exists(TEMPLATE_PATH): return
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    products = {}
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            handle = row.get('Handle')
            if not handle: continue
            
            if handle not in products:
                raw_body = row.get('Body (HTML)', '')
                shopify_metal = row.get('Jewelry material (product.metafields.shopify.jewelry-material)', '')
                title = row.get('Title', handle)
                
                products[handle] = {
                    'handle': handle,
                    'title': title,
                    'desc': translate_to_fr(raw_body),
                    'price': row.get('Variant Price', '0'),
                    'type': row.get('Type', 'Bijoux'),
                    'metal': extract_metal(raw_body, shopify_metal),
                    'stones': extract_stones(raw_body, title),
                    'shopify_imgs': [],
                    'variant_rows': []
                }
            
            products[handle]['variant_rows'].append(row)
            
            img = row.get('Image Src')
            if img and img not in products[handle]['shopify_imgs']: 
                products[handle]['shopify_imgs'].append(img)
            vimg = row.get('Variant Image')
            if vimg and vimg not in products[handle]['shopify_imgs']: 
                products[handle]['shopify_imgs'].append(vimg)

    # Map product handles to their legacy category directories for 100% navigation compatibility
    SUBDIR_MAPPING = {
        'african-flame-ring': 'singular',
        'alma-ring': 'singular',
        'amazonia-ring': 'singular',
        'amor-bangle': 'high-jewelry',
        'aqua-necklace': 'high-jewelry',
        'aqua-ring': 'high-jewelry',
        'ardoise-necklace': 'high-jewelry',
        'azura-necklace': 'high-jewelry',
        'bague-rubis-amore': 'high-jewelry',
        'bond-earrings': 'high-jewelry',
        'bonnie-clyde-ring': 'high-jewelry',
        'bracelet-unbreakable': 'unbreakable',
        'bubble-cufflinks-white-gold': 'high-jewelry',
        'bubble-cufflinks-yellow-gold': 'high-jewelry',
        'burmese-dream-ring': 'high-jewelry',
        'calchedony-earrings': 'high-jewelry',
        'calla-lily-earrings': 'high-jewelry',
        'caramelle-ring': 'high-jewelry',
        'complice-bangle': 'essentials',
        'constellation-necklace': 'high-jewelry',
        'coral-ring': 'high-jewelry',
        'cosmos-ring': 'high-jewelry',
        'crimson-charm-ring': 'high-jewelry',
        'crimson-sunset-earrings': 'high-jewelry',
        'daydreaming-necklace': 'high-jewelry',
        'deep-blue-pendant': 'high-jewelry',
        'deep-blue-ring': 'high-jewelry',
        'delicate-necklace': 'high-jewelry',
        'diabolo-earrings': 'high-jewelry',
        'dolce-noche-ring': 'high-jewelry',
        'douceur-earcuff': 'high-jewelry',
        'dr-jekyll-mr-hyde-earrings': 'high-jewelry',
        'dramatica-ring': 'high-jewelry',
        'echo-bangle': 'essentials',
        'eclat-earrings': 'high-jewelry',
        'eleganza-necklace': 'high-jewelry',
        'elisa-ear-cuff': 'high-jewelry',
        'epure-necklace': 'essentials',
        'essentiel-bangle': 'essentials',
        'eternity-necklace': 'high-jewelry',
        'himalaya-ring': 'high-jewelry',
        'hold-up-ear-cuff': 'high-jewelry',
        'icefall-earrings': 'high-jewelry',
        'imperium': 'unbreakable',
        'imperium-necklace-gold': 'unbreakable',
        'initials-s-g-necklace': 'high-jewelry',
        'kiss-me-necklace': 'high-jewelry',
        'l-anamour-bracelet': 'essentials',
        'l-anamour-bracelet-bespoke': 'essentials',
        'l-anamour-bracelet-made-to-order-black-gold-copie': 'essentials',
        'l-anamour-bracelet-made-to-order-copie': 'essentials',
        'l-anamour-bracelet-made-to-order-copie-copie': 'essentials',
        'la-belle-et-le-blues-ring': 'high-jewelry',
        'lacryma-ring': 'high-jewelry',
        'lagoon-ring': 'high-jewelry',
        'lanthracite-necklace': 'high-jewelry',
        'les-inseparables-earrings': 'high-jewelry',
        'linfini-necklace': 'essentials',
        'link-earrings': 'high-jewelry',
        'lotus-ring': 'high-jewelry',
        'loulou-earrings-1': 'high-jewelry',
        'loulou-necklace': 'high-jewelry',
        'love-potion-ring': 'high-jewelry',
        'lueur-ring': 'high-jewelry',
        'luna-ring': 'high-jewelry',
        'madame-iceberg-earrings': 'high-jewelry',
        'me-you-necklace': 'essentials',
        'me-you-necklace-mini': 'essentials',
        'me-you-necklace-mother-of-pearl': 'essentials',
        'me-you-necklace-mother-of-pearl-silver-1': 'essentials',
        'me-you-necklace-original': 'essentials',
        'melody-necklace': 'high-jewelry',
        'mermaid-earrings': 'high-jewelry',
        'mogok-ring': 'singular',
        'mysteria-ring': 'mysteria',
        'nefertity-earrings': 'high-jewelry',
        'negative-blues-necklace': 'high-jewelry',
        'night-sky-ring': 'high-jewelry',
        'night-sky-ring-black': 'high-jewelry',
        'nova-phalanx-ring': 'high-jewelry',
        'nymphe-ring': 'high-jewelry',
        'olympia': 'unbreakable',
        'olympia-copie': 'unbreakable',
        'ombre-celeste-ring': 'high-jewelry',
        'ondes-ring': 'waves',
        'onyx-cufflinks': 'high-jewelry',
        'orbis-lacteus-earrings': 'high-jewelry',
        'orbis-lacteus-ring': 'high-jewelry',
        'orchid-ring': 'high-jewelry',
        'ouranos-ring': 'high-jewelry',
        'phoenix': 'unbreakable',
        'phoenix-earrings': 'unbreakable',
        'phoenix-necklace-copie': 'unbreakable',
        'phoenix-necklace-onyx': 'unbreakable',
        'phoenix-ring': 'unbreakable',
        'pink-opulence-ring': 'high-jewelry',
        'pivoine-d-amour-ring': 'high-jewelry',
        'prunelle-ring': 'high-jewelry',
        'recif-bracelet': 'high-jewelry',
        'red-s-devotion-ring': 'high-jewelry',
        'requiem-ring': 'high-jewelry',
        'ring-unbreakable': 'unbreakable',
        'rock-n-rose-necklace-diamond': 'rockn-rose',
        'rock-n-rose-necklace-spinel': 'rockn-rose',
        'rosea-ring': 'high-jewelry',
        'safari-neclace': 'singular',
        'sapphire-single-bracelet': 'high-jewelry',
        'sensuelle-bracelet': 'high-jewelry',
        'serenity-earrings': 'high-jewelry',
        'serenity-ring': 'high-jewelry',
        'snake-earrings': 'high-jewelry',
        'snake-necklace': 'high-jewelry',
        'stardust-finger-top-ring': 'high-jewelry',
        'stellar-bloom-ring': 'high-jewelry',
        'sweetheart-necklace': 'high-jewelry',
        'tandem-bracelet': 'high-jewelry',
        'tandem-choker': 'high-jewelry',
        'tandem-earrings': 'high-jewelry',
        'tandem-earrings-studs': 'high-jewelry',
        'tandem-ring': 'high-jewelry',
        'tanzania-ring': 'singular',
        'tegula-bracelet': 'high-jewelry',
        'tella-necklace': 'high-jewelry',
        'tresor-ring': 'high-jewelry',
        'turquoise-cufflinks': 'high-jewelry',
        'twilight-elegance-double-bracelet': 'high-jewelry',
        'twilight-elegance-double-ring': 'high-jewelry',
        'twilight-elegance-earrings': 'high-jewelry',
        'twilight-elegance-necklace': 'high-jewelry',
        'twilight-elegance-necklace-white-gold': 'high-jewelry',
        'twilight-elegance-single-ring': 'high-jewelry',
        'twilight-elegance-single-ring-sapphire': 'high-jewelry',
        'ubreakable-pendant-only': 'unbreakable',
        'umba-ring': 'singular',
        'unbreakable-black-white': 'unbreakable',
        'unbreakable-earrings': 'unbreakable',
        'unbreakable-necklace': 'unbreakable',
        'unbreakable-necklace-gold-diamonds': 'unbreakable',
        'unbreakable-silver': 'unbreakable',
        'unbreakable-white-black': 'unbreakable',
        'whisper-necklace': 'high-jewelry',
        'white-black-blues-bracelet': 'high-jewelry',
        'white-black-blues-ring': 'high-jewelry',
        'yellow-and-gold-phalanx-ring': 'high-jewelry',
        'zephyris-ring': 'high-jewelry',
        'zephyris-ring-1': 'high-jewelry'
    }

    for handle, p in products.items():
        # Determine category subdir
        subdir = SUBDIR_MAPPING.get(handle)
        if not subdir:
            is_unbreakable = any(x in handle.lower() for x in ['unbreakable', 'phoenix', 'imperium', 'olympia', 'pendant'])
            if is_unbreakable: subdir = 'unbreakable'
            elif 'singular' in handle.lower() or 'singular' in p['desc'].lower(): subdir = 'singular'
            elif 'mysteria' in handle.lower() or 'mysteria' in p['desc'].lower(): subdir = 'mysteria'
            elif 'waves' in handle.lower() or 'waves' in p['desc'].lower(): subdir = 'waves'
            elif 'rose' in handle.lower() or 'rose' in p['desc'].lower(): subdir = 'rockn-rose'
            elif 'essentiel' in handle.lower() or 'complice' in handle.lower() or 'anamour' in handle.lower(): subdir = 'essentials'
            else: subdir = 'high-jewelry'

        # Compile BOTH flat and category nested copies to support all showroom navigational patterns
        configs = [
            (os.path.join(OUTPUT_ROOT, subdir), '../../'),
            (OUTPUT_ROOT, '../')
        ]
        
        for target_dir, base_url in configs:
            if not os.path.exists(target_dir): os.makedirs(target_dir)

            local_img_dir = os.path.join(IMG_ROOT, handle)
            final_images = []
            local_filenames = set()
            
            # 1. Add Local Images
            if os.path.exists(local_img_dir):
                local_files = [f for f in os.listdir(local_img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                for lf in sorted(local_files):
                    final_images.append(f'{base_url}img/produits/{handle}/{lf}')
                    local_filenames.add(lf.split('?')[0].lower())
            
            # 2. Add Shopify Images (avoiding duplicates)
            for si in p['shopify_imgs']:
                if len(final_images) >= 8: break  # increased thumbnail limit to support all color variations!
                si_name = si.split('/')[-1].split('?')[0].lower()
                if si_name not in local_filenames:
                    final_images.append(si)

            # 3. Analyze Options and Variants
            opt1_name = ''
            opt2_name = ''
            opt3_name = ''
            for r in p['variant_rows']:
                if r.get('Option1 Name') and not opt1_name: opt1_name = r.get('Option1 Name')
                if r.get('Option2 Name') and not opt2_name: opt2_name = r.get('Option2 Name')
                if r.get('Option3 Name') and not opt3_name: opt3_name = r.get('Option3 Name')

            opt_mappings = {}
            for opt_key, opt_name in [('Option1', opt1_name), ('Option2', opt2_name), ('Option3', opt3_name)]:
                if not opt_name or opt_name.lower() == 'title': continue
                
                vals = []
                for r in p['variant_rows']:
                    val = r.get(f'{opt_key} Value')
                    if val and val != 'Default Title' and val not in vals:
                        vals.append(val)
                
                if not vals: continue
                
                role = classify_option(opt_name, vals)
                opt_mappings[opt_key] = {
                    'name': opt_name,
                    'role': role,
                    'values': vals
                }

            assigned_roles = {}
            for opt_key, opt_data in opt_mappings.items():
                role = opt_data['role']
                if role not in assigned_roles:
                    assigned_roles[role] = opt_key
                else:
                    assigned_roles['other'] = opt_key

            color_opt_key = assigned_roles.get('color')
            size_opt_key = assigned_roles.get('size')
            other_opt_key = assigned_roles.get('other')
            
            has_colors = color_opt_key is not None
            has_sizes = size_opt_key is not None
            has_other = other_opt_key is not None
            
            colors_json = []
            sizes_json = []
            other_json = []
            variants_list = []
            
            if has_colors:
                for val in opt_mappings[color_opt_key]['values']:
                    hex_code, display_lbl, spec_lbl = get_metallic_hex_and_label(val)
                    color_img_idx = -1
                    for r in p['variant_rows']:
                        if r.get(f'{color_opt_key} Value') == val:
                            idx = find_image_index(r, final_images)
                            if idx != -1:
                                color_img_idx = idx
                                break
                    if color_img_idx == -1: color_img_idx = 0
                    
                    colors_json.append({
                        'value': val,
                        'label': translate_to_fr(display_lbl),
                        'hex': hex_code,
                        'spec': spec_lbl,
                        'imageIndex': color_img_idx
                    })

            if has_sizes:
                for val in opt_mappings[size_opt_key]['values']:
                    sizes_json.append({
                        'value': val,
                        'label': val
                    })

            other_name = ''
            if has_other:
                other_name = opt_mappings[other_opt_key]['name']
                for val in opt_mappings[other_opt_key]['values']:
                    other_img_idx = -1
                    for r in p['variant_rows']:
                        if r.get(f'{other_opt_key} Value') == val:
                            idx = find_image_index(r, final_images)
                            if idx != -1:
                                other_img_idx = idx
                                break
                    other_json.append({
                        'value': val,
                        'label': translate_to_fr(val),
                        'imageIndex': other_img_idx
                    })

            for r in p['variant_rows']:
                price = r.get('Variant Price', '0')
                try:
                    val = float(price.replace(',', ''))
                    price_str = f'{val:,.2f} CHF' if val > 0 else 'Sur demande'
                except: price_str = 'Sur demande'
                
                color_val = r.get(f'{color_opt_key} Value') if has_colors else None
                size_val = r.get(f'{size_opt_key} Value') if has_sizes else None
                other_val = r.get(f'{other_opt_key} Value') if has_other else None
                
                variants_list.append({
                    'color': color_val,
                    'size': size_val,
                    'other': other_val,
                    'price': price_str,
                    'imageIndex': find_image_index(r, final_images)
                })

            variants_json_obj = {
                'hasColors': has_colors,
                'hasSizes': has_sizes,
                'hasOther': has_other,
                'otherName': translate_to_fr(other_name) if other_name else '',
                'colors': colors_json,
                'sizes': sizes_json,
                'otherOptions': other_json,
                'variants': variants_list
            }

            # 4. Gallery HTML Construction
            thumbnails_html = ''
            main_images_html = ''
            
            if len(final_images) > 1:
                for idx, img_url in enumerate(final_images):
                    active_class = 'active' if idx == 0 else ''
                    thumbnails_html += f'                    <div class="thumbnail-item {active_class}" data-index="{idx}">\n'
                    thumbnails_html += f'                        <img src="{img_url}" alt="{p["title"]} miniature {idx+1}">\n'
                    thumbnails_html += f'                    </div>\n'
            
            for idx, img_url in enumerate(final_images):
                active_class = 'active' if idx == 0 else ''
                main_images_html += f'                    <img src="{img_url}" id="main-img-{idx}" class="{active_class}" alt="{p["title"]} vue {idx+1}">\n'
                
            if not final_images:
                fallback_img = f'{base_url}img/bague_saphir.png'
                main_images_html = f'                    <img src="{fallback_img}" id="main-img-0" class="active" alt="{p["title"]} vue 1">\n'

            # HTML Generation
            html_content = template
            html_content = html_content.replace('{{PRODUCT_TITLE}}', p['title'])
            html_content = html_content.replace('{{PRODUCT_DESC}}', p['desc'])
            html_content = html_content.replace('{{PRODUCT_COLLECTION}}', p['type'].upper() or 'BIJOUX')
            
            try:
                val = float(p['price'].replace(',', ''))
                price_str = f'{val:,.2f} CHF' if val > 0 else 'Sur demande'
            except: price_str = 'Sur demande'
            html_content = html_content.replace('{{PRODUCT_PRICE}}', price_str)
            
            html_content = html_content.replace('{{PRODUCT_METAL}}', p['metal'])
            html_content = html_content.replace('{{PRODUCT_PIERRES}}', p['stones'])
            html_content = html_content.replace('{{PRODUCT_ORIGINE}}', 'Ateliers Genevois')
            
            html_content = html_content.replace('{{PRODUCT_THUMBNAILS}}', thumbnails_html)
            html_content = html_content.replace('{{PRODUCT_MAIN_IMAGES}}', main_images_html)
            html_content = html_content.replace('{{PRODUCT_VARIANTS_JSON}}', json.dumps(variants_json_obj, ensure_ascii=False, indent=2))

            # Nav Fix
            html_content = html_content.replace('href="../', f'href="{base_url}')
            html_content = html_content.replace('src="../', f'src="{base_url}')

            filename = os.path.join(target_dir, f'{handle}.html')
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
        
        print(f'Synced: {handle}')

    save_cache(TRANSLATION_CACHE)
    print('Audit & Sync Complete.')

if __name__ == '__main__':
    sync()
