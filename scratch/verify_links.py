import os
from bs4 import BeautifulSoup

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/localhost_v2"
    files_to_check = [
        "evenements.html",
        "unbreakable-launch.html",
        "cannes-film-festival.html",
        "paris-blockchain-week-2025.html",
        "opera-for-peace-2025.html",
        "most-influential-women-of-the-world.html",
        "chateau-de-creema-2023.html",
        "gem-geneve-2023.html",
        "monaco-film-2022.html",
        "better-world-fund-2022.html",
        "cannes-festival-2021.html",
        "cannes-festival-2019.html",
        "vacheron-constantin-workshop-2016.html"
    ]
    
    errors = 0
    checked_links = 0
    
    print("--- AUTOMATED LINK VERIFICATION ---")
    for filename in files_to_check:
        filepath = os.path.join(folder, filename)
        if not os.path.exists(filepath):
            print(f"[ERROR] File does not exist: {filename}")
            errors += 1
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        print(f"Checking {filename}...")
        
        # Check all internal links
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href', '')
            if not href:
                continue
                
            checked_links += 1
            
            # Check for live site references
            if "elkeberr.com" in href:
                # Allow official social links
                if "instagram.com" in href or "linkedin.com" in href or "x.com" in href:
                    continue
                print(f"  [ERROR] Live site reference found in link: {href}")
                errors += 1
                
            # Check for local file existence (for non-external links)
            elif not href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                # Split anchor
                local_file = href.split('#')[0]
                if not local_file:
                    continue
                    
                local_filepath = os.path.join(folder, local_file)
                if not os.path.exists(local_filepath):
                    print(f"  [ERROR] Broken local link: {href} (file '{local_file}' not found)")
                    errors += 1
                    
        # Check all img sources
        for img_tag in soup.find_all('img'):
            src = img_tag.get('src', '')
            if not src:
                continue
                
            checked_links += 1
            
            if "elkeberr.com" in src:
                print(f"  [ERROR] Live site image source found: {src}")
                errors += 1
            elif not src.startswith(('http://', 'https://', 'data:')):
                img_filepath = os.path.join(folder, src)
                if not os.path.exists(img_filepath):
                    print(f"  [ERROR] Broken local image source: {src} (file not found)")
                    errors += 1
                    
    print(f"\nScan completed. Checked {checked_links} assets/links. Total errors: {errors}")
    if errors > 0:
        exit(1)

if __name__ == "__main__":
    main()
