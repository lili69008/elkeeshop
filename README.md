# 💎 Elke Berr Genève — Plateforme E-Commerce & Vitrine V2 ("Expert Suisse")

Bienvenue **Arnaud** ! Ce dépôt contient l'intégralité de l'écosystème **Elke Berr Genève V2** :
1. **Le site complet en local (`localhost_v2/`)** : Toutes les pages (Accueil, Maison, Haute Joaillerie, Joaillerie, Collection *Unbreakable* Paul & Zulay Pogba, Private Jeweller, 25 pages Presse, Événements et les **146 fiches produits** avec toutes les photos et vidéos HD).
2. **Le Thème Shopify OS 2.0 (`shopify_theme_v2/`)** : La conversion en sections et templates Liquid prêts à être propulsés sur Shopify (`165n1t-bx.myshopify.com`).
3. **Le compilateur automatique (`build_shopify_theme.py`)** : Synchronise tes modifications locales vers le thème Shopify et génère l'archive prête à déployer (`shopify_theme_v2_final.zip`).

---

## 🤖 1. Commandes Automatiques pour ton Claude (Claude Code / Assistant IA)

### ▶️ A. Pour installer et ouvrir tout le site en Localhost automatiquement
Copie-colle ce prompt dans **Claude Code** :

```text
Clone le dépôt privé https://github.com/lili69008/elkeeshop.git (ou mets-le à jour si tu es déjà dedans avec git pull et git lfs pull), puis lance immédiatement le serveur web local depuis le dossier localhost_v2 sur le port 8080 et ouvre automatiquement http://localhost:8080/index.html dans mon navigateur par défaut. Vérifie que le serveur répond bien en HTTP 200.
```

### 🎨 B. Pour modifier le site à ta guise puis le propulser sur Shopify & GitHub
Quand tu veux faire des changements avec Claude et les envoyer sur Shopify, copie-colle ce prompt dans **Claude Code** :

```text
Applique mes modifications à la fois sur le site local (localhost_v2/) et sur les sections correspondantes du thème Shopify (shopify_theme_v2/sections/). Ensuite :
1. Exécute `python build_shopify_theme.py` (ou `python3 build_shopify_theme.py`) pour synchroniser le CSS/JS et générer `shopify_theme_v2_final.zip`.
2. Sauvegarde et pousse les modifications sur GitHub (`git add . && git commit -m "update: modifications Arnaud" && git push origin main`).
3. Propulse le thème sur la boutique Shopify avec `npx @shopify/cli@latest theme push --path shopify_theme_v2 --store 165n1t-bx.myshopify.com --unpublished` (ou indique-moi que `shopify_theme_v2_final.zip` est prêt à être glissé dans Shopify Admin).
```

---

## ⚡ 2. Installation & Lancement en 1 Seule Commande (Sans passer par Claude)

### 🍎 Sur Mac / Linux (Terminal)
```bash
git clone https://github.com/lili69008/elkeeshop.git && cd elkeeshop && (git lfs pull || true) && (open http://localhost:8080/index.html || xdg-open http://localhost:8080/index.html) && python3 -m http.server 8080 --directory localhost_v2
```

### 🪟 Sur Windows (PowerShell)
```powershell
git clone https://github.com/lili69008/elkeeshop.git; cd elkeeshop; git lfs pull; Start-Process "http://localhost:8080/index.html"; python -m http.server 8080 -d localhost_v2
```

---

## ✏️ 3. Modifier le Site à ta Guise sur ta Machine

Tu peux modifier librement n'importe quel aspect du site en local et voir le résultat en direct sur **`http://localhost:8080`** (il suffit de rafraîchir ton navigateur) :

- **Design, Couleurs, Typographies & Mise en page :**
  - Fichier : `localhost_v2/css/style.css`
- **Animations, Menu & Interactions :**
  - Fichier : `localhost_v2/js/main.js`
- **Textes, Visuels & Structure des Pages :**
  - Accueil : `localhost_v2/index.html` (et `shopify_theme_v2/sections/` pour la version Liquid)
  - La Maison : `localhost_v2/maison.html` (`shopify_theme_v2/sections/maison.liquid`)
  - Haute Joaillerie : `localhost_v2/haute-joaillerie.html` (`shopify_theme_v2/sections/haute-joaillerie.liquid`)
  - Unbreakable (Paul & Zulay) : `localhost_v2/unbreakable.html`, `unbreakable-paul.html`, `unbreakable-zulay.html` (`shopify_theme_v2/sections/unbreakable-*.liquid`)
  - Private Jeweller : `localhost_v2/private-jeweller.html` (`shopify_theme_v2/sections/private-jeweller.liquid`)
