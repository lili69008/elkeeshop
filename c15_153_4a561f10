import os

def main():
    path = "c:/Users/lyies/Desktop/siteelk/missing_cdn_assets.txt"
    if not os.path.exists(path):
        print("missing_cdn_assets.txt not found")
        return
        
    keywords = ["evenement", "event", "cannes", "nice", "cremat", "gem", "monaco", "award", "women", "gala", "presse", "bel", "party", "showcase", "expos"]
    
    # Try reading as UTF-16
    try:
        with open(path, 'r', encoding='utf-16') as f:
            lines = f.readlines()
        print(f"Read {len(lines)} lines from missing_cdn_assets.txt (UTF-16)")
    except Exception as e:
        print(f"Failed to read as UTF-16: {e}")
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            print(f"Read {len(lines)} lines as UTF-8 (fallback)")
        except Exception as e2:
            print(f"Failed to read as UTF-8: {e2}")
            return
            
    matches = []
    for line in lines:
        matched_kws = [kw for kw in keywords if kw in line.lower()]
        if matched_kws:
            matches.append((line.strip(), matched_kws))
            
    print(f"Found {len(matches)} matches:")
    for line, kws in matches[:40]:
        print(f"  Match: {line} (KWs: {kws})")

if __name__ == "__main__":
    main()
