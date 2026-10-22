import os

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/localhost_v2"
    if not os.path.exists(folder):
        print("Folder does not exist.")
        return
        
    keywords = ["unbreakable", "cannes", "blockchain", "peace", "women", "cremat", "creema", "gem", "monaco", "better-world", "vacheron", "event"]
    files = os.listdir(folder)
    print(f"Total files in {folder}: {len(files)}")
    for f in sorted(files):
        if f.endswith('.html'):
            f_lower = f.lower()
            if any(kw in f_lower for kw in keywords):
                print(f"  {f} ({os.path.getsize(os.path.join(folder, f))} bytes)")

if __name__ == "__main__":
    main()
