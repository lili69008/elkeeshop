
import pandas as pd
import os
from PIL import Image
import json

def get_dominant_color(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        img = img.resize((1, 1))
        color = img.getpixel((0, 0))
        return color
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def classify_background(color):
    if color is None:
        return "Unknown"
    r, g, b = color
    # Simple classification
    if r > 240 and g > 240 and b > 240:
        return "White"
    if r < 50 and g < 50 and b < 50:
        return "Black"
    return "Lifestyle"

def get_collection(handle, title):
    handle = handle.lower()
    title = title.lower()
    
    if any(k in handle for k in ['unbreakable', 'ubreakable', 'phoenix', 'imperium', 'olympia']):
        return "Unbreakable"
    if 'rock-n-rose' in handle:
        return "Rock'N Rose"
    if 'mysteria' in handle:
        return "Mysteria"
    if any(k in handle for k in ['ondes', 'waves']):
        return "Waves"
    if any(k in handle for k in ['essentiel', 'complice', 'echo', 'epure', 'me-you', 'l-anamour', 'linfini']):
        return "Essentials"
    if any(k in handle for k in ['singular', 'african', 'alma', 'amazonia', 'safari', 'tanzania', 'umba', 'mogok']):
        return "Singular"
    
    # Default to Essentials or "Other"
    return "High Jewelry"

# Load CSV
df = pd.read_csv('localhost_v2/products.csv')

# Filter to keep only one row per product (handles are repeated for variants)
df_unique = df.drop_duplicates(subset=['Handle']).copy()

catalog = []

for index, row in df_unique.iterrows():
    handle = str(row['Handle'])
    title = str(row['Title'])
    collection = get_collection(handle, title)
    
    # Find main image path
    img_dir = os.path.join('localhost_v2/img/produits', handle)
    bg_class = "White" # Default
    
    if os.path.exists(img_dir):
        images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        if images:
            # Sort to get the first one (usually the main one)
            images.sort()
            main_img_path = os.path.join(img_dir, images[0])
            color = get_dominant_color(main_img_path)
            bg_class = classify_background(color)
            
    catalog.append({
        'handle': handle,
        'title': title,
        'collection': collection,
        'background': bg_class,
        'type': row['Type']
    })

# Save to JSON
with open('catalog_structure.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=4, ensure_ascii=False)

print(f"Processed {len(catalog)} products.")
