import json

def main():
    path = "c:/Users/lyies/Desktop/siteelk/elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subdata = data.get('data', {})
    meta = subdata.get('metadata', {})
    print("Metadata keys:", list(meta.keys()))
    for k in ['title', 'url', 'description', 'ogTitle', 'ogUrl', 'canonical']:
        print(f"  {k}: {meta.get(k)}")
        
    print("\nSummary:", subdata.get('summary'))

if __name__ == "__main__":
    main()
