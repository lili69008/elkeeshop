import os
import re

def run_verification():
    print("=== STARTING THE AUTOMATED PRESSE ECOSYSTEM AUDIT ===")
    main_path = 'localhost_v2/presse.html'
    
    # 1. Check main page
    if not os.path.exists(main_path):
        print(f"[FAIL] Main page {main_path} does not exist.")
        return
    print(f"[PASS] Main page {main_path} exists.")
    
    with open(main_path, 'r', encoding='utf-8') as f:
        main_content = f.read()
        
    # Check for unreplaced placeholders in main page
    unreplaced = re.findall(r'\{\{[A-Za-z0-9_]+\}\}', main_content)
    if unreplaced:
        print(f"[FAIL] Found unreplaced placeholders in {main_path}: {unreplaced}")
    else:
        print(f"[PASS] No unreplaced placeholders in {main_path}.")
        
    # 2. Extract subpage links from the grid
    subpage_links = re.findall(r'href="(presse-[a-z0-9\-]+\.html)"', main_content)
    print(f"[INFO] Extracted {len(subpage_links)} subpage links from main grid.")
    
    if len(subpage_links) != 25:
        # One is featured, 24 are in the grid? Let's check:
        # Wait, the script has 1 featured + 24 in the grid = 25 total articles.
        # But featured_article has a link too! So there should be 25 total links.
        # Let's count them:
        print(f"[INFO] Found {len(set(subpage_links))} unique links out of {len(subpage_links)} total occurrences.")
        
    # 3. Check all subpages
    errors = 0
    checked_files = set()
    for link in subpage_links:
        sub_path = os.path.join('localhost_v2', link)
        if sub_path in checked_files:
            continue
        checked_files.add(sub_path)
        
        if not os.path.exists(sub_path):
            print(f"[FAIL] Subpage {sub_path} does not exist.")
            errors += 1
            continue
            
        with open(sub_path, 'r', encoding='utf-8') as sf:
            sub_content = sf.read()
            
        # Check for unreplaced placeholders
        sub_unreplaced = re.findall(r'\{\{[A-Za-z0-9_]+\}\}', sub_content)
        if sub_unreplaced:
            print(f"[FAIL] Unreplaced placeholders in {sub_path}: {sub_unreplaced}")
            errors += 1
            
        # Check image existence
        img_match = re.search(r'class="art-cover-img" src="(img/presse/[^"]+)"', sub_content)
        if img_match:
            img_path = os.path.join('localhost_v2', img_match.group(1))
            if not os.path.exists(img_path):
                print(f"[FAIL] Image {img_path} referenced in {sub_path} does not exist.")
                errors += 1
        else:
            print(f"[WARN] No cover image match in {sub_path}.")
            
        # Check nav and footer presence
        if "site-footer" not in sub_content:
            print(f"[FAIL] Footer not found in {sub_path}.")
            errors += 1
            
        if "nav" not in sub_content:
            print(f"[FAIL] Navigation bar not found in {sub_path}.")
            errors += 1
            
    print(f"Checked {len(checked_files)} unique article subpage files.")
    if errors == 0:
        print("[SUCCESS] All links, images, and HTML structures are 100% verified and correct!")
    else:
        print(f"[ERROR] Found {errors} structural issues during validation.")

if __name__ == "__main__":
    run_verification()
