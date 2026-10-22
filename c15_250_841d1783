import os
import re

# Precise and complete NAV block with JS fallback
NAV_BLOCK = """<nav class="nav-bar">
        <div class="logo-container">
            <span class="logo-main">ELKE BERR</span>
            <span class="logo-sub">GENÈVE</span>
        </div>
        <div class="nav-links">
            <a href="index.html">Accueil</a>
            <a href="maison.html">La Maison</a>
            <div class="dropdown" onmouseover="this.querySelector('.dropdown-content').style.display='block'" onmouseout="this.querySelector('.dropdown-content').style.display='none'">
                <a href="unbreakable.html">Unbreakable</a>
                <div class="dropdown-content" style="display:none; position:absolute; background:#FDFCF8; min-width:320px; border:1px solid #E8E4DA; box-shadow:0 20px 50px rgba(0,0,0,0.1); z-index:9999; top:100%; left:0; padding:1.5rem 0;">
                    <a href="unbreakable.html" style="color:#1F1E1D; padding:0.8rem 2.5rem; display:block; text-decoration:none; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;">Unbreakable The Story</a>
                    <a href="unbreakable-paul.html" style="color:#1F1E1D; padding:0.8rem 2.5rem; display:block; text-decoration:none; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;">Elke Berr X Paul Pogba Collection</a>
                    <a href="unbreakable-zulay.html" style="color:#1F1E1D; padding:0.8rem 2.5rem; display:block; text-decoration:none; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;">Elke Berr X Zulay Pogba Collection</a>
                    <a href="unbreakable-villa.html" style="color:#1F1E1D; padding:0.8rem 2.5rem; display:block; text-decoration:none; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;">Lancement à la Villa Forbes</a>
                </div>
            </div>
            <a href="private-jeweller.html">Joaillier Privé</a>
            <a href="bagues.html">Bagues</a>
            <a href="colliers.html">Colliers</a>
            <a href="joaillerie.html">Haute Joaillerie</a>
            <a href="bespoke.html">Bespoke</a>
            <a href="news.html">News</a>
            <a href="contact.html">Contact</a>
        </div>
    </nav>"""

DIR = "c:/Users/lyies/Desktop/siteelk/localhost_v2"

def total_nav_rebuild():
    for f in os.listdir(DIR):
        if f.endswith(".html"):
            path = os.path.join(DIR, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace ANY <nav> or corrupted blocks with the clean JS-enabled one
            new_content = re.sub(r'<nav.*?</nav>', NAV_BLOCK, content, flags=re.DOTALL)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Rebuilt Nav with JS fallback in {f}")

if __name__ == "__main__":
    total_nav_rebuild()
