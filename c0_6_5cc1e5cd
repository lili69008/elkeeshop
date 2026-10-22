import os
import urllib.request
import time

def download_media():
    links_file = 'shopify_links.txt'
    output_dir = 'shopify_media'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    if not os.path.exists(links_file):
        print(f"Error: {links_file} not found.")
        return

    with open(links_file, 'r', encoding='utf-8') as f:
        links = [line.strip() for l in f if (line := l.strip())]

    print(f"Starting download of {len(links)} files...")
    
    success_count = 0
    error_count = 0
    
    for i, link in enumerate(links, 1):
        filename = link.split('/')[-1]
        # Ensure filename is unique if multiple paths have same name (unlikely in CDN but safe)
        filepath = os.path.join(output_dir, filename)
        
        print(f"[{i}/{len(links)}] Downloading {filename}...", end=' ', flush=True)
        
        try:
            # Add a user-agent to avoid being blocked
            req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            print("DONE")
            success_count += 1
        except Exception as e:
            print(f"ERROR: {e}")
            error_count += 1
        
        # Small delay to be polite to the CDN
        time.sleep(0.1)

    print(f"\nDownload complete!")
    print(f"Successfully downloaded: {success_count}")
    print(f"Failed: {error_count}")
    print(f"Files are in: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    download_media()
