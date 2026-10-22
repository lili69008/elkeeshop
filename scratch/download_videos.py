import urllib.request
import os

def download_file(url, dest):
    print(f"Downloading {url} -> {dest} ...")
    try:
        # Using a browser User-Agent to prevent CDN blocks
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        )
        with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            print(f"  Success: {len(data)} bytes")
            return len(data)
    except Exception as e:
        print(f"  Failed: {e}")
        return 0

def main():
    dest_dir = r"c:\Users\lyies\Desktop\siteelk\localhost_v2\img"
    os.makedirs(dest_dir, exist_ok=True)
    
    videos = {
        "video_106f.mp4": "https://elkeberr.com/cdn/shop/videos/c/vp/106fcdf4e1fd4c2fb54807207e16658f/106fcdf4e1fd4c2fb54807207e16658f.HD-1080p-7.2Mbps-47971286.mp4",
        "video_42f4.mp4": "https://elkeberr.com/cdn/shop/videos/c/vp/42f4f9dfa08f4137acafe4d6346d11f8/42f4f9dfa08f4137acafe4d6346d11f8.HD-1080p-7.2Mbps-47972916.mp4",
        "video_730d.mp4": "https://elkeberr.com/cdn/shop/videos/c/vp/730d1d78216147488df634f195d85203/730d1d78216147488df634f195d85203.HD-1080p-7.2Mbps-12341991.mp4",
        "video_a975.mp4": "https://elkeberr.com/cdn/shop/videos/c/vp/a9751d282c13426e9a8ff60a4fc70274/a9751d282c13426e9a8ff60a4fc70274.HD-1080p-7.2Mbps-48369783.mp4"
    }
    
    for name, url in videos.items():
        dest = os.path.join(dest_dir, name)
        download_file(url, dest)

if __name__ == "__main__":
    main()
