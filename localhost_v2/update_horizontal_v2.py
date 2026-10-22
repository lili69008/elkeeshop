import os
import re

# DIR TO PROCESS
BASE_DIR = r"c:\Users\lyies\Desktop\siteelk\localhost_v2"

def get_relative_nav(depth):
    prefix = "../" * depth
    return f"""    <nav class="nav-bar">
        <a href="{prefix}index.html" class="logo-container">
            <span class="logo-main">ELKE BERR</span>
            <span class="logo-sub">GENÈVE</span>
        </a>
        <ul class="nav-links">
            <li><a href="{prefix}index.html">Accueil</a></li>
            <li>
                <a href="{prefix}unbreakable.html">Unbreakable</a>
                <div class="dropdown-menu">
                    <a href="{prefix}unbreakable.html">Unbreakable</a>
                    <a href="{prefix}unbreakable-paul.html">Elke Berr X Paul Pogba Collection</a>
                    <a href="{prefix}unbreakable-zulay.html">Elke Berr X Zulay Pogba Collection</a>
                    <a href="{prefix}unbreakable-story.html">Unbreakable The Story</a>
                    <a href="{prefix}unbreakable-villa.html">Lancement Unbreakable à la Villa Forbes</a>
                </div>
            </li>
            <li><a href="{prefix}private-jeweller.html">Joaillerie Privée</a></li>
            <li class="has-mega">
                <a href="{prefix}haute-joaillerie.html">Haute Joaillerie</a>
                <div class="mega-menu">
                    <div class="mega-column">
                        <h4>Catégories</h4>
                        <ul>
                            <li><a href="{prefix}haute-joaillerie.html">Haute Joaillerie</a></li>
                            <li><a href="{prefix}haute-joaillerie-colliers.html">Colliers</a></li>
                            <li><a href="{prefix}haute-joaillerie-bagues.html">Bagues</a></li>
                            <li><a href="{prefix}haute-joaillerie-boucles-doreilles.html">Boucles d'oreilles</a></li>
                            <li><a href="{prefix}haute-joaillerie-bracelets.html">Bracelets</a></li>
                        </ul>
                    </div>
                </div>
            </li>
            <li class="has-mega">
                <a href="{prefix}bijoux.html">Bijoux</a>
                <div class="mega-menu">
                    <div class="mega-column">
                        <h4>Catégorie</h4>
                        <ul>
                            <li><a href="{prefix}bijoux.html">Bijoux</a></li>
                            <li><a href="{prefix}bagues.html">Bagues</a></li>
                            <li><a href="{prefix}colliers.html">Colliers</a></li>
                            <li><a href="{prefix}boucles-doreilles.html">Boucles d'oreilles</a></li>
                            <li><a href="{prefix}bracelets.html">Bracelets</a></li>
                        </ul>
                    </div>
                    <div class="mega-column">
                        <h4>Collection</h4>
                        <ul>
                            <li><a href="{prefix}collections-eb.html">Collection</a></li>
                            <li><a href="{prefix}rockn-rose.html">Rock'N Rose</a></li>
                            <li><a href="{prefix}rockn-rose-summer.html">Édition d'été de Rock'N Rose</a></li>
                            <li><a href="{prefix}singular.html">Singular</a></li>
                            <li><a href="{prefix}mysteria.html">Mysteria</a></li>
                            <li><a href="{prefix}waves.html">Waves</a></li>
                            <li><a href="{prefix}dolce.html">Dolce</a></li>
                            <li><a href="{prefix}me-you.html">Me & You</a></li>
                            <li><a href="{prefix}milky-way.html">Milky Way</a></li>
                        </ul>
                    </div>
                    <div class="mega-column">
                        <h4>Idées cadeaux</h4>
                        <ul>
                            <li><a href="{prefix}gift-idea-1.html">Idées cadeaux</a></li>
                            <li><a href="{prefix}pour-elle.html">Pour elle</a></li>
                            <li><a href="{prefix}pour-lui.html">Pour lui</a></li>
                        </ul>
                    </div>
                </div>
            </li>
            <li>
                <a href="{prefix}news.html">Nouvelles</a>
                <div class="dropdown-menu">
                    <a href="{prefix}news.html">Nouvelles</a>
                    <a href="{prefix}presse.html">Presse</a>
                    <a href="{prefix}evenements.html">Événements</a>
                </div>
            </li>
            <li>
                <a href="{prefix}maison.html">Maison EB</a>
                <div class="dropdown-menu">
                    <a href="{prefix}maison.html">Maison EB</a>
                    <a href="{prefix}maison-histoire.html">Histoire</a>
                    <a href="{prefix}maison-savoir-faire.html">Savoir-faire</a>
                    <a href="{prefix}private-jeweller.html">Joaillerie privée</a>
                </div>
            </li>
            <li><a href="{prefix}contact.html">Contact</a></li>
        </ul>
    </nav>
    <script src="{prefix}js/main.js"></script>"""

def update_page(file_path):
    # Calculate depth relative to BASE_DIR
    rel_path = os.path.relpath(os.path.dirname(file_path), BASE_DIR)
    depth = 0 if rel_path == '.' else len(rel_path.split(os.sep))
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove ANY existing nav-bar and its following scripts
    # We use a broad pattern to catch multiple consecutive script tags
    nav_pattern = re.compile(r'<nav class="nav-bar">.*?</nav>(\s*<script src=".*?js/main\.js"></script>)*', re.DOTALL)
    
    # Also catch some variants of scripts that might be at the end of body
    reveal_script_pattern = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?reveal.*?<\/script>', re.DOTALL)
    
    new_content = nav_pattern.sub(get_relative_nav(depth), content)
    new_content = reveal_script_pattern.sub('', new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# RUN ON ALL HTML FILES
count = 0
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith('.html'):
            if update_page(os.path.join(root, file)):
                count += 1

print(f"DONE: {count} pages updated with Centralized Nav and JS.")
