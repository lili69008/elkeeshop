import os
import time
from playwright.sync_api import sync_playwright

output_dir = 'c:/Users/lyies/Desktop/siteelk/elkescreen'
os.makedirs(output_dir, exist_ok=True)

pages_to_capture = [
    'index.html',
    'unbreakable.html',
    'private-jeweller.html',
    'haute-joaillerie.html',
    'bijoux.html',
    'news.html',
    'evenements.html',
    'presse.html',
    'maison.html',
    'contact.html',
    # 5 product/collection pages
    'bagues.html',
    'colliers.html',
    'boucles-doreilles.html',
    'bracelets.html',
    'rockn-rose.html'
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.set_default_timeout(15000) # 15 seconds timeout
    
    for filename in pages_to_capture:
        url = f"http://localhost:8090/{filename}"
        print(f"Capturing {filename}...")
        try:
            page.goto(url, wait_until="load")
            # Small wait to allow animations or images to load fully
            page.wait_for_timeout(2000)
            
            output_path = os.path.join(output_dir, filename.replace('.html', '.png'))
            page.screenshot(path=output_path, full_page=True)
            print(f"Saved {output_path}")
        except Exception as e:
            print(f"Error capturing {filename}: {e}")
            
    browser.close()

print("All screenshots captured and saved to elkescreen directory!")
