#!/usr/bin/env python3
"""
Script de synchronisation et de génération du Thème Shopify V2 (Elke Berr Genève).
Synchronise le CSS et le JS depuis localhost_v2/ vers shopify_theme_v2/
et génère l'archive shopify_theme_v2_final.zip prête à être importée dans Shopify.
"""
import shutil
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent
LOCALHOST_DIR = ROOT_DIR / "localhost_v2"
THEME_DIR = ROOT_DIR / "shopify_theme_v2"
OUTPUT_ZIP = ROOT_DIR / "shopify_theme_v2_final.zip"

ALLOWED_ASSET_EXTS = {".css", ".js", ".liquid", ".json", ".svg"}
THEME_SUBDIRS = ["layout", "sections", "templates", "config", "locales", "snippets", "assets"]


def sync_local_to_theme():
    print("1. Synchronisation CSS & JS depuis localhost_v2 vers shopify_theme_v2...")
    src_css = LOCALHOST_DIR / "css" / "style.css"
    dst_css = THEME_DIR / "assets" / "style.css"
    src_js = LOCALHOST_DIR / "js" / "main.js"
    dst_js = THEME_DIR / "assets" / "main.js"

    dst_css.parent.mkdir(parents=True, exist_ok=True)
    if src_css.exists():
        shutil.copy2(src_css, dst_css)
        print(f"   [OK] Copie : {src_css.relative_to(ROOT_DIR)} -> {dst_css.relative_to(ROOT_DIR)}")
    if src_js.exists():
        shutil.copy2(src_js, dst_js)
        print(f"   [OK] Copie : {src_js.relative_to(ROOT_DIR)} -> {dst_js.relative_to(ROOT_DIR)}")


def build_zip():
    print(f"2. Creation de l'archive Shopify : {OUTPUT_ZIP.name}...")
    count = 0
    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for subdir in THEME_SUBDIRS:
            folder = THEME_DIR / subdir
            if not folder.exists():
                continue
            for file_path in sorted(folder.rglob("*")):
                if not file_path.is_file():
                    continue
                if subdir == "assets" and file_path.suffix.lower() not in ALLOWED_ASSET_EXTS:
                    continue
                arcname = file_path.relative_to(THEME_DIR).as_posix()
                zf.write(file_path, arcname)
                count += 1
    size_kb = OUTPUT_ZIP.stat().st_size / 1024
    print(f"   [OK] Archive generee avec succes ({count} fichiers, {size_kb:.1f} Ko) : {OUTPUT_ZIP}")


if __name__ == "__main__":
    sync_local_to_theme()
    build_zip()
    print("\n[PRET] Le theme est pret a etre propulse sur Shopify :")
    print("   - Via Shopify CLI : shopify theme push --path shopify_theme_v2 --store 165n1t-bx.myshopify.com")
    print("   - Ou via Shopify Admin : Boutique en ligne > Themes > Ajouter un theme > Mettre en ligne shopify_theme_v2_final.zip")
