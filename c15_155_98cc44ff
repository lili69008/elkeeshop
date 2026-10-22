from bs4 import BeautifulSoup

def main():
    path = "c:/Users/lyies/Desktop/siteelk/scratch/live_subpages/unbreakable-launch.html"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Decompose head, nav, footer, script, style
    for t in ['head', 'nav', 'footer', 'script', 'style', 'header']:
        for el in soup.find_all(t):
            el.decompose()
            
    # Print all text content blocks that are not empty and are relatively long
    print("--- TEXT BLOCK ANALYSIS ---")
    for el in soup.find_all(True):
        if el.name in ['div', 'p', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']:
            # check direct text
            text = el.get_text(strip=True)
            if len(text) > 40:
                # check if there are no nested block elements to keep it leaf
                children = [c for c in el.find_all(True) if c.name in ['div', 'p', 'span']]
                if len(children) < 2:
                    print(f"[{el.name} class={el.get('class')}]: {' '.join(text.split())[:300]}")

if __name__ == "__main__":
    main()
