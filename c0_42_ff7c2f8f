import os

BASE_DIR = r"c:\Users\lyies\Desktop\siteelk\localhost_v2"
TEMPLATE_FILE = os.path.join(BASE_DIR, "unbreakable.html")

MISSING_PAGES = [
    "unbreakable-story.html",
    "unbreakable-villa.html",
    "haute-joaillerie.html",
    "haute-joaillerie-colliers.html",
    "haute-joaillerie-bagues.html",
    "haute-joaillerie-boucles-doreilles.html",
    "haute-joaillerie-bracelets.html",
    "bijoux.html",
    "bagues.html",
    "colliers.html",
    "boucles-doreilles.html",
    "bracelets.html",
    "collections-eb.html",
    "rockn-rose-summer.html",
    "dolce.html",
    "me-you.html",
    "milky-way.html",
    "gift-idea-1.html",
    "news.html",
    "presse.html",
    "evenements.html",
    "maison.html",
    "maison-histoire.html",
    "maison-savoir-faire.html"
]

def create_pages():
    if not os.path.exists(TEMPLATE_FILE):
        print("Template file not found.")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    created_count = 0
    for page in MISSING_PAGES:
        target_path = os.path.join(BASE_DIR, page)
        if not os.path.exists(target_path):
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(template_content)
            print(f"Created: {page}")
            created_count += 1
        else:
            # Still update with nav if needed, but update_horizontal_v2.py handles that.
            print(f"Skipped (already exists): {page}")
    
    print(f"DONE: {created_count} pages created.")

if __name__ == "__main__":
    create_pages()
