import os

def main():
    proj_dir = r"c:\Users\lyies\Desktop\siteelk\localhost_v2"
    target = "5dcc0929850b4fbea015c0e5b29ea8a4"
    print("Searching for HTML references...")
    for root, dirs, files in os.walk(proj_dir):
        for name in files:
            if name.endswith('.html'):
                path = os.path.join(root, name)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        if target in f.read():
                            print("-", name)
                except Exception as e:
                    pass

if __name__ == "__main__":
    main()
