import urllib.request
import os

def download(url, dest):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as r, open(dest, 'wb') as f:
            data = r.read()
            f.write(data)
        print(f"OK  {dest}: {len(data)} bytes")
        return len(data)
    except Exception as e:
        print(f"ERR {dest}: {e}")
        return 0

dest_dir = r"c:\Users\lyies\Desktop\siteelk\localhost_v2\img"

candidates = {
    # Try full-res product images from private jeweller page
    "ring_clean_1.jpg": "https://elkeberr.com/cdn/shop/files/preview_images/106fcdf4e1fd4c2fb54807207e16658f.thumbnail.0000000000.jpg?v=1747830469",
    "ring_clean_2.jpg": "https://elkeberr.com/cdn/shop/files/preview_images/106fcdf4e1fd4c2fb54807207e16658f.thumbnail.0000000001.jpg?v=1747830469",
    # Try the screenshot used in the Unbreakable product page
    "unbreakable_screenshot_1.png": "https://elkeberr.com/cdn/shop/files/Screenshot_2025-05-12_at_15.02.22.png?v=1747834781",
    "unbreakable_screenshot_2.png": "https://elkeberr.com/cdn/shop/files/Screenshot_2025-05-12_at_15.03.03.png?v=1748425236",
    # The thumbnail for 42f4 (the big video linked from unbreakable page)
    "unbreakable_vid_thumb.jpg": "https://elkeberr.com/cdn/shop/files/preview_images/42f4f9dfa08f4137acafe4d6346d11f8.thumbnail.0000000000.jpg?v=1747832232",
}

for name, url in candidates.items():
    download(url, os.path.join(dest_dir, name))
