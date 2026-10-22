import os

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/screenshots"
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
        
    files = os.listdir(folder)
    print(f"Total files in screenshots/: {len(files)}")
    for f in sorted(files):
        path = os.path.join(folder, f)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        print(f"  {f} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    main()
