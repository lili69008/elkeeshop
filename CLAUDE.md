# Instructions Automatiques pour Claude (Projet Elke Berr Genève V2)

## Démarrage Rapide en Localhost (Pour Arnaud)
Lorsque l'utilisateur demande de lancer, installer ou afficher le site en local :
1. Assure-toi d'avoir la dernière version : `git pull origin main` (et `git lfs pull` si Git LFS est installé).
2. Démarre un serveur HTTP local servant le dossier `localhost_v2/` sur le port `8080` :
   - macOS / Linux : `python3 -m http.server 8080 --directory localhost_v2`
   - Windows : `python -m http.server 8080 -d localhost_v2`
   - Alternative Node.js : `npx --yes serve localhost_v2 -l 8080`
3. Ouvre automatiquement `http://localhost:8080/index.html` dans le navigateur (`open http://localhost:8080/index.html` sur macOS, `Start-Process "http://localhost:8080/index.html"` sur Windows, ou `xdg-open http://localhost:8080/index.html` sur Linux).

## Architecture du Projet
- **`localhost_v2/`** : Version complète et autonome du site V2 ("Expert Suisse") avec :
  - Pages principales : `index.html`, `maison.html`, `haute-joaillerie.html`, `bijoux.html`, `unbreakable.html`, `unbreakable-paul.html`, `unbreakable-zulay.html`, `private-jeweller.html`, `bespoke.html`, `presse.html` (et 25 sous-pages `presse-*.html`), `evenements.html`.
  - Catalogue complet : 146 fiches produits dans `localhost_v2/produits/`, synchronisées depuis `localhost_v2/products.csv`.
  - Médias HD : `localhost_v2/img/` et `localhost_v2/shopify_media/`.
  - Styles & Scripts : `localhost_v2/css/style.css` et `localhost_v2/js/main.js`.
- **`shopify_theme_v2/`** : Thème Shopify OS 2.0 (sections Liquid, templates JSON, `assets/style.css`, `assets/main.js`).
- **`shopify_theme_v2_final.zip`** : Archive ZIP prête à être importée dans Shopify Admin.
