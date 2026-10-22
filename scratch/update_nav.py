import os

NAV_BLOCK = """<div class="nav-links">
            <a href="index.html">Accueil</a>
            <a href="maison.html">La Maison</a>
            <a href="bagues.html">Bagues</a>
            <a href="colliers.html">Colliers</a>
            <a href="joaillerie.html">Haute Joaillerie</a>
            <a href="bespoke.html">Bespoke</a>
            <a href="news.html">News</a>
            <a href="contact.html">Contact</a>
        </div>"""

OLD_NAV_START = '<div class="nav-links">'
OLD_NAV_END = '</div>'

DIR = "c:/Users/lyies/Desktop/siteelk/localhost_v2"

def update_nav():
    for f in os.listdir(DIR):
        if f.endswith(".html"):
            path = os.path.join(DIR, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Simple replacement logic
            if OLD_NAV_START in content:
                start = content.find(OLD_NAV_START)
                end = content.find(OLD_NAV_END, start) + len(OLD_NAV_END)
                new_content = content[:start] + NAV_BLOCK + content[end:]
                
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Updated nav in {f}")

if __name__ == "__main__":
    update_nav()
