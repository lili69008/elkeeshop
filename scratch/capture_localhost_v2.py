import asyncio
from playwright.async_api import async_playwright
import os

PAGES = [
    ("01_HOME_V2", "index.html"),
    ("02_MAISON_V2", "maison.html"),
    ("03_UNBREAKABLE_STORY_V2", "unbreakable.html"),
    ("04_UNBREAKABLE_PAUL_V2", "unbreakable-paul.html"),
    ("05_UNBREAKABLE_ZULAY_V2", "unbreakable-zulay.html"),
    ("06_UNBREAKABLE_VILLA_V2", "unbreakable-villa.html"),
    ("07_PRIVATE_JEWELLER_V2", "private-jeweller.html"),
    ("08_BAGUES_V2", "bagues.html"),
    ("09_COLLIERS_V2", "colliers.html"),
    ("10_JOAILLERIE_V2", "joaillerie.html"),
    ("11_BESPOKE_V2", "bespoke.html"),
    ("12_NEWS_V2", "news.html"),
    ("13_CONTACT_V2", "contact.html"),
    ("14_MENTIONS_V2", "mentions-legales.html"),
    ("15_CONFIDENTIALITE_V2", "confidentialite.html"),
    ("16_CGV_V2", "cgv.html"),
    ("17_LIVRAISON_V2", "livraison-retours.html")
]

BASE_URL = "file://c:/Users/lyies/Desktop/siteelk/localhost_v2/"
OUTPUT_DIR = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/localhost_captures"

async def capture_all():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            device_scale_factor=2
        )
        page = await context.new_page()
        
        for name, filename in PAGES:
            url = BASE_URL + filename
            print(f"Capturing {url}...")
            try:
                await page.goto(url, wait_until="networkidle")
                # Wait for any lazy loads
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(2) 
                
                output_path = os.path.join(OUTPUT_DIR, f"{name}.png")
                await page.screenshot(path=output_path, full_page=True)
                print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Skipping {filename} due to error: {e}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_all())
