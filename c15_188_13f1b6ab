from bs4 import BeautifulSoup

def main():
    path = "c:/Users/lyies/Desktop/siteelk/scratch/live_events.html"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove nav, footer, header
    for tag in ['nav', 'footer', 'header']:
        for el in soup.find_all(tag):
            el.decompose()
            
    # Find link with 'unbreakable-launch'
    link = soup.find('a', href=lambda h: h and 'unbreakable-launch' in h)
    if not link:
        print("Link not found")
        return
        
    # Go up to the featured-grid--item div
    parent = link
    while parent and 'featured-grid--item' not in parent.get('class', []):
        parent = parent.parent
        
    if parent:
        print("Found featured-grid--item:")
        print(parent.prettify()[:2000])
    else:
        print("featured-grid--item parent not found")

if __name__ == "__main__":
    main()
