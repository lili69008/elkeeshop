import os

def main():
    root = "c:/Users/lyies/Desktop/siteelk"
    files = os.listdir(root)
    print("Files in root:")
    for f in sorted(files):
        path = os.path.join(root, f)
        if os.path.isdir(path):
            print(f"  [DIR]  {f}")
        else:
            print(f"  [FILE] {f} ({os.path.getsize(path)} bytes)")

if __name__ == "__main__":
    main()
