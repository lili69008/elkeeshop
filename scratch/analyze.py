import os
from bs4 import BeautifulSoup

handles = [
    "phoenix-necklace-copie", "unbreakable-necklace-gold-diamonds",
    "imperium-necklace-gold", "olympia-copie", "olympia"
]

for h in handles:
    filepath = f"localhost_v2/produits/unbreakable/{h}.html"
    exists = os.path.exists(filepath)
    print(f"Handle: {h} | Path: {filepath} | Exists: {exists}")
    if exists:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Title
        title_el = soup.find('h1', class_='product-title')
        title = title_el.text.strip() if title_el else "No H1 title"
        
        # Price
        price_el = soup.find('div', class_='product-price')
        price = price_el.text.strip() if price_el else "No Price"
        
        # Specs
        specs = {}
        spec_items = soup.find_all('div', class_='spec-item')
        for item in spec_items:
            spans = item.find_all('span')
            if len(spans) == 2:
                specs[spans[0].text.strip()] = spans[1].text.strip()
                
        # Image
        img_el = soup.find('div', class_='product-gallery')
        img_src = ""
        if img_el:
            first_img = img_el.find('img')
            if first_img:
                img_src = first_img.get('src', '')
        
        print(f"  Title: {title}")
        print(f"  Price: {price}")
        print(f"  Image: {img_src}")
        print(f"  Specs: {specs}")
        print("-" * 50)
