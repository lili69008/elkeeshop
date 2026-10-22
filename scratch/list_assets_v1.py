import os

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/assets_v1"
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
        
    # Walk and list files
    for root, dirs, files in os.walk(folder):
        print(f"Directory: {root}")
        for d in dirs:
            print(f"  [Dir] {d}")
        for f in files[:50]:
            path = os.path.join(root, f)
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"  [File] {f} ({size_mb:.2f} MB)")
        if len(files) > 50:
            print(f"  ... and {len(files) - 50} more files")

if __name__ == "__main__":
    main()
