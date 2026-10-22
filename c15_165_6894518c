import os

def search_folder(folder):
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
        
    keywords = ["evenement", "event", "cannes", "monaco", "nice", "geneve", "paris"]
    matches = []
    
    for root, dirs, files in os.walk(folder):
        for f in files:
            f_lower = f.lower()
            if any(kw in f_lower for kw in keywords):
                path = os.path.join(root, f)
                matches.append(path)
                
    print(f"Found {len(matches)} matches in {folder}:")
    for m in matches[:100]:
        print(f"  {m}")

def main():
    search_folder("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify_files")
    search_folder("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify 2_files")

if __name__ == "__main__":
    main()
