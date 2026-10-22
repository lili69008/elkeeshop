import requests
import re

url = "https://elkeberr.com/fr/collections/bagues"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.34",
    "Referer": "https://elkeberr.com/"
}

try:
    response = requests.get(url, headers=headers)
    content = response.text
    
    # Look for image URLs in the source
    # Pattern: //cdn.shopify.com/s/files/...products/NAME_2048x.jpg
    images = re.findall(r'//cdn\.shopify\.com/s/files/[^"\']+', content)
    
    # Filter for diamond and emerald related keywords
    diamond_imgs = [img for img in images if 'diam' in img.lower() or 'white' in img.lower()]
    emerald_imgs = [img for img in images if 'emer' in img.lower() or 'vert' in img.lower()]
    
    print("Diamond related candidates:")
    for img in set(diamond_imgs):
        print(f"https:{img}")
        
    print("\nEmerald related candidates:")
    for img in set(emerald_imgs):
        print(f"https:{img}")

except Exception as e:
    print(f"Error: {e}")
