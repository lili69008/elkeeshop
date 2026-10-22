from bs4 import BeautifulSoup
import re

def main():
    path = "c:/Users/lyies/Desktop/siteelk/scratch/live_events.html"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove nav and footer to avoid noisy search
    for nav in soup.find_all('nav'):
        nav.decompose()
    for footer in soup.find_all('footer'):
        footer.decompose()
    for header in soup.find_all('header'):
        header.decompose()
        
    # Let's search for links that contain our event slugs
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
    
    for slug in event_slugs:
        links = soup.find_all('a', href=lambda h: h and slug in h)
        print(f"\nSlug: {slug} - Found {len(links)} links in body")
        for idx, l in enumerate(links):
            # Traverse ancestors to find a div containing an image or backgrounds
            curr = l
            found_img = False
            for i in range(12):
                # Check for images or background style
                imgs = curr.find_all('img')
                style = curr.get('style') or ''
                bg_match = re.search(r'url\((.*?)\)', style)
                
                img_srcs = []
                if imgs:
                    for im in imgs:
                        src = im.get('src') or im.get('data-src') or im.get('data-srcset')
                        if src and 'cdn.shopify.com' in src and 'flags' not in src:
                            img_srcs.append(src)
                            
                bg_src = bg_match.group(1) if bg_match else None
                
                print(f"  Level {i}: tag={curr.name}, class={curr.get('class')}, imgs={img_srcs}, bg={bg_src}")
                curr = curr.parent
                if not curr:
                    break

if __name__ == "__main__":
    main()
