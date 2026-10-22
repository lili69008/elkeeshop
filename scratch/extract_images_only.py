from PIL import Image
import numpy as np
import os

def main():
    blocks = [
        ("event_1_influential_women.png", 1732, 3244),
        ("event_2_white_art_party.png", 4102, 5614),
        ("event_3_gem_geneve.png", 6422, 7934),
        ("event_4_monaco_film_festival.png", 8742, 10250),
        ("event_5_cannes_festival.png", 11060, 12572)
    ]
    
    path = "c:/Users/lyies/Desktop/siteelk/screenshots/01_root_evenements.png"
    if not os.path.exists(path):
        print("Screenshot not found")
        return
        
    img = Image.open(path)
    width, height = img.size
    
    output_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    os.makedirs(output_dir, exist_ok=True)
    
    for filename, start, end in blocks:
        block_height = end - start
        block_img = img.crop((0, start, width, end))
        
        # Convert to grayscale numpy array
        gray_block = block_img.convert('L')
        arr = np.array(gray_block)
        
        # Look at the percentage of pixels that are NOT white (< 250)
        non_white_ratio = np.mean(arr < 250, axis=1)
        
        # Find the split row where text starts
        # Text has white background, so rows between text paragraphs or text lines will have very low non-white ratio (almost 0).
        # Photographic images have consistently higher non-white ratios.
        # Let's search from the bottom upwards. The first row that has a non-white ratio > 0.3 is likely the bottom of the image.
        split_row = block_height
        for r in range(block_height - 1, -1, -1):
            if non_white_ratio[r] > 0.3:
                split_row = r + 1
                break
                
        print(f"File {filename}: block height {block_height}, detected image split row at {split_row}")
        
        # If the split row is too close to the top, use the full height or crop top 1000px
        if split_row < 400:
            split_row = min(1080, block_height)
            print(f"  Warning: split row too high, falling back to {split_row}")
            
        # Crop column boundaries
        img_arr = arr[:split_row, :]
        col_non_white = np.mean(img_arr < 250, axis=0)
        content_cols = np.where(col_non_white > 0.02)[0]
        
        if len(content_cols) > 0:
            c_start = content_cols[0]
            c_end = content_cols[-1]
            c_start = max(0, c_start - 10)
            c_end = min(width, c_end + 10)
        else:
            c_start = 0
            c_end = width
            
        image_portion = block_img.crop((c_start, 0, c_end, split_row))
        image_portion.save(os.path.join(output_dir, filename))
        print(f"  Saved image portion to {filename} ({image_portion.size[0]}x{image_portion.size[1]})")
        
        # Only save text portion if there is vertical space left
        if split_row < block_height - 10:
            text_portion = block_img.crop((0, split_row, width, block_height))
            text_portion.save(os.path.join(output_dir, "text_" + filename))
            print(f"  Saved text portion to text_{filename}")

if __name__ == "__main__":
    main()
