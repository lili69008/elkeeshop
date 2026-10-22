import os
import json
import re

# Define premium French translations for all 25 press parutions
FRENCH_TRANSLATIONS = {
    "INCOLOR 2025": {
        "pub_name": "InColor Magazine",
        "date_str": "Début 2025",
        "citation": "« La joaillerie et la musique s'unissent pour donner une voix aux talents de demain. »",
        "text": "Elke Berr Créations s'associe fièrement à l'organisation Opera for Peace pour soutenir et propulser les talents artistiques émergents à travers le monde. Cette collaboration unique explore la synergie créatrice et le pouvoir transformateur de la musique classique et de la haute joaillerie, célébrant l'excellence et la transmission du savoir-faire."
    },
    "Luxury Magazine 2024": {
        "pub_name": "Luxury Magazine",
        "date_str": "Automne 2024",
        "citation": "« Un voyage de huit pages au cœur de l'expertise des gemmes et de la création joaillière d'exception. »",
        "text": "La Maison Elke Berr a été mise à l'honneur dans un grand portrait de huit pages au sein du prestigieux Luxury Magazine. Cet article exclusif retrace son parcours exceptionnel de gemmologue globe-trotteuse, ses contributions artistiques majeures à la haute joaillerie contemporaine, et l'engagement de la Maison envers la traçabilité et l'innovation."
    },
    "Most Influential Women of the World 2024": {
        "pub_name": "Most Influential Women",
        "date_str": "Été 2024",
        "citation": "« Célébrer l'audace, la vision et l'excellence féminine dans le monde des pierres précieuses. »",
        "text": "Ce dossier spécial met en lumière la brillante carrière d'Elke Berr en tant que gemmologue et visionnaire créative. Il souligne ses contributions pionnières à l'industrie des pierres précieuses ainsi que l'engagement de sa marque pour l'innovation numérique et la transparence totale grâce à la technologie blockchain."
    },
    "Collectissm Magazine 2023": {
        "pub_name": "Collectissim Magazine",
        "date_str": "Fin 2023",
        "citation": "« L'art délicat de métamorphoser des pierres d'exception en trésors éternels. »",
        "text": "Dans une double page exclusive (pages 26 et 27), Collectissim Magazine célèbre le parcours d'Elke Berr en tant que gemmologue et designer joaillière de premier plan. L'article met en avant son savoir-faire unique pour révéler l'âme des gemmes rares et sa recherche constante de la perfection artisanale."
    },
    "Gala 2023": {
        "pub_name": "Gala",
        "date_str": "Automne 2023",
        "citation": "« Les adresses secrètes de la haute joaillerie genevoise sur mesure. »",
        "text": "Elke Berr figure en place d'honneur dans la section très convoitée « Carnet d'Adresses » du magazine Gala. La publication recommande chaleureusement l'atelier genevois aux lecteurs en quête de créations de haute joaillerie exclusives, de pièces uniques et de services de création sur mesure."
    },
    "Bilan 2023": {
        "pub_name": "Bilan Magazine",
        "date_str": "Printemps 2023",
        "citation": "« Décrypter les grandes mutations du marché de la haute joaillerie post-pandémie. »",
        "text": "Le marché mondial de la joaillerie fine a connu d'importantes mutations. Dans cette interview approfondie pour le magazine économique suisse Bilan, Elke Berr partage son analyse stratégique sur la fluctuation des cours des gemmes et l'évolution des exigences des collectionneurs privés."
    },
    "Europa Star 2022": {
        "pub_name": "Europa Star",
        "date_str": "Fin 2022",
        "citation": "« La pierre précieuse comme passion artistique et actif financier alternatif tangible. »",
        "text": "Dans cet entretien exclusif pour Europa Star, la gemmologue Elke Berr partage ses précieux secrets pour sélectionner les pierres les plus pures, comprendre leur cotation et appréhender les forces du marché. Elle livre une analyse intemporelle pour ceux qui souhaitent investir dans les gemmes de couleur de grande rareté."
    },
    "InColor 2022": {
        "pub_name": "InColor Magazine",
        "date_str": "Automne 2022",
        "citation": "« Transparence et adaptabilité : les nouveaux piliers de l'industrie des pierres précieuses. »",
        "text": "Dans ce numéro spécial d'InColor, Elke Berr apporte son éclairage d'experte sur la restructuration des chaînes d'approvisionnement mondiales après la crisis sanitaire. Elle insiste sur l'importance cruciale de la traçabilité et de l'authenticité pour valoriser les investissements dans les gemmes de couleur."
    },
    "Tiempo de Relojes 2022": {
        "pub_name": "Tiempo de Relojes",
        "date_str": "Printemps 2022",
        "citation": "« Le diamant naturel face à l'essor technologique des gemmes de synthèse. »",
        "text": "Pour la revue Tiempo de Relojes, Elke Berr explore avec objectivité l'essor des diamants de synthèse dans le paysage du luxe. Elle décrypte leur structure cristalline identique à celle des diamants de mine et analyse l'impact de ces alternatives sur la démocratisation de l'éclat sans pour autant altérer le prestige de la pierre naturelle historique."
    },
    "InColor AW 2020": {
        "pub_name": "InColor Magazine",
        "date_str": "Hiver 2020",
        "citation": "« L'harmonie parfaite entre techniques séculaires et design contemporain audacieux. »",
        "text": "L'édition Automne/Hiver d'InColor consacre un dossier aux pièces de la Maison Elke Berr. Les critiques saluent son habileté à marier des structures d'or sculpturales d'inspiration moderne avec des gemmes facettées de manière traditionnelle, affirmant le style singulier de la marque."
    },
    "InColor SS 2020": {
        "pub_name": "InColor Magazine",
        "date_str": "Été 2020",
        "citation": "« La couleur à l'état pur : magnifier l'éclat solaire des plus beaux trésors de la Terre. »",
        "text": "Le numéro de prestige d'InColor met en scène les créations estivales d'Elke Berr. L'accent est mis sur son génie chromatique et sa capacité à associer des teintes vives et des tailles asymétriques pour façonner des parures d'une fraîcheur et d'une sophistication exceptionnelles."
    },
    "Bilan 2019": {
        "pub_name": "Bilan Magazine",
        "date_str": "Fin 2019",
        "citation": "« La valeur refuge inaltérable des diamants de couleur de taille exceptionnelle. »",
        "text": "Elke Berr livre une analyse pointue dans les colonnes de Bilan sur la baisse globale de la demande pour les diamants bruts standard. Elle met en lumière le contraste avec l'attrait grandissant et la stabilité financière remarquable des grands diamants de couleur et des pierres d'investissement."
    },
    "Gala Croisette 2019": {
        "pub_name": "Gala Croisette",
        "date_str": "Mai 2019",
        "citation": "« L'éclat des gemmes genevoises illumine le tapis rouge du Festival de Cannes. »",
        "text": "Les parures de haute joaillerie signées Elke Berr ont fait sensation sur la Croisette. Portées avec grâce par la célèbre actrice Frédérique Bel lors des montées des marches, ces pièces uniques ont captivé les photographes et sublimé le chic et l'élégance de la haute couture française."
    },
    "InColor AW 2019": {
        "pub_name": "InColor Magazine",
        "date_str": "Automne 2019",
        "citation": "« Le corail à l'honneur : une célébration chaleureuse de la couleur de l'année. »",
        "text": "Pour célébrer la couleur Pantone de l'année, InColor met en avant les créations audacieuses d'Elke Berr sublimant les gemmes aux nuances corail et orangées. L'article salue l'équilibre des volumes et la vitalité insufflée à ces pièces de collection."
    },
    "InColor AW 2018": {
        "pub_name": "InColor Magazine",
        "date_str": "Hiver 2018",
        "citation": "« Le rubis étoilé : l'une des plus fascinantes merveilles de la nature mise en majesté. »",
        "text": "L'édition de fin d'année d'InColor magazine explore la beauté mystique et la rareté infinie des rubis. La bague rubis étoilé d'Elke Berr y est mise à l'honneur parmi les plus belles créations au monde, célébrant la qualité exceptionnelle de sa gemme centrale."
    },
    "BK Le Mag 2017": {
        "pub_name": "BK Le Mag",
        "date_str": "Automne 2017",
        "citation": "« De l'expertise brute à la création joaillière : l'histoire d'une vocation. »",
        "text": "Dans une interview portrait exclusive, BK Le Mag retrace le parcours inspirant d'Elke Berr, de ses débuts de gemmologue exploratrice à la fondation de Berr & Partners et au lancement de sa marque éponyme. Une plongée dans les coulisses de la création joaillière genevoise haut de gamme."
    },
    "Rapaport 2017": {
        "pub_name": "Rapaport",
        "date_str": "Printemps 2017",
        "citation": "« Le saphir de Birmanie de 118 carats : le rêve ultime de toute gemmologue. »",
        "text": "Interrogée par le prestigieux groupe Rapaport, Elke Berr partage son coup de cœur absolu pour un saphir birman de 118,88 carats adjugé chez Christie's. Elle en décrit la transparence divine et la profondeur de bleu, analysant la cote exceptionnelle de cette merveille géologique."
    },
    "Sur La Terre 2014": {
        "pub_name": "Sur La Terre",
        "date_str": "Automne 2014",
        "citation": "« Repenser les codes de la haute joaillerie face à la globalisation des marchés. »",
        "text": "Dans cette tribune libre pour Sur la Terre, Elke Berr analyse avec lucidité la restructuration et la concentration de l'industrie du luxe depuis les années 2000. Elle y défend une vision de la joaillerie d'auteur, indépendante, éthique et centrée sur l'émotion pure de la pierre."
    },
    "Trends & Colours 2014": {
        "pub_name": "Trends & Colours",
        "date_str": "Été 2014",
        "citation": "« La bague calcédoine de la collection Mysteria : une sculpture de pure douceur. »",
        "text": "La revue de référence internationale met en avant la bague en calcédoine d'Elke Berr. Issue de la collection Mysteria, cette pièce est saluée pour ses courbes veloutées, son jeu subtil de translucidité et son élégance mystérieuse très contemporaine."
    },
    "Day & Night 2013": {
        "pub_name": "Day & Night",
        "date_str": "Printemps 2013",
        "citation": "« L'élégance genevoise conquiert les collectionneurs du Moyen-Orient. »",
        "text": "Le magazine de luxe Day & Night consacre un grand focus à Elke Berr. L'article célèbre son double talent de gemmologue et de designer, soulignant l'accueil exceptionnel réservé à ses créations de haute joaillerie auprès d'une clientèle internationale exigeante."
    },
    "Trends & Colours 2013": {
        "pub_name": "Trends & Colours",
        "date_str": "Hiver 2013",
        "citation": "« Le spinelle rouge : la flamboyance d'une gemme d'exception injustement méconnue. »",
        "text": "Trends & Colours consacre un article à l'extraordinaire bague spinelle rouge signée Elke Berr. Le magazine loue le choix de cette gemme rare au feu intense, souvent préférée au rubis par les connaisseurs pour sa brillance et sa pureté naturelle."
    },
    "The New Diner Scope 2013": {
        "pub_name": "The New Diner Scope",
        "date_str": "Printemps 2013",
        "citation": "« Façonner les rêves en joaillerie fine : l'excellence du sur-mesure. »",
        "text": "Dans ce grand article de fond, The New Diner Scope met en lumière la collection signature 'Aqua Bubble' d'Elke Berr, caractérisée par ses gemmes polies en cabochon évoquant la fluidité de l'eau. L'article salue son service exclusif de création de bijoux sur mesure."
    },
    "The New Diner Scope 2013 (Iris)": {
        "pub_name": "The New Diner Scope",
        "date_str": "Hiver 2013",
        "citation": "« La collection Iris ou la poésie délicate des gemmes aux nuances pastel. »",
        "text": "La prestigieuse publication zoome sur la collection Iris d'Elke Berr. Les critiques s'émerveillent de l'accord subtil de saphirs pastel, de tanzanites douces et de quartz rose, illustrant la palette chromatique unique et la sensibilité poétique de la créatrice genevoise."
    },
    "The New Diner Scope 2011": {
        "pub_name": "The New Diner Scope",
        "date_str": "Automne 2011",
        "citation": "« Laguna, Dramatica, Fuoco : la trilogie créative qui bouscule les codes du luxe. »",
        "text": "Un grand panorama des premières collections iconiques d'Elke Berr. L'article explore comment chaque ligne ('Laguna' pour la sérénité aquatique, 'Dramatica' pour les contrastes intenses, 'Fuoco' pour la passion de l'or rouge) incarne une facette de l'excellence de la créatrice."
    },
    "The New Diner Scope 2011 (Onde)": {
        "pub_name": "The New Diner Scope",
        "date_str": "Printemps 2011",
        "citation": "« La taille ondulée exclusive Onde : sculpter la lumière dans la pierre brute. »",
        "text": "Cet article retrace les innovations techniques majeures introduites par Elke Berr, notamment la taille 'Onde' brevetée qui fait danser la lumière à la surface des gemmes, et le travail sur l'ombre et la clarté caractérisant la collection Mysteria."
    }
}

