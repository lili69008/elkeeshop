import urllib.request
import os

images = {
    "48.png": "https://cdn.shopify.com/s/files/1/0905/4394/8040/files/48.png?v=1751533800",
    "49.png": "https://cdn.shopify.com/s/files/1/0905/4394/8040/files/49.png?v=1751533800"
}

dest_dir = "localhost_v2/img/produits/alma-ring"
os.makedirs(dest_dir, exist_ok=True)

for name, url in images.items():
    dest_path = os.path.join(dest_dir, name)
    if not os.path.exists(dest_path):
        print(f"Downloading {name} from {url}...")
        try:
            # Add a user agent to prevent download blocks
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Successfully saved to {dest_path}")
        except Exception as e:
            print(f"Error downloading {name}: {e}")
    else:
        print(f"{name} already exists.")
