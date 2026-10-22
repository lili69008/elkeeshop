import os
import datetime

def main():
    folder = "c:/Users/lyies/Desktop/siteelk/screenshots"
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
        
    files = os.listdir(folder)
    print(f"Total files in screenshots/: {len(files)}")
    for f in sorted(files):
        path = os.path.join(folder, f)
        mtime = os.path.getmtime(path)
        mtime_dt = datetime.datetime.fromtimestamp(mtime)
        size_mb = os.path.getsize(path) / (1024 * 1024)
        print(f"  {f} ({size_mb:.2f} MB) - Modified: {mtime_dt}")

if __name__ == "__main__":
    main()
