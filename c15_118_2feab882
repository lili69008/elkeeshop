import json

def main():
    path = "c:/Users/lyies/Desktop/siteelk/elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subdata = data.get('data', {})
    images = subdata.get('images', [])
    print(f"Total images: {len(images)}")
    
    keywords = ["evenement", "event", "cannes", "monaco", "nice", "geneve", "women", "party", "gala", "award", "expo", "bel", "press"]
    matches = []
    for img in images:
        img_str = str(img).lower()
        if any(kw in img_str for kw in keywords):
            matches.append(img)
            
    print(f"Found {len(matches)} matching images:")
    for m in matches[:100]:
        print(f"  {m}")

if __name__ == "__main__":
    main()
