# Instructions Automatiques pour Claude (Projet Elke Berr Genève V2)

## 1. Démarrage Rapide en Localhost (Pour Arnaud)
Lorsque l'utilisateur demande de lancer, installer ou afficher le site en local :
1. Assure-toi d'avoir la dernière version : `git pull origin main` (et `git lfs pull` si Git LFS est installé).
2. Démarre un serveur HTTP local servant le dossier `localhost_v2/` sur le port `8080` :
   - macOS / Linux : `python3 -m http.server 8080 --directory localhost_v2`
   - Windows : `python -m http.server 8080 -d localhost_v2`
   - Alternative Node.js : `npx --yes serve localhost_v2 -l 8080`
3. Ouvre automatiquement `http://localhost:8080/index.html` dans le navigateur (`open http://localhost:8080/index.html` sur macOS, `Start-Process "http://localhost:8080/index.html"` sur Windows, ou `xdg-open http://localhost:8080/index.html` sur Linux).

## 2. Règle d'Or lors des Modifications (Localhost <-> Shopify)
Chaque fois qu'Arnaud te demande de modifier le design, des textes, des sections ou des scripts :
1. **Applique la modification dans `localhost_v2/`** (`localhost_v2/css/style.css`, `localhost_v2/js/main.js`, et les fichiers `.html` concernés) pour qu'Arnaud voie immédiatement le changement sur `http://localhost:8080`.
2. **Répercute la modification dans `shopify_theme_v2/sections/` ou `shopify_theme_v2/layout/theme.liquid`** si le HTML d'une section a changé.
3. **Exécute systématiquement le script de build Shopify :**
   ```bash
   python build_shopify_theme.py
   ```
   *(ou `python3 build_shopify_theme.py` sur macOS/Linux)*
   Ce script copie automatiquement `localhost_v2/css/style.css` et `localhost_v2/js/main.js` dans `shopify_theme_v2/assets/` et régénère `shopify_theme_v2_final.zip`.

## 3. Propulsion sur Shopify (`165n1t-bx.myshopify.com`) & GitHub
Lorsque l'utilisateur demande de propulser / déployer sur Shopify :
1. Exécute `python build_shopify_theme.py` (ou `python3 build_shopify_theme.py`).
2. Sauvegarde sur GitHub :
   ```bash
   git add .
   git commit -m "update: modifications du site et du thème Shopify V2"
   git push origin main
   ```
3. Déploie sur Shopify via Shopify CLI :
   - Pour prévisualiser en live : `npx @shopify/cli@latest theme dev --path shopify_theme_v2 --store 165n1t-bx.myshopify.com`
   - Pour envoyer le thème dans la bibliothèque Shopify : `npx @shopify/cli@latest theme push --path shopify_theme_v2 --store 165n1t-bx.myshopify.com --unpublished`
   - Pour publier directement en live : `npx @shopify/cli@latest theme push --path shopify_theme_v2 --store 165n1t-bx.myshopify.com --live`
   - Ou indique à l'utilisateur que le fichier `shopify_theme_v2_final.zip` est prêt à être importé dans `https://admin.shopify.com/store/165n1t-bx/themes`.
