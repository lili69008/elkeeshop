import re
import os

def extract_from_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return set()
    print(f"Reading {filename}...")
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # regex to find shopify files
    regex = r'https://cdn\.shopify\.com/[^\s\"\'\>]+'
    all_links = re.findall(regex, content)
    
    clean_links = set()
    for link in all_links:
        base_url = link.split('?')[0].split('&')[0]
        base_url = base_url.replace('&amp;', '&').replace('"', '').replace("'", "").replace(">", "").replace("<", "")
        # Try to clean trailing characters
        base_url = re.sub(r'[\)\,\.\;\:\*\#]+$', '', base_url)
        if base_url.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mov', '.webm', '.svg')):
            clean_links.add(base_url)
    return clean_links

def main():
    links1 = extract_from_file("Elke Berr · Files · Shopify.html")
    links2 = extract_from_file("Elke Berr · Files · Shopify 2.html")
    all_links = links1.union(links2)
    print(f"File 1 links: {len(links1)}")
    print(f"File 2 links: {len(links2)}")
    print(f"Total unique links: {len(all_links)}")
    
    # Search for keywords
    keywords = ["evenement", "event", "cannes", "nice", "cremat", "gem", "monaco", "award", "women", "gala", "presse", "bel", "party", "showcase", "expos"]
    matches = []
    for link in sorted(list(all_links)):
        filename = os.path.basename(link)
        matched_kws = [kw for kw in keywords if kw in filename.lower()]
        if matched_kws:
            matches.append((link, matched_kws))
            
    print(f"Matches ({len(matches)}):")
    for link, kws in matches:
        print(f"  - {link} (KWs: {kws})")

if __name__ == "__main__":
    main()
