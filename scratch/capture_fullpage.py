"""
Capture haute résolution du site Elke Berr — section par section.
Viewport 1920px, full scroll, découpage précis.
"""
import os
import time
from playwright.sync_api import sync_playwright

URL = "https://elke-berr-v2-feedback.netlify.app/"
OUTPUT_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/screenshots_hd"
VIEWPORT_W = 1920
VIEWPORT_H = 1080

def capture_site():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(URL, wait_until="networkidle", timeout=60000)

        # Wait for animations / lazy-loaded content
        time.sleep(5)

        # --------------------------------------------------
        # 1) Full-page screenshot (everything in one shot)
        # --------------------------------------------------
        full_path = os.path.join(OUTPUT_DIR, "00_FULL_PAGE.png")
        page.screenshot(path=full_path, full_page=True)
        print(f"[OK] Full page -> {full_path}")

        # --------------------------------------------------
        # 2) Section-by-section viewport captures
        #    Scroll down the page in viewport-height steps
        #    to capture every pixel without overlap gaps.
        # --------------------------------------------------
        total_height = page.evaluate("document.body.scrollHeight")
        print(f"Page height: {total_height}px")

        step = VIEWPORT_H  # 1080px per capture
        idx = 1
        scroll_y = 0

        while scroll_y < total_height:
            page.evaluate(f"window.scrollTo(0, {scroll_y})")
            time.sleep(0.8)  # let animations settle

            out_path = os.path.join(OUTPUT_DIR, f"{idx:02d}_section_{scroll_y}px.png")
            page.screenshot(path=out_path)
            print(f"[OK] Section {idx} (y={scroll_y}px) -> {out_path}")

            scroll_y += step
            idx += 1

        # Final capture at the very bottom (to avoid missing the footer)
        page.evaluate(f"window.scrollTo(0, {total_height})")
        time.sleep(0.8)
        out_path = os.path.join(OUTPUT_DIR, f"{idx:02d}_section_bottom.png")
        page.screenshot(path=out_path)
        print(f"[OK] Section {idx} (bottom) -> {out_path}")

        browser.close()

    print(f"\n✅ {idx} captures sauvées dans {OUTPUT_DIR}")

if __name__ == "__main__":
    capture_site()
