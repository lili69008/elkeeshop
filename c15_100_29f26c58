import os
import json
import urllib.request
import time

def main():
    json_path = "c:/Users/lyies/Desktop/siteelk/scratch/parsed_events.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        events = json.load(f)
        
    output_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Target directory: {output_dir}")
    
    # Custom filenames map to keep them clean and short
    filenames_map = {
        "unbreakable-launch": "unbreakable-launch.jpg",
        "cannes-film-festival": "cannes-film-festival.jpg",
        "paris-blockchain-week-2025": "paris-blockchain-week.jpg",
        "opera-for-peace-2025": "opera-for-peace.jpg",
        "most-influential-women-of-the-world": "most-influential-women.jpg",
        "chateau-de-creema-2023": "chateau-de-cremat.jpg",
        "gem-geneve-2023": "gem-geneve.jpg",
        "monaco-film-2022": "monaco-film-festival.jpg",
        "better-world-fund-2022": "better-world-fund.jpg",
        "cannes-festival-2021": "cannes-festival-2021.jpg",
        "cannes-festival-2019": "cannes-festival-2019.jpg",
        "vacheron-constantin-workshop-2016": "vacheron-constantin.jpg"
    }
    
    downloaded_data = []
    
    for item in events:
        link = item['link']
        # Extract slug from /fr/pages/slug
        slug = link.split('/')[-1]
        img_url = item['image_url']
        
        filename = filenames_map.get(slug, f"{slug}.jpg")
        filepath = os.path.join(output_dir, filename)
        
        print(f"Downloading image for '{slug}' from: {img_url}")
        print(f"Saving to: {filepath}")
        
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print("  -> Success!")
            
            # Save local path
            item['local_image_path'] = f"img/evenements/{filename}"
            item['slug'] = slug
            downloaded_data.append(item)
        except Exception as e:
            print(f"  -> Error: {e}")
            item['local_image_path'] = "img/news.png"  # fallback
            item['slug'] = slug
            downloaded_data.append(item)
            
        time.sleep(0.2)
        
    # Write updated events JSON
    with open("c:/Users/lyies/Desktop/siteelk/scratch/downloaded_events.json", "w", encoding="utf-8") as out:
        json.dump(downloaded_data, out, indent=4, ensure_ascii=False)
        
    print("Done downloading all event images.")

if __name__ == "__main__":
    main()
