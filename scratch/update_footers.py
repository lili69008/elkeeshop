import os

FOOTER_BLOCK = """<div class="footer-links">
            <a href="mentions-legales.html">Mentions Légales</a>
            <a href="confidentialite.html">Confidentialité</a>
            <a href="cgv.html">CGV</a>
            <a href="livraison-retours.html">Livraison & Retours</a>
        </div>"""

OLD_FOOTER_START = '<div class="footer-links">'
OLD_FOOTER_END = '</div>'

DIR = "c:/Users/lyies/Desktop/siteelk/localhost_v2"

def update_footers():
    for f in os.listdir(DIR):
        if f.endswith(".html"):
            path = os.path.join(DIR, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if OLD_FOOTER_START in content:
                start = content.find(OLD_FOOTER_START)
                end = content.find(OLD_FOOTER_END, start) + len(OLD_FOOTER_END)
                new_content = content[:start] + FOOTER_BLOCK + content[end:]
                
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated footer in {f}")

if __name__ == "__main__":
    update_footers()
