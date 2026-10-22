import urllib.request
import os
import time

def main():
    slugs = [
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
    
    output_dir = "c:/Users/lyies/Desktop/siteelk/scratch/live_subpages"
    os.makedirs(output_dir, exist_ok=True)
    
    for slug in slugs:
        url = f"https://elkeberr.com/fr/pages/{slug}"
        filepath = os.path.join(output_dir, f"{slug}.html")
        print(f"Fetching detail page: {url} -> {filepath}")
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print("  -> Success")
        except Exception as e:
            print(f"  -> Error: {e}")
            
        time.sleep(0.2)

if __name__ == "__main__":
    main()
