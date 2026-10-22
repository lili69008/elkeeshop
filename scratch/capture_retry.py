import os
import time
import socket
import http.server
import socketserver
import threading
from playwright.sync_api import sync_playwright

RETRY_PAGES = [
    ("01_root_unbreakable-story", "unbreakable-story.html"),
    ("01_root_unbreakable-villa", "unbreakable-villa.html")
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
            pass

    handler = Handler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

def main():
    localhost_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2"
    output_dir = "c:/Users/lyies/Desktop/siteelk/screenshots"
    os.makedirs(output_dir, exist_ok=True)
    
    port = find_free_port()
    server_thread = threading.Thread(target=run_server, args=(port, localhost_dir), daemon=True)
    server_thread.start()
    time.sleep(1)
    
    base_url = f"http://localhost:{port}/"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=2
        )
        page = context.new_page()
        
        for name, relative_url in RETRY_PAGES:
            url = base_url + relative_url
            print(f"[{relative_url}] Retrying capture...")
            try:
                # Use domcontentloaded to not wait for infinite stream/videos
                page.goto(url, wait_until="domcontentloaded", timeout=20000)
                
                # Give assets and layout 3 seconds to load/stabilize
                time.sleep(3)
                
                # Progressive scroll
                total_height = page.evaluate("document.body.scrollHeight")
                current_pos = 0
                scroll_step = 600
                
                while current_pos < total_height:
                    page.evaluate(f"window.scrollTo(0, {current_pos})")
                    time.sleep(0.15)
                    current_pos += scroll_step
                    total_height = page.evaluate("document.body.scrollHeight")
                
                page.evaluate("window.scrollTo(0, 0)")
                time.sleep(0.5)
                
                output_path = os.path.join(output_dir, f"{name}.png")
                page.screenshot(path=output_path, full_page=True)
                print(f"  Saved: {output_path}")
            except Exception as e:
                print(f"  Failed: {e}")
                
        browser.close()

if __name__ == "__main__":
    main()
