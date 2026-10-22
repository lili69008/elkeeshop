import os
import json
import urllib.request
import time

def download_images():
    json_path = 'scratch/presse_data.json'
    dest_dir = 'localhost_v2/img/presse'
    
    os.makedirs(dest_dir, exist_ok=True)
    
    if not os.path.exists(json_path):
        print(f"Error: Metadata file {json_path} not found.")
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)
        
    print(f"Loaded {len(articles)} articles from metadata.")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    success_count = 0
    for idx, article in enumerate(articles, 1):
        title = article['title']
        img_url = article['imageUrl']
        
        # Determine file extension from URL or fallback to .jpg
        ext = '.jpg'
        if '.png' in img_url.lower():
            ext = '.png'
        elif '.webp' in img_url.lower():
            ext = '.webp'
            
        # Create a clean local filename from the title
        clean_title = title.lower().replace('&', 'and').replace(' ', '_').replace('(', '').replace(')', '').replace('\'', '')
        local_filename = f"{clean_title}{ext}"
        local_path = os.path.join(dest_dir, local_filename)
        
        # Update article object with the local image path for subsequent HTML generation
        article['local_image_path'] = f"img/presse/{local_filename}"
        
        print(f"[{idx}/{len(articles)}] Downloading image for '{title}'...")
        print(f"  Source: {img_url}")
        print(f"  Target: {local_path}")
        
        req = urllib.request.Request(img_url, headers=headers)
        
        # Retry logic up to 3 times
        downloaded = False
        for attempt in range(1, 4):
            try:
                with urllib.request.urlopen(req, timeout=15) as response:
                    with open(local_path, 'wb') as out_file:
                        out_file.write(response.read())
                print(f"  -> Success!")
                downloaded = True
                success_count += 1
                break
            except Exception as e:
                print(f"  -> Attempt {attempt} failed: {e}")
                time.sleep(1)
                
        if not downloaded:
            print(f"  -> Failed to download image for '{title}' after 3 attempts.")
            
    # Save the updated json back to the scratch file
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
    print("Updated scratch/presse_data.json with local_image_path mappings.")
    print(f"Download complete: {success_count}/{len(articles)} images successfully downloaded.")

if __name__ == "__main__":
    download_images()
