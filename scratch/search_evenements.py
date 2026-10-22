import os

def main():
    root_dir = "c:/Users/lyies/Desktop/siteelk"
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if "evenements.html" in f.lower() or "evenement" in f.lower():
                path = os.path.join(root, f)
                print(f"Found file: {path} ({os.path.getsize(path)} bytes)")

if __name__ == "__main__":
    main()
