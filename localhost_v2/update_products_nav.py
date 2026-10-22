import os
import re

DIR = r"c:\Users\lyies\Desktop\siteelk\localhost_v2\produits"

# REFINED HORIZONTAL NAV HTML FOR SUBDIRECTORIES (using ../)
HORIZONTAL_NAV = """    <nav class="nav-bar">
        <a href="../index.html" class="logo-container">
            <span class="logo-main">ELKE BERR</span>
            <span class="logo-sub">GENÈVE</span>
        </a>
        <ul class="nav-links">
            <li><a href="../index.html">Accueil</a></li>
            <li><a href="../maison.html">La Maison</a></li>
            <li>
                <a href="../unbreakable.html">Unbreakable</a>
                <div class="dropdown-menu">
                    <a href="../unbreakable.html">The Story</a>
                    <a href="../unbreakable-paul.html">Elke Berr X Paul Pogba</a>
                    <a href="../unbreakable-zulay.html">Elke Berr X Zulay Pogba</a>
                </div>
            </li>
            <li class="has-mega">
                <a href="../bagues.html">Bijoux</a>
                <div class="mega-menu">
                    <div class="mega-column">
                        <h4>Catégories</h4>
                        <ul>
                            <li><a href="../bagues.html">Bagues</a></li>
                            <li><a href="../colliers.html">Colliers</a></li>
                            <li><a href="../bracelets.html">Bracelets</a></li>
                            <li><a href="../boucles-doreilles.html">Boucles d'oreilles</a></li>
                            <li><a href="../pendentifs.html">Pendentifs</a></li>
                        </ul>
                    </div>
                    <div class="mega-column">
                        <h4>Collections</h4>
                        <ul>
                            <li><a href="#">Rock'N Rose</a></li>
                            <li><a href="#">Singular</a></li>
                            <li><a href="#">Mysteria</a></li>
                            <li><a href="#">Waves</a></li>
                        </ul>
                    </div>
                    <div class="mega-column">
                        <h4>Idées Cadeaux</h4>
                        <ul>
                            <li><a href="#">Pour Elle</a></li>
                            <li><a href="#">Pour Lui</a></li>
                            <li><a href="#">Sélections</a></li>
                        </ul>
                    </div>
                </div>
            </li>
            <li><a href="../joaillerie.html">Haute Joaillerie</a></li>
            <li><a href="../bespoke.html">Bespoke</a></li>
            <li>
                <a href="../news.html">News</a>
                <div class="dropdown-menu">
                    <a href="../presse.html">Presse</a>
                    <a href="../evenements.html">Événements</a>
                </div>
            </li>
            <li><a href="../contact.html">Contact</a></li>
        </ul>
    </nav>"""

def update_nav(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search for the existing nav block
    nav_pattern = r'<nav class="nav-bar">.*?</nav>'
    
    if re.search(nav_pattern, content, re.DOTALL):
        # Replace the entire nav block
        new_content = re.sub(nav_pattern, HORIZONTAL_NAV, content, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(f"No nav block found in: {os.path.basename(file_path)}")

if os.path.exists(DIR):
    html_files = [f for f in os.listdir(DIR) if f.endswith('.html')]
    for file in html_files:
        update_nav(os.path.join(DIR, file))
    print(f"Successfully updated navigation for {len(html_files)} product pages.")
else:
    print("Directory 'produits' does not exist.")
