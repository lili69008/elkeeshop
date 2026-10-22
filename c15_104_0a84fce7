import os
import json
import urllib.request
import time

def main():
    json_path = "c:/Users/lyies/Desktop/siteelk/scratch/parsed_subpages_data.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        pages_data = json.load(f)
        
    base_output_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    
    updated_pages_data = {}
    
    for slug, data in pages_data.items():
        page_dir = os.path.join(base_output_dir, slug)
        os.makedirs(page_dir, exist_ok=True)
        print(f"\nProcessing slug '{slug}' - directory: {page_dir}")
        
        local_images = []
        # Let's download up to 6 key images for each page
        images_to_download = [img for img in data['images'] if 'Echo_Bangle' not in img and 'WhatsApp_Image_2025-07-03' not in img and '3_044d8ac4' not in img and 'Collierlong_rings' not in img and '1_9ba496c6' not in img and 'BIJOUXZULAYSITE' not in img][:6]
        
        for idx, img_url in enumerate(images_to_download):
            # Extract filename from url
            filename = img_url.split('?')[0].split('/')[-1]
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg')):
                filename = f"image_{idx+1}.jpg"
                
            filepath = os.path.join(page_dir, filename)
            print(f"  Downloading [{idx+1}/{len(images_to_download)}] {filename}...")
            
            try:
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
                print("    -> Success")
                local_images.append(f"img/evenements/{slug}/{filename}")
            except Exception as e:
                print(f"    -> Error: {e}")
                
            time.sleep(0.15)
            
        data['local_images'] = local_images
        updated_pages_data[slug] = data
        
    with open("c:/Users/lyies/Desktop/siteelk/scratch/downloaded_subpages_data.json", "w", encoding="utf-8") as out:
        json.dump(updated_pages_data, out, indent=4, ensure_ascii=False)
        
    print("\nSuccessfully finished downloading subpage images.")

if __name__ == "__main__":
    main()
