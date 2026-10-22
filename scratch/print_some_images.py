import json

def main():
    path = "c:/Users/lyies/Desktop/siteelk/elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subdata = data.get('data', {})
    images = subdata.get('images', [])
    print(f"Total images: {len(images)}")
    for img in images[:50]:
        print(f"  {img}")

if __name__ == "__main__":
    main()
