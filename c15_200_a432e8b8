import re

def main():
    log_path = r"C:\Users\lyies\.gemini\antigravity\brain\652bc02e-3f32-4751-88c9-8efa401d3edb\.system_generated\logs\overview.txt"
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print("Error reading log:", e)
        return
        
    urls = set(re.findall(r'https?://[^\s\"\'\>]+?\.mp4', content))
    print(f"Found {len(urls)} MP4 URLs in overview.txt:")
    for url in sorted(list(urls)):
        print("-", url)
        
    # Also search for files containing .mp4 or yellow or ring or diamond
    matches = re.findall(r'[^\s\"\'\>]+?\.mp4', content)
    unique_matches = set(matches)
    print(f"\nFound {len(unique_matches)} raw .mp4 references:")
    for m in sorted(list(unique_matches)):
        if "img/" in m or "cdn" in m:
            print("-", m)

if __name__ == "__main__":
    main()
