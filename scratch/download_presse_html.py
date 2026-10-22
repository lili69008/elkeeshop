import os
import re
import json
import urllib.request
from urllib.parse import urljoin

def download_press_data():
    url = "https://elkeberr.com/pages/presse"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print(f"Fetching raw HTML from {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

    # Let's save the raw HTML for manual inspection if needed
    os.makedirs('scratch', exist_ok=True)
    with open('scratch/raw_presse.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved raw HTML to scratch/raw_presse.html")

    # Let's find all images on the page
    # Shopify usually has images inside divs with classes or inside img tags with src/srcset
    # We can use regex to find img tags
    img_tags = re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', html)
    print(f"Found {len(img_tags)} simple img tags.")

    # We also want to find article entries
    # Let's search for articles, titles, and text
    # In the markdown we saw titles like "INCOLOR 2025", "Luxury Magazine 2024", etc.
    # Let's see how they are structured in HTML. Let's do a search for one of them in the raw HTML.
    
    # We can print some statistics and save the file
    # Let's extract sections that look like article grids or paragraphs
    
if __name__ == "__main__":
    download_press_data()
