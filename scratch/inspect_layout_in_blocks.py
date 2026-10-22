from PIL import Image
import numpy as np
import os

def main():
    blocks = [
        ("event_1", 1732, 3244),
        ("event_2", 4102, 5614),
        ("event_3", 6422, 7934),
        ("event_4", 8742, 10250),
        ("event_5", 11060, 12572)
    ]
    
    path = "c:/Users/lyies/Desktop/siteelk/screenshots/01_root_evenements.png"
    if not os.path.exists(path):
        print("Screenshot not found")
        return
        
    img = Image.open(path)
    width, height = img.size
    
    output_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    os.makedirs(output_dir, exist_ok=True)
    
    for name, start, end in blocks:
        block_height = end - start
        block_img = img.crop((0, start, width, end))
        
        # Save left half and right half
        left_half = block_img.crop((0, 0, width // 2, block_height))
        right_half = block_img.crop((width // 2, 0, width, block_height))
        
        # Analyze which half is the image and which is the text.
        # Images have high detail/variance. Text blocks have lots of white background.
        # Let's convert to grayscale numpy arrays
        left_arr = np.array(left_half.convert('L'))
        right_arr = np.array(right_half.convert('L'))
        
        # Calculate fraction of white/near-white pixels (e.g. > 245)
        left_white_frac = np.mean(left_arr > 245)
        right_white_frac = np.mean(right_arr > 245)
        
        print(f"Block {name}:")
        print(f"  Left half white fraction: {left_white_frac:.4f}")
        print(f"  Right half white fraction: {right_white_frac:.4f}")
        
        # The half with lower white fraction is the image.
        # Let's crop it precisely (removing extra white borders)
        if left_white_frac < right_white_frac:
            print("  -> Image is on the LEFT")
            image_half = left_half
            text_half = right_half
            image_side = "left"
        else:
            print("  -> Image is on the RIGHT")
            image_half = right_half
            text_half = left_half
            image_side = "right"
            
        # Crop borders of the image half
        image_arr = np.array(image_half.convert('L'))
        # Find column boundaries where there's content (not solid white)
        col_non_white = np.mean(image_arr < 250, axis=0)
        content_cols = np.where(col_non_white > 0.02)[0]
        
        # Find row boundaries
        row_non_white = np.mean(image_arr < 250, axis=1)
        content_rows = np.where(row_non_white > 0.02)[0]
        
        if len(content_cols) > 0 and len(content_rows) > 0:
            x_start = content_cols[0]
            x_end = content_cols[-1]
            y_start = content_rows[0]
            y_end = content_rows[-1]
            
            # Crop to content box
            clean_image = image_half.crop((x_start, y_start, x_end, y_end))
            image_name = f"{name}_original.png"
            clean_image.save(os.path.join(output_dir, image_name))
            print(f"  Saved clean image to {image_name} ({clean_image.size[0]}x{clean_image.size[1]})")
        else:
            print("  Error: no content found in image half!")

if __name__ == "__main__":
    main()
