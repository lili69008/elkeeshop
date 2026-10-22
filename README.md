# 💎 Elke Berr Genève — Plateforme E-Commerce & Vitrine V2 ("Expert Suisse")

Bienvenue **Arnaud** ! Ce dépôt contient l'intégralité de l'écosystème **Elke Berr Genève V2** :
1. **Le site complet en local (`localhost_v2/`)** : Toutes les pages (Accueil, Maison, Haute Joaillerie, Joaillerie, Collection *Unbreakable* Paul & Zulay Pogba, Private Jeweller, 25 pages Presse, Événements et les **146 fiches produits** avec toutes les photos et vidéos HD).
2. **Le Thème Shopify OS 2.0 (`shopify_theme_v2/`)** : La conversion en sections et templates Liquid prêts pour Shopify.
3. **Les livrables & maquettes (`wireframes_pack/`)** : Les documents de conception et de validation.

---

## 🤖 OPTION 1 : Commande Automatique pour ton Claude (Claude Code / Terminal IA)

Copie-colle simplement ce bloc directement dans **Claude Code** (ou ton agent IA dans le terminal) pour qu'il installe, configure et ouvre tout le site automatiquement sur ta machine :

```text
Clone le dépôt privé https://github.com/lili69008/elkeeshop.git (ou mets-le à jour si tu es déjà dedans avec git pull et git lfs pull), puis lance immédiatement le serveur web local depuis le dossier localhost_v2 sur le port 8080 et ouvre automatiquement http://localhost:8080/index.html dans mon navigateur par défaut. Vérifie que le serveur répond bien en HTTP 200.
```

---

## ⚡ OPTION 2 : Installation & Lancement Automatique en 1 Seule Commande (Terminal)

### 🍎 Sur Mac / Linux (Terminal)
Copie-colle cette commande unique dans ton terminal :

```bash
git clone https://github.com/lili69008/elkeeshop.git && cd elkeeshop && (git lfs pull || true) && (open http://localhost:8080/index.html || xdg-open http://localhost:8080/index.html) && python3 -m http.server 8080 --directory localhost_v2
```

### 🪟 Sur Windows (PowerShell)
Copie-colle cette commande unique dans PowerShell :

```powershell
git clone https://github.com/lili69008/elkeeshop.git; cd elkeeshop; git lfs pull; Start-Process "http://localhost:8080/index.html"; python -m http.server 8080 -d localhost_v2
```

---

## 🔄 Relancer le site plus tard (une fois déjà cloné)

Si le dossier `elkeeshop` est déjà sur ta machine, place-toi dedans et lance :

- **Sur Mac / Linux :**
  ```bash
  git pull && (open http://localhost:8080/index.html || true) && python3 -m http.server 8080 --directory localhost_v2
  ```
- **Sur Windows (PowerShell) :**
  ```powershell
  git pull; Start-Process "http://localhost:8080/index.html"; python -m http.server 8080 -d localhost_v2
  ```
- **Alternative avec Node.js (si Python n'est pas installé) :**
  ```bash
  npx --yes serve localhost_v2 -l 8080
  ```

---

## 🗺️ Pages Principales à Prévisualiser en Localhost

Une fois le serveur lancé, tout le site est navigable sur **`http://localhost:8080`** :

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

---

## 📁 Structure du Dépôt

```text
elkeeshop/
├── localhost_v2/               # 🌐 SITE COMPLET LOCAL (HTML/CSS/JS + Médias HD)
│   ├── index.html              # Page d'accueil principale
│   ├── css/style.css           # Feuille de style principale V2 ("Expert Suisse")
│   ├── js/main.js              # Animations, Mega-Menu, filtres et interactions
│   ├── produits/               # 146 fiches produits générées et synchronisées
│   ├── img/                    # Visuels éditoriaux, Haute Joaillerie, Private Jeweller
│   ├── shopify_media/          # Photos & vidéos HD du catalogue et de la collection Unbreakable
│   └── proposition_client.md   # Proposition stratégique de déploiement Shopify
│
├── shopify_theme_v2/           # 🛍️ THÈME SHOPIFY OS 2.0 (Liquid + JSON Templates)
│   ├── layout/theme.liquid
│   ├── sections/               # 19 sections Liquid modulaires
│   ├── templates/              # Templates JSON OS 2.0
│   ├── config/
│   └── assets/                 # style.css & main.js du thème
│
├── shopify_theme_v2_final.zip  # 📦 Archive légère prête à l'import dans Shopify Admin
└── wireframes_pack/            # 📐 Maquettes et PDF de validation (via Git LFS)
```

---

## 🛠️ Instructions Contextuelles pour Claude (si Arnaud utilise Claude Code pour modifier le projet)

Si tu demandes à **Claude** de faire des modifications sur le site :
1. **Pour modifier le site local :** travailler directement dans `localhost_v2/` (`localhost_v2/css/style.css`, `localhost_v2/js/main.js`, et les fichiers `.html`).
2. **Pour synchroniser ou régénérer les fiches produits :** utiliser les scripts Python présents dans `localhost_v2/` (`sync_products_v4.py`, `generate_collections.py`, `generate_hj_collections.py`).
3. **Pour pousser les modifications sur GitHub :**
   ```bash
   git add .
   git commit -m "update: description des modifications"
   git push origin main
   ```