- **Catalogue Produits (146 pièces) :**
  - Données sources : `localhost_v2/products.csv`
  - Fiches HTML : `localhost_v2/produits/` (régénérables via `python localhost_v2/sync_products_v4.py`)

---

## 🚀 4. Propulser le Site Modifié sur Shopify

Dès que tes modifications te conviennent en local, tu as **2 méthodes** pour les propulser sur Shopify :

### Étape préalable (commune) : Compiler & Synchroniser le Thème
Lance cette commande à la racine du projet :
```bash
python build_shopify_theme.py
```
*(Sur Mac/Linux : `python3 build_shopify_theme.py`)*
👉 Ce script copie automatiquement ton `style.css` et ton `main.js` de `localhost_v2/` vers `shopify_theme_v2/assets/` et génère le fichier **`shopify_theme_v2_final.zip`** (44 Ko) contenant les 36 fichiers du thème OS 2.0.

### Méthode A — Propulsion Directe en Ligne de Commande (Shopify CLI)
1. Prévisualiser en direct sur Shopify (Hot-Reload) :
   ```bash
   npx @shopify/cli@latest theme dev --path shopify_theme_v2 --store 165n1t-bx.myshopify.com
   ```
2. Envoyer en tant que nouveau thème dans la bibliothèque Shopify (sans écraser le thème en ligne) :
   ```bash
   npx @shopify/cli@latest theme push --path shopify_theme_v2 --store 165n1t-bx.myshopify.com --unpublished
   ```
3. Publier directement en production :
   ```bash
   npx @shopify/cli@latest theme push --path shopify_theme_v2 --store 165n1t-bx.myshopify.com --live
   ```

### Méthode B — Import en 1 Clic dans l'Interface Shopify Admin (Sans CLI)
1. Ouvre l'administration Shopify : **`https://admin.shopify.com/store/165n1t-bx/themes`**
2. Clique sur **Ajouter un thème** (`Add theme`) ➡️ **Mettre en ligne un fichier zip** (`Upload zip file`).
3. Glisse le fichier **`shopify_theme_v2_final.zip`** qui vient d'être généré à la racine du dossier.
4. Clique sur **Personnaliser** ou **Publier** !

---

## 🗺️ Pages Principales à Prévisualiser en Localhost (`http://localhost:8080`)

| Univers | URL Locale |
| :--- | :--- |
| **Accueil V2** | [http://localhost:8080/index.html](http://localhost:8080/index.html) |
| **La Maison (Histoire & Savoir-Faire)** | [http://localhost:8080/maison.html](http://localhost:8080/maison.html) |
| **Haute Joaillerie** | [http://localhost:8080/haute-joaillerie.html](http://localhost:8080/haute-joaillerie.html) |
| **Joaillerie & Collections** | [http://localhost:8080/bijoux.html](http://localhost:8080/bijoux.html) / [http://localhost:8080/collections-eb.html](http://localhost:8080/collections-eb.html) |
| **Collection Unbreakable (Paul & Zulay Pogba)** | [http://localhost:8080/unbreakable.html](http://localhost:8080/unbreakable.html) |
| **Unbreakable — Univers Paul** | [http://localhost:8080/unbreakable-paul.html](http://localhost:8080/unbreakable-paul.html) |
| **Unbreakable — Univers Zulay** | [http://localhost:8080/unbreakable-zulay.html](http://localhost:8080/unbreakable-zulay.html) |
| **Private Jeweller & Sur-Mesure** | [http://localhost:8080/private-jeweller.html](http://localhost:8080/private-jeweller.html) / [http://localhost:8080/bespoke.html](http://localhost:8080/bespoke.html) |
| **Presse (25 parutions dédiées)** | [http://localhost:8080/presse.html](http://localhost:8080/presse.html) |
| **Événements (Cannes, GemGenève, Monaco...)** | [http://localhost:8080/evenements.html](http://localhost:8080/evenements.html) |
