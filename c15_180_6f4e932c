from bs4 import BeautifulSoup
import urllib.parse
import json

def main():
    path = "c:/Users/lyies/Desktop/siteelk/scratch/live_events.html"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Decompose nav/footer/header to clean up
    for t in ['nav', 'footer', 'header']:
        for el in soup.find_all(t):
            el.decompose()
            
    items = soup.find_all(class_='featured-grid--item')
    print(f"Found {len(items)} featured-grid--item elements.")
    
    extracted_events = []
    
    for idx, item in enumerate(items):
        print(f"\nAnalyzing Item {idx+1}:")
        
        # 1. Find link
        link_el = item.find('a', href=True)
        link = link_el['href'] if link_el else None
        
        # 2. Find image
        img_el = item.find('img')
        img_url = None
        if img_el:
            img_url = img_el.get('src') or img_el.get('data-src') or img_el.get('data-srcset')
            if img_url:
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif not img_url.startswith('http'):
                    img_url = urllib.parse.urljoin('https://elkeberr.com', img_url)
                    
        # 3. Find title
        # Usually inside some header or class like 'stacked-text--title'
        title_el = item.find(class_=lambda c: c and 'title' in c.lower())
        if not title_el:
            # Check h1-h6
            for h in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                title_el = item.find(h)
                if title_el:
                    break
        title = title_el.get_text().strip() if title_el else ""
        
        # 4. Find description/text content
        # Usually inside 'stacked-text--description' or text class
        desc_el = item.find(class_=lambda c: c and 'description' in c.lower())
        if not desc_el:
            # Fallback to paragraph
            desc_el = item.find('p')
        desc = desc_el.get_text().strip() if desc_el else ""
        
        # Let's clean up title & desc formatting (replace newlines)
        title = ' '.join(title.split())
        desc = ' '.join(desc.split())
        
        print(f"  Title: {title}")
        print(f"  Link: {link}")
        print(f"  Image: {img_url}")
        print(f"  Desc: {desc[:100]}...")
        
        extracted_events.append({
            "index": idx + 1,
            "title": title,
            "link": link,
            "image_url": img_url,
            "description": desc
        })
        
    with open("c:/Users/lyies/Desktop/siteelk/scratch/parsed_events.json", "w", encoding="utf-8") as out:
        json.dump(extracted_events, out, indent=4, ensure_ascii=False)
        
    print(f"\nSaved {len(extracted_events)} events to scratch/parsed_events.json")

if __name__ == "__main__":
    main()
