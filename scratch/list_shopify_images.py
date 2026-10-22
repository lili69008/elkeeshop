import os

def search_images(folder):
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
        
    exts = ['.png', '.jpg', '.jpeg', '.webp', '.gif']
    matches = []
    
    for root, dirs, files in os.walk(folder):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in exts:
                path = os.path.join(root, f)
                matches.append((f, os.path.getsize(path)))
                
    print(f"Found {len(matches)} images in {folder}:")
    for name, size in sorted(matches, key=lambda x: x[1], reverse=True)[:50]:
        print(f"  {name} ({size/1024:.1f} KB)")

def main():
    search_images("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify_files")
    search_images("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify 2_files")

if __name__ == "__main__":
    main()
