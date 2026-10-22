import requests
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

IMG_MAP = {
    "https://cdn.shopify.com/s/files/1/0905/4394/8040/collections/banner_insta_Paul.png?v=1748416124": "hero_home.png",
    "https://cdn.shopify.com/s/files/1/0905/4394/8040/files/portrait_elke_berr.jpg?v=1740662253": "portrait_elke.jpg",
    "https://cdn.shopify.com/s/files/1/0905/4394/8040/files/twilightelegancedoubleringblueupdate.png?v=1740662253": "bague_saphir.png",
    "https://cdn.shopify.com/s/files/1/0905/4394/8040/files/yellow_diamond_sketch.jpg?v=1740662253": "atelier.jpg"
}

OUTPUT_DIR = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/"

def download_pro_assets():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for url, filename in IMG_MAP.items():
        try:
            print(f"Downloading {filename}...")
            response = requests.get(url, headers=HEADERS, timeout=30)
            if response.status_code == 200:
                with open(os.path.join(OUTPUT_DIR, filename), 'wb') as f:
                    f.write(response.content)
                print(f"Success: {filename}")
            else:
                print(f"Failed {filename}: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error {filename}: {str(e)}")

if __name__ == "__main__":
    download_pro_assets()
