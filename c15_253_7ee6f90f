import os

products = [
    {"handle": "epure-necklace", "title": "ÉPURE NECKLACE", "category": "Colliers & Pendentifs"},
    {"handle": "linfini-necklace", "title": "L'INFINI NECKLACE", "category": "Colliers & Pendentifs"},
    {"handle": "alma-ring", "title": "ALMA RING", "category": "Bagues"},
    {"handle": "tresor-ring", "title": "TRÉSOR RING", "category": "Bagues"},
    {"handle": "eclat-earrings", "title": "ÉCLAT EARRINGS", "category": "Boucles d'oreilles"},
    {"handle": "bond-earrings", "title": "BOND EARRINGS", "category": "Boucles d'oreilles"},
    {"handle": "link-earrings", "title": "LINK EARRINGS", "category": "Boucles d'oreilles"},
    {"handle": "complice-bangle", "title": "COMPLICE BANGLE", "category": "Bracelets"},
    {"handle": "echo-bangle", "title": "ECHO BANGLE", "category": "Bracelets"},
    {"handle": "essentiel-bangle", "title": "ESSENTIEL BANGLE", "category": "Bracelets"}
]

print("Verifying files and images:")
for p in products:
    html_path = os.path.join("localhost_v2/produits", f"{p['handle']}.html")
    img_path = os.path.join("localhost_v2/img", f"zp_unbreakable_{p['handle'].replace('-', '_')}.png")
    
    html_exists = os.path.exists(html_path)
    img_exists = os.path.exists(img_path)
    
    print(f"Product: {p['title']}")
    print(f"  HTML: {'OK' if html_exists else 'MISSING'} ({html_path})")
    print(f"  IMG:  {'OK' if img_exists else 'MISSING'} ({img_path})")
    
    if html_exists:
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Find the spec-list metal, stones
            if "Métal" in content:
                print("  Metal element exists in HTML")
            if "Rhodium" in content:
                print("  WARNING: Rhodium metal found in HTML!")
