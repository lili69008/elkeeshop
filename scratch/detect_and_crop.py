from PIL import Image
import numpy as np
import os

def main():
    path = "c:/Users/lyies/Desktop/siteelk/screenshots/01_root_evenements.png"
    if not os.path.exists(path):
        print("Screenshot not found")
        return
        
    img = Image.open(path)
    width, height = img.size
    print(f"Loaded screenshot of size {width}x{height}")
    
    # Convert image to grayscale numpy array for faster analysis
    print("Converting to numpy array...")
    gray_img = img.convert('L')
    arr = np.array(gray_img)
    
    # Let's find rows where the variance is not 0 (or close to 0, since the background is white)
    # The background is likely white (255)
    row_means = np.mean(arr, axis=1)
    row_stds = np.std(arr, axis=1)
    
    # Rows with std > 2 are likely not solid background
    is_content_row = row_stds > 3
    
    # Find contiguous blocks of content rows
    blocks = []
    in_block = False
    start_row = 0
    for r in range(height):
        if is_content_row[r] and not in_block:
            in_block = True
            start_row = r
        elif not is_content_row[r] and in_block:
            in_block = False
            # Filter out blocks that are too small (e.g. text lines or headers)
            if r - start_row > 100:
                blocks.append((start_row, r))
                
    if in_block:
        if height - start_row > 100:
            blocks.append((start_row, height))
            
    print(f"Detected {len(blocks)} content blocks:")
    for idx, (s, e) in enumerate(blocks):
        print(f"  Block {idx+1}: {s} to {e} (height: {e-s}px)")
        
    # Crop and save each detected block
    output_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    os.makedirs(output_dir, exist_ok=True)
    
    for idx, (s, e) in enumerate(blocks):
        # We can crop the full width first to inspect
        block_img = img.crop((0, s, width, e))
        block_img.save(os.path.join(output_dir, f"detected_block_{idx+1}.png"))
        
        # Let's also try to crop the horizontal region that contains the image
        # Images are usually centered or take up a specific column width
        # Let's analyze the column standard deviations for this block
        block_arr = arr[s:e, :]
        col_stds = np.std(block_arr, axis=0)
        is_content_col = col_stds > 3
        
        # Find the horizontal boundaries of the content
        content_cols = np.where(is_content_col)[0]
        if len(content_cols) > 0:
            c_start = content_cols[0]
            c_end = content_cols[-1]
            # Add some padding
            c_start = max(0, c_start - 10)
            c_end = min(width, c_end + 10)
            
            cropped_content = img.crop((c_start, s, c_end, e))
            cropped_content.save(os.path.join(output_dir, f"cropped_block_{idx+1}_content.png"))
            print(f"    Saved cropped content {c_start} to {c_end}")

if __name__ == "__main__":
    main()
