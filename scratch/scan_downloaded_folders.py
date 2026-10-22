import os

def scan_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return []
    
    print(f"Scanning {folder_path}...")
    files_found = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            files_found.append(os.path.join(root, f))
    return files_found

def main():
    folders = [
        "Elke Berr · Files · Shopify_files",
        "Elke Berr · Files · Shopify 2_files",
        "Elke Berr · Analytics · Shopify_files",
        "assets_v1",
        "wireframes_pack",
        "screenshots"
    ]
    
    keywords = ["evenement", "event", "cannes", "nice", "cremat", "gem", "monaco", "award", "women", "gala", "presse", "bel", "party", "showcase", "expos"]
    
    all_matches = []
    for folder in folders:
        files = scan_folder(folder)
        print(f"  Total files: {len(files)}")
        for path in files:
            filename = os.path.basename(path)
            matched_kws = [kw for kw in keywords if kw in filename.lower()]
            if matched_kws:
                all_matches.append((path, matched_kws))
                
    print(f"\nFound {len(all_matches)} total event matches:")
    for path, kws in all_matches[:40]:
        print(f"  - {path} (KWs: {kws})")

if __name__ == "__main__":
    main()
