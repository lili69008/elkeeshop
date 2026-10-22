from bs4 import BeautifulSoup
import re
import json

def main():
    path = "c:/Users/lyies/Desktop/siteelk/scratch/live_events.html"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's search for links that point to the 12 events
    event_slugs = [
        "unbreakable-launch",
        "cannes-film-festival",
        "paris-blockchain-week-2025",
        "opera-for-peace-2025",
        "most-influential-women-of-the-world",
        "chateau-de-creema-2023",
        "gem-geneve-2023",
        "monaco-film-2022",
        "better-world-fund-2022",
        "cannes-festival-2021",
        "cannes-festival-2019",
        "vacheron-constantin-workshop-2016"
    ]
    
    events_data = {}
    
    # Let's inspect links
    links = soup.find_all('a', href=True)
    print(f"Total links: {len(links)}")
    
    for slug in event_slugs:
        # Find all link elements that contain this slug in href
        matching_links = [l for l in links if slug in l['href']]
        if not matching_links:
            print(f"No link found for slug: {slug}")
            continue
            
        print(f"\nSlug: {slug} - Found {len(matching_links)} matches")
        
        # For each match, let's traverse up to find a common parent/container that has an image and text
        for idx, link in enumerate(matching_links):
            # Check parents
            parent = link.parent
            depth = 0
            img_src = None
            title_text = ""
            desc_text = ""
            
            while parent and depth < 8:
                # Search for img and text inside this parent
                imgs = parent.find_all('img')
                texts = parent.get_text(separator=' ').strip()
                
                if imgs and not img_src:
                    # Prefer standard content image, ignore small icons/flags
                    for im in imgs:
                        src = im.get('src') or im.get('data-src') or im.get('data-srcset')
                        if src and 'cdn.shopify.com' in src and 'flags' not in src:
                            img_src = src
                            break
                            
                # Let's see if we can find clean header texts
                headers = [parent.find(h) for h in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'] if parent.find(h)]
                if headers and not title_text:
                    title_text = headers[0].get_text().strip()
                    
                parent = parent.parent
                depth += 1
                
            print(f"  Match {idx+1}:")
            print(f"    Title: {title_text}")
            print(f"    Image: {img_src}")
            print(f"    Clean Text preview: {texts[:200] if texts else ''}")
            
            if slug not in events_data and img_src:
                events_data[slug] = {
                    "slug": slug,
                    "title": title_text,
                    "image": img_src,
                    "preview": texts
                }
                
    # Save extracted info
    with open("c:/Users/lyies/Desktop/siteelk/scratch/extracted_events_data.json", "w", encoding="utf-8") as out:
        json.dump(events_data, out, indent=4, ensure_ascii=False)
    print("\nSaved extracted data to scratch/extracted_events_data.json")

if __name__ == "__main__":
    main()
