import os

def main():
    base_dir = "C:/Users/lyies/.gemini/antigravity"
    if not os.path.exists(base_dir):
        print("Base directory does not exist.")
        return
        
    print("Searching for images in antigravity app data...")
    count = 0
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.png') or f.endswith('.webp') or f.endswith('.jpg'):
                path = os.path.join(root, f)
                size_mb = os.path.getsize(path) / (1024*1024)
                print(f"Found: {path} ({size_mb:.2f} MB)")
                count += 1
                if count >= 100:
                    print("Truncating search to 100 images.")
                    return

if __name__ == "__main__":
    main()
