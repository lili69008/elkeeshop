import os
import re
import requests
import time

def download_missing_media():
    root_dir = 'localhost_v2'
    media_dir = os.path.join(root_dir, 'shopify_media')
    if not os.path.exists(media_dir):
        os.makedirs(media_dir)
        
    shopify_regex = re.compile(r'https://cdn\.shopify\.com/s/files/[^"\'>\s]+')
    
    all_urls = set()
    for root, dirs, files in os.walk(root_dir):
        if 'shopify_media' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    all_urls.update(shopify_regex.findall(content))
    
    print(f"Found {len(all_urls)} unique Shopify URLs.")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    downloaded = 0
    skipped = 0
    failed = 0
    
    for url in all_urls:
        clean_url = url.split('?')[0]
        filename = os.path.basename(clean_url)
        # Check if already exists (possibly with suffix)
        exists = False
        for f in os.listdir(media_dir):
            if f.startswith(os.path.splitext(filename)[0]):
                exists = True
                break
        
        if exists:
            skipped += 1
            continue
            
        try:
            print(f"Downloading: {filename}...", end='\r')
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                with open(os.path.join(media_dir, filename), 'wb') as f:
                    f.write(response.content)
                downloaded += 1
                time.sleep(0.1) # Small delay to be polite
            else:
                print(f"\nFailed to download {url}: {response.status_code}")
                failed += 1
        except Exception as e:
            print(f"\nError downloading {url}: {e}")
            failed += 1
            
    print(f"\nDownload summary:")
    print(f"- Downloaded: {downloaded}")
    print(f"- Already existed: {skipped}")
    print(f"- Failed: {failed}")

if __name__ == "__main__":
    download_missing_media()
