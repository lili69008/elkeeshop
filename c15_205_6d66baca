from PIL import Image
import os

def main():
    path = "c:/Users/lyies/Desktop/siteelk/screenshots/01_root_evenements.png"
    if not os.path.exists(path):
        print("Screenshot not found")
        return
        
    img = Image.open(path)
    width, height = img.size
    
    output_dir = "c:/Users/lyies/Desktop/siteelk/scratch/slices"
    os.makedirs(output_dir, exist_ok=True)
    
    slice_height = 1000
    for i in range(15):
        top = i * slice_height
        bottom = min((i + 1) * slice_height, height)
        if top >= height:
            break
            
        slice_img = img.crop((0, top, width, bottom))
        # Resize to width 800 for quick inspection
        w_new = 800
        h_new = int((bottom - top) * (w_new / width))
        slice_resized = slice_img.resize((w_new, h_new), Image.Resampling.LANCZOS)
        
        slice_name = f"slice_{i+1}_{top}_{bottom}.png"
        slice_resized.save(os.path.join(output_dir, slice_name))
        print(f"Saved slice {i+1}: {slice_name} ({w_new}x{h_new})")

if __name__ == "__main__":
    main()
