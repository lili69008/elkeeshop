import os

def list_files(folder):
    if not os.path.exists(folder):
        print(f"Folder {folder} does not exist.")
        return
    files = os.listdir(folder)
    print(f"Files in {folder} (total {len(files)}):")
    for f in sorted(files)[:50]:
        print(f"  {f}")

def main():
    list_files("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify_files")

if __name__ == "__main__":
    main()
