import urllib.request
import re
import os

def main():
    url = "https://elkeberr.com/fr/pages/events"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        print(f"Fetching {url}...")
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        print(f"Successfully fetched {len(html)} bytes.")
        
        # Write html to a scratch file to inspect if needed
        os.makedirs("c:/Users/lyies/Desktop/siteelk/scratch", exist_ok=True)
        with open("c:/Users/lyies/Desktop/siteelk/scratch/live_events.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Wrote live_events.html to scratch/")
        
        # Let's search for image urls (e.g. cdn.shopify.com) or custom tags
        img_tags = re.findall(r'<img[^>]+src="([^"]+)"', html)
        print(f"Found {len(img_tags)} image tags in HTML.")
        
        # Let's also look for event page links (fr/pages/...)
        page_links = re.findall(r'href="(/fr/pages/[^"]+)"', html)
        print(f"Found {len(page_links)} event page links in HTML:")
        for link in set(page_links):
            print(f"  - {link}")
            
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
