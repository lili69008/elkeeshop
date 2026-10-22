import os
from PIL import Image

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
        
    files = os.listdir(folder)
    print(f"Total files in {folder}: {len(files)}")
    for f in sorted(files):
        if f.endswith('.png'):
            path = os.path.join(folder, f)
            img = Image.open(path)
            print(f"  {f} - Size: {img.size} - Mode: {img.mode}")

if __name__ == "__main__":
    main()
