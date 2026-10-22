import os
from PIL import Image

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/scratch"
    for i in range(1, 9):
        filename = f"evenements_chunk_{i}.png"
        path = os.path.join(folder, filename)
        if os.path.exists(path):
            img = Image.open(path)
            print(f"{filename} - Size: {img.size} - Mode: {img.mode} - File Size: {os.path.getsize(path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
