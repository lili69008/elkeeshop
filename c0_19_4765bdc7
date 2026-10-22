import re
import os

def extract_videos():
    files_to_check = [
        "Elke Berr · Files · Shopify.html",
        "Elke Berr · Files · Shopify 2.html"
    ]
    
    video_links = set()
    
    # Very aggressive regex to find anything that looks like a video URL on Shopify CDN
    # or just any .mp4 / .mov link
    patterns = [
        r'https://cdn\.shopify\.com/[^\s\"\'\>]+\.(?:mp4|mov|webm|m4v)',
        r'https://cdn\.shopify\.com/videos/c/o/v/[a-f0-9]+',
        r'//cdn\.shopify\.com/[^\s\"\'\>]+\.(?:mp4|mov|webm|m4v)'
    ]
    
    for filename in files_to_check:
        if not os.path.exists(filename):
            print(f"Skipping {filename} (not found)")
            continue
            
        print(f"Analyzing {filename}...")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for m in matches:
                    link = m if m.startswith('http') else 'https:' + m
                    # Clean the link
                    link = link.split('?')[0].split('"')[0].split("'")[0]
                    video_links.add(link)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    # Also look for IDs from thumbnails and try to guess the video URL
    thumbnail_ids = re.findall(r'/preview_images/([a-f0-9]+)\.thumbnail', content)
    for tid in thumbnail_ids:
        # Common Shopify video path patterns
        video_links.add(f"https://cdn.shopify.com/videos/c/o/v/{tid}.mp4")

    sorted_videos = sorted(list(video_links))
    
    with open('shopify_videos.txt', 'w', encoding='utf-8') as f:
        for link in sorted_videos:
            f.write(link + '\n')
    
    print(f"Found {len(sorted_videos)} potential video links. Saved to shopify_videos.txt")

if __name__ == "__main__":
    extract_videos()
