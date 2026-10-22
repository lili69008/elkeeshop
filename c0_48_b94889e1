import os
import re
files = {
    'haute-joaillerie-bagues.html': ('HAUTE JOAILLERIE', 'LES BAGUES D\'EXCEPTION'),
    'haute-joaillerie-colliers.html': ('HAUTE JOAILLERIE', 'LES COLLIERS D\'EXCEPTION'),
    'haute-joaillerie-boucles-doreilles.html': ('HAUTE JOAILLERIE', 'LES BOUCLES D\'OREILLES D\'EXCEPTION'),
    'haute-joaillerie-bracelets.html': ('HAUTE JOAILLERIE', 'LES BRACELETS D\'EXCEPTION'),
    'unbreakable-gold.html': ('UNBREAKABLE', 'GOLD COLLECTION'),
    'unbreakable-silver.html': ('UNBREAKABLE', 'SILVER COLLECTION'),
    'unbreakable-diamond.html': ('UNBREAKABLE', 'DIAMOND COLLECTION')
}
for f, (kicker, title) in files.items():
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    # Handle different possible kickers in templates
    content = re.sub(r'<span class="kicker">.*?</span>', f'<span class="kicker">{kicker}</span>', content, count=1)
    # Handle different possible titles in templates
    content = re.sub(r'<h1.*?>.*?</h1>', f'<h1 style="font-size: 3.5rem; letter-spacing: 0.2em;">{title}</h1>', content, count=1)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
