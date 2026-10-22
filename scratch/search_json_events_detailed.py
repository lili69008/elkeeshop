import json
import os

def main():
    json_path = "c:/Users/lyies/Desktop/siteelk/elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    if not os.path.exists(json_path):
        print("JSON file not found!")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        root_data = json.load(f)

    data = root_data.get("data", {})
    
    # We want to search in all items (pages, articles, collections, etc.)
    # Let's inspect the keys under data
    print("Keys in JSON data:", data.keys())
    
    keywords = ["evenement", "event", "cannes", "nice", "cremat", "gem", "monaco", "award", "women", "gala", "presse", "bel", "party", "showcase", "expos"]
    
    results = []
    
    def search_object(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_path = f"{path}.{k}" if path else k
                if isinstance(v, str):
                    for kw in keywords:
                        if kw in v.lower():
                            results.append((new_path, v))
                            break
                else:
                    search_object(v, new_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                new_path = f"{path}[{i}]"
                if isinstance(item, str):
                    for kw in keywords:
                        if kw in item.lower():
                            results.append((new_path, item))
                            break
                else:
                    search_object(item, new_path)

    search_object(data)
    print(f"Found {len(results)} raw string matches under 'data'.")
    
    # Write matches to a text file for inspection
    out_path = "c:/Users/lyies/Desktop/siteelk/scratch/json_event_matches.txt"
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(f"Matches count: {len(results)}\n\n")
        for path, val in results:
            # truncate value if it's too long
            snippet = val[:200] + "..." if len(val) > 200 else val
            out.write(f"Path: {path}\n")
            out.write(f"Value: {snippet}\n\n")
            
    print(f"Saved matching paths to {out_path}")

if __name__ == "__main__":
    main()
