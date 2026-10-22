import json
import os

def main():
    json_path = "c:/Users/lyies/Desktop/siteelk/elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    if not os.path.exists(json_path):
        print("JSON file not found!")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        root_data = json.load(f)

    data = root_data.get("data", {})
    images = data.get("images", [])
    print(f"Total images in JSON 'images' field: {len(images)}")
    
    # Save first 100 images to a text file to inspect
    output_path = "c:/Users/lyies/Desktop/siteelk/scratch/json_images.txt"
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(f"Total images: {len(images)}\n\n")
        for i, img in enumerate(images):
            out.write(f"Image {i+1}:\n")
            if isinstance(img, dict):
                for k, v in img.items():
                    out.write(f"  {k}: {v}\n")
            else:
                out.write(f"  {img}\n")
            out.write("\n")
            
    print(f"Written image list to {output_path}")

if __name__ == "__main__":
    main()
