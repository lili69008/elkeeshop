import os
import time
import socket
import subprocess
import http.server
import socketserver
import threading
from playwright.sync_api import sync_playwright

ROOT_PAGES = [
    "index.html",
    "maison.html",
    "maison-histoire.html",
    "maison-savoir-faire.html",
    "private-jeweller.html",
    "bespoke.html",
    "evenements.html",
    "presse.html",
    "news.html",
    "contact.html",
    "cgv.html",
    "mentions-legales.html",
    "confidentialite.html",
    "livraison-retours.html",
    # Main collection hubs / listing pages
    "haute-joaillerie.html",
    "haute-joaillerie-bagues.html",
    "haute-joaillerie-boucles-doreilles.html",
    "haute-joaillerie-bracelets.html",
    "haute-joaillerie-colliers.html",
    "joaillerie.html",
    "bijoux.html",
    "bagues.html",
    "boucles-doreilles.html",
    "bracelets.html",
    "colliers.html",
    "boutons-de-manchette.html",
    "pendentifs.html",
    "pour-elle.html",
    "pour-lui.html",
    "selections.html",
    # Collection lines
    "unbreakable.html",
    "unbreakable-paul.html",
    "unbreakable-zulay.html",
    "unbreakable-story.html",
    "unbreakable-villa.html",
    "dolce.html",
    "milky-way.html",
    "mysteria.html",
    "rockn-rose.html",
    "singular.html",
    "waves.html",
    "me-you.html",
    "gift-idea-1.html"
]

PRODUCT_PAGES = [
    "produits/african-flame-ring.html",
    "produits/alma-ring.html",
    "produits/bracelet-unbreakable.html",
    "produits/l-anamour-bracelet.html",
    "produits/orbis-lacteus-ring.html"
]

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def run_server(port, directory):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)
            
        def log_message(self, format, *args):
            # Suppress normal request logs to keep output clean
            pass

    handler = Handler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Local server started on port {port}")
        httpd.serve_forever()

def main():
    localhost_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2"
    output_dir = "c:/Users/lyies/Desktop/siteelk/screenshots"
    os.makedirs(output_dir, exist_ok=True)
    
    port = find_free_port()
    
    # Start local server in a daemon thread
    server_thread = threading.Thread(target=run_server, args=(port, localhost_dir), daemon=True)
    server_thread.start()
    
    # Wait for server to boot
    time.sleep(1)
    
    base_url = f"http://localhost:{port}/"
    
    all_pages = [(f"01_root_{p.replace('.html', '')}", p) for p in ROOT_PAGES] + \
                [(f"02_product_{p.split('/')[-1].replace('.html', '')}", p) for p in PRODUCT_PAGES]
                
    print(f"Total pages to capture: {len(all_pages)}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2 # HD Retinas scale
        )
        page = context.new_page()
        
        for name, relative_url in all_pages:
            url = base_url + relative_url
            print(f"[{relative_url}] Navigating...")
            try:
                page.goto(url, wait_until="networkidle", timeout=15000)
                
                # --- PROGRESSIVE SCROLL FOR LAZY LOADED IMAGES ---
                total_height = page.evaluate("document.body.scrollHeight")
                current_pos = 0
                scroll_step = 600
                
                while current_pos < total_height:
                    page.evaluate(f"window.scrollTo(0, {current_pos})")
                    time.sleep(0.15)
                    current_pos += scroll_step
                    total_height = page.evaluate("document.body.scrollHeight")
                
                # Scroll back to top
                page.evaluate("window.scrollTo(0, 0)")
                time.sleep(0.5)
                
                # Take full page screenshot
                filename = f"{name}.png"
                output_path = os.path.join(output_dir, filename)
                page.screenshot(path=output_path, full_page=True)
                print(f"  Saved full page to {output_path}")
            except Exception as e:
                print(f"  Error capturing {relative_url}: {e}")
                
        browser.close()

if __name__ == "__main__":
    main()
