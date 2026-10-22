import os
import re

def migrate_media():
    root_dir = 'localhost_v2'
    media_dir = os.path.join(root_dir, 'shopify_media')
    
    # Build a map of filenames in shopify_media
    # We strip the query params and just keep the basename for matching
    available_files = set(os.listdir(media_dir))
    print(f"Available local files: {len(available_files)}")

    # Regex for Shopify CDN URLs
    # Example: https://cdn.shopify.com/s/files/1/0905/4394/8040/files/32.png?v=1747130013
    shopify_regex = re.compile(r'https://cdn\.shopify\.com/s/files/[^"\'>\s]+')

    files_modified = 0
    urls_replaced = 0
    urls_missing = 0

    for root, dirs, files in os.walk(root_dir):
        # Skip the media directory itself
        if 'shopify_media' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                # Calculate relative path to shopify_media
                # If root is 'localhost_v2', relative is 'shopify_media/'
                # If root is 'localhost_v2/produits', relative is '../shopify_media/'
                depth = len(os.path.relpath(root, root_dir).split(os.sep))
                if os.path.relpath(root, root_dir) == '.':
                    rel_prefix = 'shopify_media/'
                else:
                    rel_prefix = '../' * depth + 'shopify_media/'

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = content
                matches = shopify_regex.findall(content)
                
                replaced_in_file = False
                for url in set(matches):
                    # Extract the filename from the URL
                    clean_url = url.split('?')[0]
                    filename = os.path.basename(clean_url)
                    name_parts = os.path.splitext(filename)
                    base_name = name_parts[0]
                    extension = name_parts[1]
                    
                    # Try to find a match in available_files
                    # 1. Exact match
                    # 2. Match with suffix (e.g. base_name + "_800x800" + extension)
                    # 3. Match starting with base_name
                    match = None
                    if filename in available_files:
                        match = filename
                    else:
                        for f in available_files:
                            if f.startswith(base_name) and f.endswith(extension):
                                match = f
                                break
                    
                    if match:
                        local_path = rel_prefix + match
                        new_content = new_content.replace(url, local_path)
                        urls_replaced += 1
                        replaced_in_file = True
                    else:
                        urls_missing += 1
                
                if replaced_in_file:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    files_modified += 1

    print(f"Migration complete:")
    print(f"- Files modified: {files_modified}")
    print(f"- URLs replaced: {urls_replaced}")
    print(f"- URLs missing locally: {urls_missing}")

if __name__ == "__main__":
    migrate_media()
