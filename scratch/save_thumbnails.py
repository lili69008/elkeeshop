from PIL import Image
import os

def main():
    output_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2/img/evenements"
    files = [
        "event_1_influential_women.png",
        "event_2_white_art_party.png",
        "event_3_gem_geneve.png",
        "event_4_monaco_film_festival.png",
        "event_5_cannes_festival.png"
    ]
    
    for f in files:
        path = os.path.join(output_dir, f)
        if not os.path.exists(path):
            print(f"File {path} not found")
            continue
            
        img = Image.open(path)
        w, h = img.size
        new_w = 800
        new_h = int(h * (new_w / w))
        
        thumb = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        thumb_name = f"thumb_{f}"
        thumb_path = os.path.join(output_dir, thumb_name)
        thumb.save(thumb_path)
        print(f"Saved thumbnail: {thumb_path} ({new_w}x{new_h})")

if __name__ == "__main__":
    main()
