import os

def main():
    media_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/shopify_media"
    if not os.path.exists(media_dir):
        print(f"Folder {media_dir} not found.")
        return
        
    keywords = ["evenement", "event", "cannes", "nice", "cremat", "gem", "monaco", "award", "women", "gala", "presse", "bel", "party", "showcase", "expos"]
    
    files = os.listdir(media_dir)
    print(f"Total files in shopify_media: {len(files)}")
    
    matches = []
    for f in files:
        matched = [kw for kw in keywords if kw in f.lower()]
        if matched:
            matches.append((f, matched))
            
    print(f"Found {len(matches)} matches:")
    for f, kws in matches:
        print(f"  - {f} (KWs: {kws})")

if __name__ == "__main__":
    main()
