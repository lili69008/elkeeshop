from PIL import Image
import os

def main():
    path = "c:/Users/lyies/Desktop/siteelk/screenshots/01_root_evenements.png"
    if not os.path.exists(path):
        print("File not found")
        return
        
    img = Image.open(path)
    width, height = img.size
    print(f"Dimensions: {width} x {height}")
    
    # Save a small version of the image so we can inspect it if needed
    # (resizing to max 1000px height for quick review, or splitting)
    # Let's save chunks of 2000px height
    chunk_height = 2000
    num_chunks = (height + chunk_height - 1) // chunk_height
    
    print(f"Splitting into {num_chunks} chunks...")
    for i in range(num_chunks):
        top = i * chunk_height
        bottom = min((i + 1) * chunk_height, height)
        chunk = img.crop((0, top, width, bottom))
        
        # Save chunk to scratch
        out_name = f"c:/Users/lyies/Desktop/siteelk/scratch/evenements_chunk_{i+1}.png"
        chunk.save(out_name)
        print(f"Saved {out_name} ({chunk.size[0]}x{chunk.size[1]})")

if __name__ == "__main__":
    main()
