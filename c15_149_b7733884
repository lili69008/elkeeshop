from bs4 import BeautifulSoup

def main():
    path = "c:/Users/lyies/Desktop/siteelk/scratch/live_events.html"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's find the link for 'unbreakable-launch'
    link = soup.find('a', href=lambda h: h and 'unbreakable-launch' in h)
    if not link:
        print("Link not found")
        return
        
    # Let's print the ancestors and siblings
    curr = link
    for i in range(5):
        print(f"\n--- Ancestor Level {i}: tag={curr.name}, class={curr.get('class')}, id={curr.get('id')} ---")
        print(str(curr)[:1000])
        curr = curr.parent
        if not curr:
            break

if __name__ == "__main__":
    main()
