"""
Capture haute resolution du site Elke Berr - Version "No-Missing-Images".
Force le scroll integral pour declencher le lazy-loading avant la capture.
"""
import os
import time
from playwright.sync_api import sync_playwright

URL = "https://elke-berr-v2-feedback.netlify.app/"
OUTPUT_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
VIEWPORT_W = 1920
VIEWPORT_H = 1080

def capture_perfect_site():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page = context.new_page()
        
        print(f"Navigation vers {URL}...")
        page.goto(URL, wait_until="networkidle", timeout=60000)

        # --- FORCE LAZY LOADING ---
        # On scrolle petit a petit jusqu'en bas
        total_height = page.evaluate("document.body.scrollHeight")
        current_pos = 0
        scroll_step = 600 # Pixels par saut
        
        print(f"Scroll progressif ({total_height}px) pour charger les images...")
        while current_pos < total_height:
            page.evaluate(f"window.scrollTo(0, {current_pos})")
            time.sleep(0.3) # Petit delai pour le rendu
            current_pos += scroll_step
            # Re-evaluer la hauteur car elle peut changer avec le chargement
            total_height = page.evaluate("document.body.scrollHeight")

        # Scroll final en bas et remontée
        page.evaluate(f"window.scrollTo(0, {total_height})")
        time.sleep(2)
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(1)

        # --- CAPTURE FULL PAGE ---
        full_path = os.path.join(OUTPUT_DIR, "00_FULL_PAGE_PERFECT.png")
        page.screenshot(path=full_path, full_page=True)
        print(f"[OK] Full page parfaite generee -> {full_path}")

        # --- CAPTURE SECTIONS ---
        # On reprend les sections pour etre sur qu'elles sont a jour aussi
        idx = 1
        scroll_y = 0
        while scroll_y < total_height:
            page.evaluate(f"window.scrollTo(0, {scroll_y})")
            time.sleep(0.5)
            out_path = os.path.join(OUTPUT_DIR, f"{idx:02d}_section_{scroll_y}px_perfect.png")
            page.screenshot(path=out_path)
            scroll_y += VIEWPORT_H
            idx += 1

        browser.close()

if __name__ == "__main__":
    capture_perfect_site()
