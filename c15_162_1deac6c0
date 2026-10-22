import os

def main():
    root_dir = "c:/Users/lyies/Desktop/siteelk/localhost_v2"
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
    
    images = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if f.lower().endswith(image_extensions):
                rel_path = os.path.relpath(os.path.join(root, f), root_dir)
                images.append(rel_path)
                
    print(f"Total image files found: {len(images)}")
    
    # We replace \ with / for matching
    filtered = []
    for img in sorted(images):
        normalized = img.replace('\\', '/')
        if 'evenement' in normalized.lower() or 'event' in normalized.lower() or 'presse' in normalized.lower() or 'press' in normalized.lower() or 'news' in normalized.lower() or 'cannes' in normalized.lower() or 'monaco' in normalized.lower() or 'nice' in normalized.lower() or 'geneve' in normalized.lower() or 'paris' in normalized.lower():
            filtered.append(normalized)
            
    print(f"Filtered images matching keywords ({len(filtered)}):")
    for f in filtered[:100]:
        print(f)

if __name__ == "__main__":
    main()