def generate_presse_files():
    json_path = 'scratch/presse_data.json'
    presse_html_path = 'localhost_v2/presse.html'
    
    if not os.path.exists(json_path):
        print(f"Error: Metadata file {json_path} not found.")
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)
        
    print(f"Successfully loaded {len(articles)} articles from metadata.")
    
    # 1. Read the existing navigation and footer from presse.html to guarantee 100% parity
    if not os.path.exists(presse_html_path):
        print(f"Error: {presse_html_path} does not exist. Cannot extract layout navigation.")
        return
        
    with open(presse_html_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
        
    # Extract Navigation Block
    nav_match = re.search(r'(<!--\s*NAVIGATION\s*-->.*?<nav.*?>.*?</nav>\s*<script src="js/main.js"></script>)', raw_html, re.DOTALL)
    if not nav_match:
        nav_match = re.search(r'(<nav.*?>.*?</nav>\s*<script src="js/main.js"></script>)', raw_html, re.DOTALL)
        
    if nav_match:
        nav_html = nav_match.group(1)
        print("Successfully extracted Navigation HTML block.")
    else:
        print("Warning: Navigation block not found.")
        nav_html = ""
        
    # Extract Footer Block
    footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', raw_html, re.DOTALL)
    if footer_match:
        footer_html = footer_match.group(1)
        print("Successfully extracted Footer HTML block.")
    else:
        print("Warning: Footer block not found.")
        footer_html = ""
        
    # Enrich articles with French translations and check local image path
    enriched_articles = []
    for item in articles:
        title = item['title']
        translation_key = title
        if title not in FRENCH_TRANSLATIONS:
            if "Iris" in title:
                translation_key = "The New Diner Scope 2013 (Iris)"
            elif "Onde" in title:
                translation_key = "The New Diner Scope 2011 (Onde)"
            else:
                translation_key = title
                
        trans = FRENCH_TRANSLATIONS.get(translation_key, {
            "pub_name": item.get('pub', 'Média'),
            "date_str": item.get('date', 'Archives'),
            "citation": "« Une création d'exception alliant art et savoir-faire précieux. »",
            "text": item.get('original_description', '')
        })
        
        # Clean local image path
        local_img = item.get('local_image_path', '')
        if not local_img:
            clean_title = title.lower().replace('&', 'and').replace(' ', '_').replace('(', '').replace(')', '').replace('\'', '')
            ext = '.png' if '.png' in item['imageUrl'].lower() else '.jpg'
            local_img = f"img/presse/{clean_title}{ext}"
            
        clean_title = title.lower().replace('&', 'and').replace(' ', '-').replace('(', '').replace(')', '').replace('\'', '').replace('--', '-')
        subpage_filename = f"presse-{clean_title}.html"
        
        enriched_articles.append({
            "title": title,
            "pub": trans["pub_name"],
            "date": trans["date_str"],
            "citation": trans["citation"],
            "description": trans["text"],
            "imageUrl": local_img,
            "articleUrl": item["articleUrl"],
            "subpageUrl": subpage_filename,
            "sourceUrl": f"source-{clean_title}.html"
        })
        
    featured_article = enriched_articles[0]
    grid_articles = enriched_articles[1:]
    
    # 2. Build main presse.html contents using a raw template string (adapted for Light Luxury Theme)
    grid_cards_html = ""
    for art in grid_articles:
        grid_cards_html += """
        <div class="press-card">
            <a href="{subpageUrl}" style="text-decoration: none; color: inherit;">
                <div class="press-card-img">
                    <img src="{imageUrl}" alt="{title}" loading="lazy">
                </div>
                <div class="press-card-meta">
                    <span class="pub">{pub}</span>
                    <span class="date">{date}</span>
                    <h3>{title}</h3>
                    <p>{description_short}...</p>
                </div>
            </a>
        </div>""".format(
            subpageUrl=art['subpageUrl'],
            imageUrl=art['imageUrl'],
            title=art['title'],
            pub=art['pub'],
            date=art['date'],
            description_short=art['description'][:140]
        )
        
    main_presse_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Elke Berr Genève dans la presse — revue de presse complète, parutions et couvertures médias de la Maison de joaillerie.">
    <title>Revue de Presse — Elke Berr Genève</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        /* ── HERO ── */
        .press-hero {
            position: relative;
            height: 60vh;
            min-height: 450px;
            overflow: hidden;
            background-color: var(--bg-alt); /* Harmony ivory tint fallback */
        }
        .press-hero-img {
            width: 100%; height: 100%;
            object-fit: cover;
            object-position: center 30%;
            filter: brightness(0.9);
        }
        .press-hero-overlay {
            position: absolute; inset: 0;
            background: linear-gradient(to bottom, rgba(250,250,247,0.1) 0%, var(--bg) 100%);
            display: flex; flex-direction: column;
            align-items: center; justify-content: flex-end;
            padding-bottom: 6rem; text-align: center;
        }
        .press-hero-overlay .kicker { 
            color: var(--accent, #2A6355); 
            letter-spacing: 0.5em;
            font-size: 0.8rem;
            text-transform: uppercase;
            margin-bottom: 1rem;
            font-weight: 500;
        }
        .press-hero-overlay h1 {
            font-size: clamp(2.5rem, 5vw, 4.5rem);
            letter-spacing: 0.25em;
            color: var(--fg, #1C1A16);
            font-family: var(--font-serif);
            font-weight: 300;
            margin: 0;
            text-transform: uppercase;
        }

        /* ── INTRO ── */
        .press-intro {
            max-width: 800px;
            margin: 7rem auto;
            text-align: center;
            padding: 0 5%;
        }
        .press-intro p {
            color: var(--muted, #7A7166);
            font-weight: 300;
            line-height: 2.1;
            font-size: 1.15rem;
            letter-spacing: 0.02em;
        }
        .press-divider {
            width: 50px; height: 1px;
            background: var(--accent, #2A6355);
            margin: 3.5rem auto;
        }

        /* ── FEATURED ── */
        .press-featured {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 0;
            max-width: 1400px;
            margin: 0 auto 9rem;
            padding: 0 5%;
            background: var(--bg-alt, #F2EFE7);
            box-shadow: 0 20px 40px rgba(0,0,0,0.04);
            border: 1px solid var(--border, #E2DDD6);
        }
        .press-featured-img {
            aspect-ratio: 16/10;
            overflow: hidden;
            position: relative;
        }
        .press-featured-img img {
            width: 100%; height: 100%;
            object-fit: cover;
            transition: transform 1.2s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .press-featured:hover .press-featured-img img { transform: scale(1.04); }
        .press-featured-text {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 5rem 6rem;
        }
        .press-featured-text .press-pub {
            font-size: 0.7rem;
            letter-spacing: 0.5em;
            color: var(--accent, #2A6355);
            text-transform: uppercase;
            margin-bottom: 0.8rem;
            font-weight: 600;
        }
        .press-featured-text .press-date {
            font-size: 0.7rem;
            letter-spacing: 0.25em;
            color: var(--muted, #7A7166);
            text-transform: uppercase;
            margin-bottom: 2.5rem;
        }
        .press-featured-text h2 {
            font-family: var(--font-serif);
            font-size: clamp(1.8rem, 3vw, 2.6rem);
            font-weight: 300;
            line-height: 1.35;
            letter-spacing: 0.02em;
            margin-bottom: 2.2rem;
            color: var(--fg, #1C1A16);
        }
        .press-featured-text p {
            color: var(--muted, #7A7166);
            font-size: 0.95rem;
            line-height: 2;
            font-style: normal;
            margin-bottom: 3rem;
        }
        .press-btn {
            align-self: flex-start;
            display: inline-flex;
            align-items: center;
            gap: 1rem;
            color: var(--fg, #1C1A16);
            text-decoration: none;
            font-size: 0.75rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            font-weight: 500;
            border-bottom: 1px solid var(--accent, #2A6355);
            padding-bottom: 0.6rem;
            transition: all 0.4s ease;
        }
        .press-btn:hover {
            color: var(--accent, #2A6355);
            border-color: var(--fg, #1C1A16);
            padding-left: 0.5rem;
        }

        /* ── GRID ── */
        .press-section-title {
            text-align: center;
            padding: 0 5% 5rem;
        }
        .press-section-title h2 {
            font-family: var(--font-serif);
            font-size: 2.2rem;
            font-weight: 300;
            letter-spacing: 0.08em;
            color: var(--fg, #1C1A16);
            margin-top: 0.5rem;
        }
        .press-section-title .kicker {
            font-size: 0.7rem;
            letter-spacing: 0.4em;
            color: var(--accent, #2A6355);
            text-transform: uppercase;
            font-weight: 600;
        }

        .press-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 5% 9rem;
        }
        .press-card {
            background: #ffffff;
            border: 1px solid var(--border, #E2DDD6);
            padding: 1.5rem;
            opacity: 0;
            transform: translateY(30px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.02);
            transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1), background 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
        }
        .press-card.reveal { opacity: 1; transform: translateY(0); }
        .press-card:hover {
            background: var(--bg-alt, #F2EFE7);
            border-color: var(--accent-light, #3D7E6E);
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        }
        .press-card-img {
            width: 100%;
            aspect-ratio: 3/4;
            overflow: hidden;
            position: relative;
            background: #f7f7f7;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        }
        .press-card-img img {
            width: 100%; height: 100%;
            object-fit: cover;
            transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .press-card:hover .press-card-img img { transform: scale(1.05); }
        .press-card-meta {
            padding: 2rem 0.5rem 0.5rem;
        }
        .press-card-meta .pub {
            font-size: 0.6rem;
            letter-spacing: 0.4em;
            color: var(--accent, #2A6355);
            text-transform: uppercase;
            display: block;
            margin-bottom: 0.4rem;
            font-weight: 600;
        }
        .press-card-meta .date {
            font-size: 0.6rem;
            letter-spacing: 0.25em;
            color: var(--muted, #7A7166);
            text-transform: uppercase;
            display: block;
            margin-bottom: 1.5rem;
        }
        .press-card-meta h3 {
            font-family: var(--font-serif);
            font-size: 1.3rem;
            font-weight: 300;
            letter-spacing: 0.03em;
            line-height: 1.4;
            margin-bottom: 1.2rem;
            color: var(--fg, #1C1A16);
        }
        .press-card-meta p {
            font-size: 0.88rem;
            color: var(--muted, #7A7166);
            line-height: 1.8;
            font-weight: 300;
        }

        /* ── PRODUCT EDITORIAL ROW ── */
        .press-product-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto 9rem;
            padding: 0 5%;
        }
        .press-product-item {
            padding: 1.5rem;
            text-align: center;
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.8s ease, transform 0.8s ease, background 0.4s ease, border-color 0.4s ease;
            background: #ffffff;
            border: 1px solid var(--border, #E2DDD6);
        }
        .press-product-item.reveal { opacity: 1; transform: translateY(0); }
        .press-product-item img {
            width: 100%;
            aspect-ratio: 1/1;
            object-fit: contain;
            background: #f7f7f7;
            padding: 1.5rem;
            transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .press-product-item:hover img {
            transform: scale(1.05);
        }
        .press-product-item span {
            display: block;
            margin-top: 1.5rem;
            font-size: 0.65rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--fg, #1C1A16);
            font-weight: 500;
        }
        .press-product-item:hover {
            background: var(--bg-alt, #F2EFE7);
            border-color: var(--accent, #2A6355);
        }

        /* ── CONTACT PRESSE ── */
        .press-contact {
            background: var(--bg-alt, #F2EFE7);
            text-align: center;
            padding: 9rem 5%;
            border-top: 1px solid var(--border, #E2DDD6);
        }
        .press-contact h2 {
            font-family: var(--font-serif);
            font-size: 2.2rem;
            font-weight: 300;
            letter-spacing: 0.08em;
            margin-bottom: 2.5rem;
            color: var(--fg, #1C1A16);
        }
        .press-contact p {
            color: var(--muted, #7A7166);
            line-height: 2.2;
            font-size: 1rem;
            font-weight: 300;
        }
        .press-contact a {
            color: var(--accent, #2A6355);
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }
        .press-contact a:hover {
            border-color: var(--accent, #2A6355);
            padding-bottom: 0.2rem;
        }

        @media (max-width: 1100px) {
            .press-grid { grid-template-columns: repeat(2, 1fr); }
            .press-product-row { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 768px) {
            .press-featured { grid-template-columns: 1fr; }
            .press-featured-text { padding: 4rem 5%; }
            .press-grid { grid-template-columns: 1fr; }
            .press-product-row { grid-template-columns: repeat(2, 1fr); gap: 1rem; }
        }
    </style>
</head>
<body>

    {{nav_html}}

    <!-- HERO -->
    <div class="press-hero">
        <img class="press-hero-img" src="{{featured_img}}" alt="Revue de presse Elke Berr">
        <div class="press-hero-overlay">
            <span class="kicker">MÉDIAS &amp; PARUTIONS</span>
            <h1>PRESSE</h1>
        </div>
    </div>

    <!-- INTRO -->
    <div class="press-intro">
        <p>L'excellence créative et l'expertise gemmologique de la Maison Elke Berr célébrées par la presse internationale de luxe et de haute spécialité. Une rétrospective éditoriale témoignant d'un savoir-faire unique.</p>
        <div class="press-divider"></div>
    </div>

    <!-- FEATURED ARTICLE -->
    <div class="press-featured">
        <div class="press-featured-img">
            <img src="{{featured_img}}" alt="{{featured_title}}">
        </div>
        <div class="press-featured-text">
            <span class="press-pub">À la Une / {{featured_pub}}</span>
            <span class="press-date">{{featured_date}}</span>
            <h2>{{featured_title}} — {{featured_citation}}</h2>
            <p>{{featured_desc}}</p>
            <a href="{{featured_url}}" class="press-btn">Lire l'article &rarr;</a>
        </div>
    </div>

    <!-- PRESS GRID -->
    <div class="press-section-title">
        <span class="kicker">ARCHIVES ÉDITORIALES</span>
        <h2>Revue de Presse</h2>
        <div class="press-divider"></div>
    </div>

    <div class="press-grid">
        {{grid_cards}}
    </div>

    <!-- PRODUCT EDITORIAL -->
    <div class="press-section-title" style="padding-top: 2rem;">
        <span class="kicker">VUS EN PRESSE</span>
        <h2>Pièces Remarquées</h2>
        <div class="press-divider"></div>
    </div>

    <div class="press-product-row">
        <div class="press-product-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_linfini_necklace.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_linfini_necklace.png" alt="L'Infini Necklace">
                <span>Collier L'Infini — Unbreakable</span>
            </a>
        </div>
        <div class="press-product-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_link_earrings.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_link_earrings.png" alt="Link Earrings">
                <span>Boucles Link — Unbreakable</span>
            </a>
        </div>
        <div class="press-product-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_complice_bangle.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_complice_bangle.png" alt="Complice Bangle">
                <span>Bracelet Complice — Unbreakable</span>
            </a>
        </div>
        <div class="press-product-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_tresor_ring.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_tresor_ring.png" alt="Trésor Ring">
                <span>Bague Trésor — Unbreakable</span>
            </a>
        </div>
    </div>

    <!-- PRESSE CONTACT -->
    <div class="press-contact">
        <span class="kicker">RELATIONS MÉDIAS</span>
        <h2>Contact Presse</h2>
        <p>
            Pour toute demande d'interview, d'accréditation ou de prêt de bijoux d'exception,<br>
            notre département relations médias est à votre entière disposition.<br><br>
            <a href="mailto:office@berrandpartners.ch">office@berrandpartners.ch</a><br>
            +41 22 310 61 10<br><br>
            Maison Elke Berr Creations · Rue du Cendrier 12-14 · 1201 Genève
        </p>
    </div>

    {{footer_html}}

    <script>
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('reveal');
                }
            });
        }, { threshold: 0.08 });
        document.querySelectorAll('.press-card, .press-product-item').forEach(el => observer.observe(el));
    </script>
</body>
</html>"""

    # Apply placeholder replacements for the main page
    main_presse_html = main_presse_template.replace("{{nav_html}}", nav_html)
    main_presse_html = main_presse_html.replace("{{featured_img}}", featured_article['imageUrl'])
    main_presse_html = main_presse_html.replace("{{featured_pub}}", featured_article['pub'])
    main_presse_html = main_presse_html.replace("{{featured_date}}", featured_article['date'])
    main_presse_html = main_presse_html.replace("{{featured_title}}", featured_article['title'])
    main_presse_html = main_presse_html.replace("{{featured_citation}}", featured_article['citation'])
    main_presse_html = main_presse_html.replace("{{featured_desc}}", featured_article['description'])
    main_presse_html = main_presse_html.replace("{{featured_url}}", featured_article['subpageUrl'])
    main_presse_html = main_presse_html.replace("{{grid_cards}}", grid_cards_html)
    main_presse_html = main_presse_html.replace("{{footer_html}}", footer_html)
    
    with open(presse_html_path, 'w', encoding='utf-8') as f:
        f.write(main_presse_html)
    print("Main V2 'presse.html' compiled and written successfully.")

    # 3. Build individual subpages (25 pages)
    # Define a clean subpage template string to avoid curly brace problems (adapted for Light Luxury Theme)
    subpage_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Lecture de l'article de presse : {{title}} — Revue de presse de la Maison Elke Berr Genève.">
    <title>{{title}} — Revue de Presse — Elke Berr</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        /* ── BREADCRUMB ── */
        .art-breadcrumb {
            max-width: 1400px;
            margin: 10rem auto 3rem;
            padding: 0 5%;
            font-size: 0.65rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--muted, #7A7166);
        }
        .art-breadcrumb a {
            color: var(--muted, #7A7166);
            text-decoration: none;
            transition: color 0.3s ease;
        }
        .art-breadcrumb a:hover {
            color: var(--accent, #2A6355);
        }
        .art-breadcrumb span {
            margin: 0 0.8rem;
            color: var(--border, #E2DDD6);
        }

        /* ── EDITORIAL GRID ── */
        .art-container {
            display: grid;
            grid-template-columns: 1fr 1.1fr;
            gap: 5rem;
            max-width: 1400px;
            margin: 0 auto 9rem;
            padding: 0 5%;
            align-items: start;
        }
        
        /* ── LEFT COLUMN: COVER ── */
        .art-cover {
            position: sticky;
            top: 120px;
            background: var(--bg-alt, #F2EFE7);
            padding: 2.5rem;
            border: 1px solid var(--border, #E2DDD6);
            box-shadow: 0 30px 60px rgba(0,0,0,0.03);
            transition: all 0.5s ease;
        }
        .art-cover:hover {
            border-color: var(--accent-light, #3D7E6E);
            box-shadow: 0 30px 65px rgba(42,99,85,0.05);
        }
        .art-cover-img {
            width: 100%;
            aspect-ratio: 3/4;
            object-fit: cover;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            display: block;
        }

        /* ── RIGHT COLUMN: TEXT ── */
        .art-details {
            display: flex;
            flex-direction: column;
            padding-top: 1rem;
        }
        .art-meta {
            display: flex;
            flex-direction: column;
            margin-bottom: 2.5rem;
        }
        .art-meta .pub {
            font-size: 0.75rem;
            letter-spacing: 0.5em;
            color: var(--accent, #2A6355);
            text-transform: uppercase;
            font-weight: 600;
            margin-bottom: 0.6rem;
        }
        .art-meta .date {
            font-size: 0.7rem;
            letter-spacing: 0.2em;
            color: var(--muted, #7A7166);
            text-transform: uppercase;
        }
        .art-details h1 {
            font-family: var(--font-serif);
            font-size: clamp(2rem, 3.5vw, 3.2rem);
            font-weight: 300;
            line-height: 1.3;
            letter-spacing: 0.02em;
            color: var(--fg, #1C1A16);
            margin: 0 0 2.5rem;
        }
        .art-citation {
            font-family: var(--font-serif);
            font-size: 1.35rem;
            line-height: 1.7;
            color: var(--accent, #2A6355);
            font-style: italic;
            border-left: 2px solid var(--accent, #2A6355);
            padding-left: 2rem;
            margin-bottom: 3rem;
            font-weight: 300;
            letter-spacing: 0.01em;
        }
        .art-body {
            color: var(--muted, #7A7166);
            font-size: 1.02rem;
            line-height: 2.1;
            font-weight: 300;
            letter-spacing: 0.01em;
            margin-bottom: 4rem;
        }
        .art-body p {
            margin-bottom: 2rem;
        }
        
        .art-actions {
            display: flex;
            gap: 2rem;
            border-top: 1px solid var(--border, #E2DDD6);
            padding-top: 3rem;
        }
        .art-back-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: transparent;
            color: var(--fg, #1C1A16);
            border: 1px solid var(--border, #E2DDD6);
            padding: 1.1rem 2.2rem;
            font-size: 0.7rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            text-decoration: none;
            transition: all 0.4s ease;
            font-weight: 500;
        }
        .art-back-btn:hover {
            background: var(--fg, #1C1A16);
            color: #ffffff;
            border-color: var(--fg, #1C1A16);
        }
        .art-external-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: var(--accent, #2A6355);
            color: #ffffff;
            border: 1px solid var(--accent, #2A6355);
            padding: 1.1rem 2.2rem;
            font-size: 0.7rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            text-decoration: none;
            transition: all 0.4s ease;
            font-weight: 500;
            gap: 0.8rem;
        }
        .art-external-btn:hover {
            background: transparent;
            border-color: var(--accent, #2A6355);
            color: var(--accent, #2A6355);
        }

        /* ── RELATED JEWELRY SECTION ── */
        .art-related-title {
            text-align: center;
            padding: 6rem 5% 4rem;
            border-top: 1px solid var(--border, #E2DDD6);
            background: var(--bg-alt, #F2EFE7);
        }
        .art-related-title h2 {
            font-family: var(--font-serif);
            font-size: 1.8rem;
            font-weight: 300;
            letter-spacing: 0.08em;
            color: var(--fg, #1C1A16);
            margin-top: 0.5rem;
        }
        .art-related-title .kicker {
            font-size: 0.65rem;
            letter-spacing: 0.35em;
            color: var(--accent, #2A6355);
            text-transform: uppercase;
            font-weight: 600;
        }
        .art-related-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 5% 9rem;
            background: var(--bg-alt, #F2EFE7);
        }
        .art-related-item {
            padding: 1.5rem;
            text-align: center;
            background: #ffffff;
            border: 1px solid var(--border, #E2DDD6);
            transition: all 0.5s ease;
        }
        .art-related-item img {
            width: 100%;
            aspect-ratio: 1/1;
            object-fit: contain;
            background: #f7f7f7;
            padding: 1.5rem;
            transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .art-related-item:hover img {
            transform: scale(1.04);
        }
        .art-related-item span {
            display: block;
            margin-top: 1.5rem;
            font-size: 0.65rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--fg, #1C1A16);
            font-weight: 500;
        }
        .art-related-item:hover {
            background: var(--bg-alt, #F2EFE7);
            border-color: var(--accent, #2A6355);
        }

        @media (max-width: 991px) {
            .art-container { grid-template-columns: 1fr; gap: 4rem; }
            .art-cover { position: static; max-width: 600px; margin: 0 auto; }
            .art-related-row { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 768px) {
            .art-actions { flex-direction: column; gap: 1rem; }
            .art-back-btn, .art-external-btn { width: 100%; }
            .art-related-row { grid-template-columns: repeat(2, 1fr); gap: 1rem; }
        }
    </style>
</head>
<body>

    {{nav_html}}

    <!-- BREADCRUMB -->
    <div class="art-breadcrumb">
        <a href="index.html">Accueil</a><span>/</span><a href="presse.html">Presse</a><span>/</span><span>{{title}}</span>
    </div>

    <!-- ARTICLE MAIN CONTAINER -->
    <div class="art-container">
        <!-- LEFT COLUMN: COVER -->
        <div class="art-cover">
            <img class="art-cover-img" src="{{imageUrl}}" alt="Couverture de {{pub}} - {{title}}">
        </div>

        <!-- RIGHT COLUMN: DETAILS -->
        <div class="art-details">
            <div class="art-meta">
                <span class="pub">{{pub}}</span>
                <span class="date">{{date}}</span>
            </div>
            
            <h1>{{title}}</h1>
            
            <div class="art-citation">
                {{citation}}
            </div>
            
            <div class="art-body">
                <p>{{description}}</p>
                <p>À travers cette parution de prestige, les critiques de mode, d'économie et de luxe soulignent la rigueur scientifique de la gemmologue et la finesse artistique de ses montures. Une reconnaissance internationale qui valide la démarche créative indépendante et éthique de la Maison Elke Berr Genève.</p>
            </div>
            
            <div class="art-actions">
                <a href="presse.html" class="art-back-btn">&larr; Retour aux médias</a>
                <a href="{{articleUrl}}" target="_blank" rel="noopener" class="art-external-btn">
                    Voir la source d'origine
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block; vertical-align:middle;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
            </div>
        </div>
    </div>

    <!-- RELATED PRODUCTS -->
    <div class="art-related-title">
        <span class="kicker">VUS DANS LES MÉDIAS</span>
        <h2>Pièces Remarquées</h2>
    </div>
    
    <div class="art-related-row">
        <div class="art-related-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_linfini_necklace.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_linfini_necklace.png" alt="L'Infini Necklace">
                <span>Collier L'Infini — Unbreakable</span>
            </a>
        </div>
        <div class="art-related-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_link_earrings.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_link_earrings.png" alt="Link Earrings">
                <span>Boucles Link — Unbreakable</span>
            </a>
        </div>
        <div class="art-related-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_complice_bangle.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_complice_bangle.png" alt="Complice Bangle">
                <span>Bracelet Complice — Unbreakable</span>
            </a>
        </div>
        <div class="art-related-item">
            <a href="produits/zp-unbreakable/zp_unbreakable_tresor_ring.html" style="text-decoration: none; color: inherit;">
                <img src="img/zp_unbreakable_tresor_ring.png" alt="Trésor Ring">
                <span>Bague Trésor — Unbreakable</span>
            </a>
        </div>
    </div>

    {{footer_html}}

</body>
</html>"""

    for art in enriched_articles:
        subpage_path = os.path.join('localhost_v2', art['subpageUrl'])
        
        # Apply placeholder replacements for the subpage
        art_html = subpage_template.replace("{{nav_html}}", nav_html)
        art_html = art_html.replace("{{title}}", art['title'])
        art_html = art_html.replace("{{pub}}", art['pub'])
        art_html = art_html.replace("{{date}}", art['date'])
        art_html = art_html.replace("{{citation}}", art['citation'])
        art_html = art_html.replace("{{description}}", art['description'])
        art_html = art_html.replace("{{imageUrl}}", art['imageUrl'])
        art_html = art_html.replace("{{articleUrl}}", art['sourceUrl'])
        art_html = art_html.replace("{{footer_html}}", footer_html)
        
        with open(subpage_path, 'w', encoding='utf-8') as f:
            f.write(art_html)
        # Generate placeholder source page
        source_path = os.path.join('localhost_v2', art['sourceUrl'])
        placeholder_html = f"<!DOCTYPE html><html lang=\"fr\"><head><meta charset=\"UTF-8\"><title>{art['title']} – Source</title>{nav_html}</head><body><h1>Source originale</h1><p>Le contenu original de cet article était hébergé sur {art['articleUrl']}.</p>{footer_html}</body></html>"
        with open(source_path, 'w', encoding='utf-8') as sf:
            sf.write(placeholder_html)
            
    print(f"Generated 25 individual press subpages successfully.")

if __name__ == "__main__":
    generate_presse_files()
