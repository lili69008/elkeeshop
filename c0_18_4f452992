import re
import os

def extract_links():
    filename = "Elke Berr · Files · Shopify.html"
    if not os.path.exists(filename):
        # Try without special characters if encoding/copy-paste changed it
        files = os.listdir('.')
        for f in files:
            if "Files" in f and "Shopify" in f and f.endswith(".html"):
                filename = f
                break
    
    print(f"Reading {filename}...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Broad regex to find all Shopify CDN links (files and videos)
    regex = r'https://cdn\.shopify\.com/(?:s/files|videos)/[^\s\"\'\>]+'
    all_links = re.findall(regex, content)
    
    # Clean and deduplicate
    clean_links = set()
    for link in all_links:
        # Remove query parameters like ?v=...
        base_url = link.split('?')[0]
        # Some URLs might have &amp; or other artifacts
        base_url = base_url.replace('&amp;', '&').replace('"', '').replace("'", "")
        
        # Filter for relevant media types
        if base_url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mov', '.webm', '.svg')):
            clean_links.add(base_url)

    sorted_links = sorted(list(clean_links))
    
    with open('shopify_links.txt', 'w', encoding='utf-8') as f:
        for link in sorted_links:
            f.write(link + '\n')
    
    print(f"Extracted {len(sorted_links)} unique media links to shopify_links.txt")

if __name__ == "__main__":
    extract_links()
