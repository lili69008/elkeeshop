import os
import re

FOOTER_BLOCK = """<footer>
        <div class="footer-logo">ELKE BERR GENÈVE</div>
        <div class="footer-links">
            <a href="mentions-legales.html">Mentions Légales</a>
            <a href="confidentialite.html">Confidentialité</a>
            <a href="cgv.html">CGV</a>
            <a href="livraison-retours.html">Livraison & Retours</a>
        </div>
        <p style="font-size: 0.6rem; color: var(--muted);">&copy; 2026 Elke Berr Creations. Tous droits réservés.</p>
    </footer>"""

DIR = "c:/Users/lyies/Desktop/siteelk/localhost_v2"

def update_all_footers():
    for f in os.listdir(DIR):
        if f.endswith(".html"):
            path = os.path.join(DIR, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace the entire <footer> block
            new_content = re.sub(r'<footer>.*?</footer>', FOOTER_BLOCK, content, flags=re.DOTALL)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated footer in {f}")

if __name__ == "__main__":
    update_all_footers()
