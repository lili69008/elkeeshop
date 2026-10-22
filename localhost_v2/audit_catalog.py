import os
import re
import json

OUTPUT_ROOT = "produits"
PLACEHOLDERS = [
    "{{PRODUCT_TITLE}}",
    "{{PRODUCT_DESC}}",
    "{{PRODUCT_COLLECTION}}",
    "{{PRODUCT_PRICE}}",
    "{{PRODUCT_METAL}}",
    "{{PRODUCT_PIERRES}}",
    "{{PRODUCT_ORIGINE}}",
    "{{PRODUCT_THUMBNAILS}}",
    "{{PRODUCT_MAIN_IMAGES}}",
    "{{PRODUCT_VARIANTS_JSON}}",
    "{{PRODUCT_IMAGE_1}}",
    "{{PRODUCT_IMAGE_2_BLOCK}}"
]

def audit():
    print("Starting Comprehensive Catalog and Visual Identity Audit...")
    total_audited = 0
    anomalies = []
    
    # Traverse output directories
    for root, dirs, files in os.walk(OUTPUT_ROOT):
        for file in files:
            if not file.endswith(".html"): continue
            
            filepath = os.path.join(root, file)
            total_audited += 1
            
            # Determine depth dynamically based on directory structure
            rel_dir = os.path.relpath(root, OUTPUT_ROOT)
            if rel_dir == '.':
                expected_base = "../"
            else:
                expected_base = "../../"
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # 1. Check for Unresolved Placeholders
            found_placeholders = []
            for p in PLACEHOLDERS:
                if p in content:
                    found_placeholders.append(p)
            
            # 2. Check for Incorrect Asset Paths
            # Search for style.css, main.js, etc.
            correct_style = f'href="{expected_base}css/style.css"'
            correct_js = f'src="{expected_base}js/main.js"'
            
            style_mismatch = False
            js_mismatch = False
            
            if 'css/style.css' in content and correct_style not in content:
                style_mismatch = True
            if 'js/main.js' in content and correct_js not in content:
                js_mismatch = True
                
            # 3. Parse and Validate Variants JSON
            json_issue = None
            variants_data = None
            json_match = re.search(r'<script id="product-variants-data" type="application/json">(.*?)</script>', content, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
                try:
                    variants_data = json.loads(json_str)
                except Exception as e:
                    json_issue = f"Invalid JSON payload: {str(e)}"
            else:
                json_issue = "Missing <script id=\"product-variants-data\"> element"
                
            if found_placeholders or style_mismatch or js_mismatch or json_issue:
                anomalies.append({
                    "file": filepath,
                    "placeholders": found_placeholders,
                    "style_mismatch": style_mismatch,
                    "js_mismatch": js_mismatch,
                    "json_issue": json_issue,
                    "variants_info": {
                        "hasColors": variants_data.get("hasColors") if variants_data else None,
                        "hasSizes": variants_data.get("hasSizes") if variants_data else None,
                        "variants_count": len(variants_data.get("variants", [])) if variants_data else 0
                    } if variants_data else None
                })

    print(f"\nAudit complete. Checked {total_audited} HTML files.")
    if anomalies:
        print(f"[WARNING] Found {len(anomalies)} files with anomalies:")
        for a in anomalies:
            print(f"- File: {a['file']}")
            if a['placeholders']:
                print(f"  Unresolved Placeholders: {a['placeholders']}")
            if a['style_mismatch']:
                print(f"  Incorrect style.css link prefix")
            if a['js_mismatch']:
                print(f"  Incorrect main.js script prefix")
            if a['json_issue']:
                print(f"  JSON State Issue: {a['json_issue']}")
            if a['variants_info']:
                v = a['variants_info']
                print(f"  Variants: colors={v['hasColors']}, sizes={v['hasSizes']}, count={v['variants_count']}")
    else:
        print("[SUCCESS] Excellent! 0 anomalies found. All files are fully compiled, resolved, and link-compliant!")

if __name__ == "__main__":
    audit()
