import os
import re
from bs4 import BeautifulSoup
import json
import urllib.parse

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/scratch/live_subpages"
    files = [f for f in os.listdir(folder) if f.endswith('.html')]
    
    pages_data = {}
    
    for f in files:
        slug = f.replace('.html', '')
        path = os.path.join(folder, f)
        
        with open(path, 'r', encoding='utf-8') as file_obj:
            html = file_obj.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Decompose header, footer, nav
        for tag in ['nav', 'footer', 'header']:
            for el in soup.find_all(tag):
                el.decompose()
                
        # Find all content headings and paragraphs
        content_paragraphs = []
        for p in soup.find_all('p'):
            txt = p.get_text().strip()
            if txt and len(txt) > 20 and "rejoignez notre cercle" not in txt.lower():
                content_paragraphs.append(' '.join(txt.split()))
                
        # Find all headings
        content_headings = []
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            txt = h.get_text().strip()
            if txt and len(txt) > 3 and "newsletter" not in txt.lower() and "cercle" not in txt.lower():
                content_headings.append(' '.join(txt.split()))
                
        # Find all images on the page
        img_urls = []
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-srcset')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif not src.startswith('http'):
                    src = urllib.parse.urljoin('https://elkeberr.com', src)
                
                src_lower = src.lower()
                if any(x in src_lower for x in ['logo', 'flag', 'icon', 'arrow', 'social', 'widget', 'loader', 'payment']):
                    continue
                if src not in img_urls:
                    img_urls.append(src)
                    
        pages_data[slug] = {
            "slug": slug,
            "headings": content_headings[:15],
            "paragraphs": content_paragraphs[:20],
            "images": img_urls[:20]
        }
            
    with open("c:/Users/lyies/Desktop/siteelk/scratch/parsed_subpages_data.json", "w", encoding="utf-8") as out:
        json.dump(pages_data, out, indent=4, ensure_ascii=False)
        
    print("Done. Saved all subpages content to scratch/parsed_subpages_data.json")

if __name__ == "__main__":
    main()
