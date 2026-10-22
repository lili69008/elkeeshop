from PIL import Image
import os

def main():
    blocks = [
        ("event_1_clean.png", 1732, 3244),
        ("event_2_clean.png", 4102, 5614),
        ("event_3_clean.png", 6422, 7934),
        ("event_4_clean.png", 8742, 10250),
        ("event_5_clean.png", 11060, 12572)
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
        # The block contains the repeated sticky header in the top portion (~300px)
        # Let's crop from y_offset = 300 to the end of the block
        content_start = start + 300
        content_end = end
        
        # Crop full width
        content_img = img.crop((0, content_start, width, content_end))
        
        # Save full res
        content_img.save(os.path.join(output_dir, filename))
        print(f"Saved clean content to {filename} ({content_img.size[0]}x{content_img.size[1]})")
        
        # Let's also save a thumbnail for quick viewing
        w_new = 800
        h_new = int(content_img.size[1] * (w_new / content_img.size[0]))
        thumb = content_img.resize((w_new, h_new), Image.Resampling.LANCZOS)
        thumb.save(os.path.join(output_dir, "thumb_" + filename))
        print(f"  Saved thumbnail for {filename}")

if __name__ == "__main__":
    main()
