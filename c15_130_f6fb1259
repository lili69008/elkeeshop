import os
import json
import re
from bs4 import BeautifulSoup

def clean_captions(headings, title):
    # Filter out common layout text, buttons, and titles to leave only real captions
    ignored = [
        "votre panier",
        "🇺🇸 attention for us customers",
        "attention for us customers",
        "please note",
        "boucles d'oreilles unbreakable",
        "lancement unbreakable",
        "à la villa forbes, cannes",
        "l'événement",
        "une nuit d'exception",
        "retour aux événements",
        "continuer mes achats",
        title.lower()
    ]
    cleaned = []
    for h in headings:
        h_clean = h.strip()
        h_lower = h_clean.lower()
        if not h_clean:
            continue
        if any(ig in h_lower for ig in ignored):
            continue
        if h_clean not in cleaned:
            cleaned.append(h_clean)
    return cleaned

def get_kicker_and_location(slug, title):
    # Custom mapping of high-end kicker/locations based on events
    mapping = {
        "unbreakable-launch": ("CANNES", "VILLA FORBES, CANNES"),
        "cannes-film-festival": ("CANNES 2025", "FESTIVAL DE CANNES — TAPIS ROUGE"),
        "paris-blockchain-week-2025": ("PBW 2025", "PARIS BLOCKCHAIN WEEK"),
        "opera-for-peace-2025": ("ROME 2025", "OPERA FOR PEACE GALA, ROME"),
        "most-influential-women-of-the-world": ("PARIS 2024", "FEMMES INFLUENTES DU MONDE — LE RITZ"),
        "chateau-de-creema-2023": ("NICE 2023", "WHITE ART PARTY — CHÂTEAU DE CRÉMAT"),
        "gem-geneve-2023": ("GENÈVE 2023", "GEMGENÈVE — DESIGNER VILLAGE"),
        "monaco-film-2022": ("MONACO 2022", "FESTIVAL DU FILM DE MONACO"),
        "better-world-fund-2022": ("CANNES 2022", "BETTER WORLD FUND GALA"),
        "cannes-festival-2021": ("CANNES 2021", "FESTIVAL DE CANNES — COCKTAIL"),
        "cannes-festival-2019": ("CANNES 2019", "FESTIVAL DE CANNES — CARPET"),
        "vacheron-constantin-workshop-2016": ("GENÈVE 2014", "ATELIER JOAILLERIE VACHERON CONSTANTIN")
    }
    return mapping.get(slug, ("ÉVÉNEMENT", title))

