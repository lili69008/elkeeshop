import os
import re
from urllib.parse import urljoin, urlparse

BASE_DIR = r"c:\Users\lyies\Desktop\siteelk\localhost_v2"

def get_all_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def check_links():
    html_files = get_all_html_files(BASE_DIR)
    all_pages = [os.path.relpath(f, BASE_DIR).replace("\\", "/") for f in html_files]
    
    broken_links = []
    
    # Regex for href and src
    link_pattern = re.compile(r'(?:href|src)=["\'](.*?)["\']')
    
    for file_path in html_files:
        rel_file_path = os.path.relpath(file_path, BASE_DIR).replace("\\", "/")
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            for link in links:
                # Skip external links, anchors, and data URIs
                if link.startswith(("http", "mailto:", "tel:", "#", "data:")):
                    continue
                
                # Normalize link
                # If it starts with ../, we need to resolve it
                resolved_link = urljoin(rel_file_path, link)
                # Remove query params or fragments
                resolved_link = urlparse(resolved_link).path
                
                # Check if it exists
                target_full_path = os.path.normpath(os.path.join(BASE_DIR, resolved_link))
                
                if not os.path.exists(target_full_path):
                    broken_links.append({
                        "file": rel_file_path,
                        "link": link,
                        "resolved": resolved_link
                    })
    
    return broken_links

if __name__ == "__main__":
    print("Starting Link Audit...")
    broken = check_links()
    if not broken:
        print("No broken links found!")
    else:
        print(f"Found {len(broken)} broken links:")
        # Group by file for readability
        grouped = {}
        for b in broken:
            f = b["file"]
            if f not in grouped: grouped[f] = []
            grouped[f].append(b["link"])
            
        for f, links in grouped.items():
            print(f"File: {f}")
            for l in set(links):
                print(f"  - {l}")