def main():
    events_json = "c:/Users/lyies/Desktop/siteelk/scratch/downloaded_events.json"
    subpages_json = "c:/Users/lyies/Desktop/siteelk/scratch/downloaded_subpages_data.json"
    evenements_src = "c:/Users/lyies/Desktop/siteelk/localhost_v2/evenements.html"
    
    with open(events_json, 'r', encoding='utf-8') as f:
        events = json.load(f)
        
    with open(subpages_json, 'r', encoding='utf-8') as f:
        subpages_data = json.load(f)
        
    # Read navigation and footer from source file
    with open(evenements_src, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Extract nav and footer
    nav_html = str(soup.find('nav', class_='nav-bar'))
    footer_html = str(soup.find('footer', class_='site-footer'))
    
    # 1. GENERATE THE SUBPAGES
    for ev in events:
        slug = ev['slug']
        title = ev['title']
        description = ev['description']
        main_img = ev['local_image_path']
        if slug == "cannes-film-festival":
            main_img = "img/evenements/cannes-film-festival/0a3f8519-1ade-4f80-b6f9-888903d6b1c7_1_1.jpg"
        
        # Subpage details
        sub_data = subpages_data.get(slug, {"headings": [], "paragraphs": [], "local_images": []})
        gallery_images = sub_data.get('local_images', [])
        captions = clean_captions(sub_data.get('headings', []), title)
        
        kicker_short, kicker_full = get_kicker_and_location(slug, title)
        
        # Split title for dynamic span style in Hero
        words = title.split()
        if len(words) > 1:
            hero_title = " ".join(words[:-1]) + f" <span>{words[-1]}</span>"
        else:
            hero_title = title
            
        # Build gallery items
        gallery_html = ""
        for idx, img_path in enumerate(gallery_images):
            # assign a caption if available
            cap = captions[idx] if idx < len(captions) else ""
            if not cap:
                cap = kicker_short
            
            gallery_html += f"""
        <div class="gallery-item">
            <img src="{img_path}" alt="{cap} — Elke Berr Genève" loading="lazy">
            <p>{cap}</p>
        </div>"""

        subpage_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <title>{title} — Événements | Elke Berr Genève</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .event-intro {{ padding: 8rem 15vw 6rem; text-align: center; }}
        .event-intro h1 {{ font-size: 3rem; margin-bottom: 2rem; font-family: 'Playfair Display', serif; font-weight: 400; }}
        .event-intro p {{ font-size: 1.1rem; line-height: 1.8; color: #444; margin-bottom: 3rem; max-width: 800px; margin-left: auto; margin-right: auto; }}
        
        .gallery-masonry {{ columns: 2; column-gap: 2.5rem; padding: 0 6vw 10rem; max-width: 1400px; margin: 0 auto; }}
        .gallery-item {{ break-inside: avoid; margin-bottom: 2.5rem; position: relative; overflow: hidden; border: 1px solid var(--border); }}
        .gallery-item img {{ width: 100%; display: block; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1); }}
        .gallery-item:hover img {{ transform: scale(1.05); }}
        .gallery-item p {{ position: absolute; bottom: 0; left: 0; width: 100%; padding: 1.5rem; background: linear-gradient(transparent, rgba(0,0,0,0.8)); color: #fff; font-size: 0.75rem; letter-spacing: 0.1em; opacity: 0; transition: opacity 0.4s; margin: 0; font-family: 'Inter', sans-serif; text-transform: uppercase; }}
        .gallery-item:hover p {{ opacity: 1; }}
        
        @media (max-width: 1024px) {{ .gallery-masonry {{ columns: 2; }} }}
        @media (max-width: 600px) {{ .gallery-masonry {{ columns: 1; }} }}
    </style>
</head>
<body>
    {nav_html}
      <div class="hero-video-container hero-collection" style="background: url('{main_img}') no-repeat center top; background-size: cover; background-color: #0c0f0a;">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <span class="kicker kicker--light">{kicker_full}</span>
            <h1>{hero_title}</h1>
            <div class="hero-divider"></div>
            <p>Événements Elke Berr Genève</p>
        </div>
    </div>

    <section class="event-intro">
        <span class="kicker">{kicker_short}</span>
        <h1>{title}</h1>
        <p>{description}</p>
        <a href="evenements.html" class="btn btn--secondary">← Retour aux événements</a>
    </section>

    <div class="gallery-masonry">{gallery_html}
    </div>

    {footer_html}
</body>
</html>
"""
        
        out_path = f"c:/Users/lyies/Desktop/siteelk/localhost_v2/{slug}.html"
        with open(out_path, 'w', encoding='utf-8') as out_f:
            out_f.write(subpage_content)
        print(f"Generated subpage: {slug}.html")
        
    # 2. GENERATE THE INDEX PAGE: evenements.html
    grid_cards_html = ""
    for ev in events:
        slug = ev['slug']
        title = ev['title']
        description = ev['description']
        main_img = ev['local_image_path']
        if slug == "cannes-film-festival":
            main_img = "img/evenements/cannes-film-festival/image00006.jpg"
        elif slug == "better-world-fund-2022":
            main_img = "img/evenements/better-world-fund-2022/Screenshot_2025-02-12_at_11.03.37.png"
        elif slug == "cannes-festival-2021":
            main_img = "img/evenements/cannes-festival-2021/gettyimages-1327677406-1024x1024.jpg"
        kicker_short, kicker_full = get_kicker_and_location(slug, title)
        
        grid_cards_html += f"""
        <div class="event-card">
            <div class="event-card-img-wrapper">
                <img src="{main_img}" alt="{title} — Elke Berr Genève" loading="lazy">
            </div>
            <div class="event-card-content">
                <span class="event-card-kicker">{kicker_short}</span>
                <h3 class="event-card-title">{title}</h3>
                <p class="event-card-desc">{description}</p>
                <a href="{slug}.html" class="event-card-link">Découvrir l'événement →</a>
            </div>
        </div>"""
        
    index_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Découvrez les événements, expositions et soirées exclusives de la Maison de Haute Joaillerie Elke Berr Genève.">
    <title>Événements — Elke Berr Genève</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .events-hero {{
            height: 60vh;
            background: url('img/launch_hero.jpg') no-repeat center 30%;
            background-size: cover;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            margin-bottom: 8rem;
        }}
        .events-hero::after {{
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.4);
        }}
        .events-hero-content {{
            position: relative;
            z-index: 2;
            color: #fff;
            padding: 0 4vw;
        }}
        .events-hero-content h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            font-weight: 400;
            letter-spacing: 0.05em;
            margin: 0;
            color: #ffffff;
        }}
        .events-hero-content p {{
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-top: 1.5rem;
            opacity: 0.9;
        }}
        
        .events-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 4rem 3rem;
            padding: 0 6vw 10rem;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .event-card {{
            background: transparent;
            border: 1px solid var(--border);
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        .event-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
            border-color: var(--primary);
        }}
        .event-card-img-wrapper {{
            width: 100%;
            height: 300px;
            overflow: hidden;
            position: relative;
        }}
        .event-card img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .event-card:hover img {{
            transform: scale(1.05);
        }}
        .event-card-content {{
            padding: 2.5rem;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .event-card-kicker {{
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--primary);
            margin-bottom: 1rem;
        }}
        .event-card-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            font-weight: 400;
            line-height: 1.3;
            margin-bottom: 1rem;
            color: var(--text-color);
        }}
        .event-card-desc {{
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
            line-height: 1.6;
            color: #666;
            margin-bottom: 2rem;
            flex-grow: 1;
        }}
        .event-card-link {{
            font-family: 'Inter', sans-serif;
            font-size: 0.75rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--text-color);
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: color 0.3s;
            margin-top: auto;
        }}
        .event-card-link:hover {{
            color: var(--primary);
        }}
        
        @media (max-width: 1024px) {{
            .events-grid {{
                grid-template-columns: repeat(2, 1fr);
                gap: 3rem;
            }}
        }}
        @media (max-width: 768px) {{
            .events-hero {{ height: 50vh; margin-bottom: 5rem; }}
            .events-hero-content h1 {{ font-size: 2.8rem; }}
        }}
        @media (max-width: 600px) {{
            .events-grid {{
                grid-template-columns: 1fr;
                gap: 2.5rem;
                padding: 0 4vw 8rem;
            }}
        }}
    </style>
</head>
<body>
    {nav_html}
    <script src="js/main.js"></script>

    <div class="events-hero">
        <div class="events-hero-content">
            <h1>ÉVÉNEMENTS</h1>
            <p>Maison Elke Berr Genève</p>
        </div>
    </div>

    <div class="events-grid">{grid_cards_html}
    </div>

    {footer_html}
</body>
</html>
"""
    
    with open(evenements_src, 'w', encoding='utf-8') as out_idx:
        out_idx.write(index_content)
    print("Successfully generated index: evenements.html")

if __name__ == "__main__":
    main()
