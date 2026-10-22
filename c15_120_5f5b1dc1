import os
import re

def main():
    root_dir = r"C:\Users\lyies\.gemini\antigravity\brain\652bc02e-3f32-4751-88c9-8efa401d3edb"
    targets = [
        "730d1d78216147488df634f195d85203",
        "a9751d282c13426e9a8ff60a4fc70274",
        "106fcdf4e1fd4c2fb54807207e16658f",
        "42f4f9dfa08f4137acafe4d6346d11f8"
    ]
    
    print("Searching...")
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if name.endswith(('.txt', '.json', '.html', '.md')):
                path = os.path.join(root, name)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    for t in targets:
                        if t in content:
                            print(f"- Found {t} in {name}")
                            # find surrounding lines
                            lines = content.splitlines()
                            for i, l in enumerate(lines):
                                if t in l:
                                    start = max(0, i - 2)
                                    end = min(len(lines), i + 3)
                                    print(f"  Lines {start}-{end}:")
                                    for idx in range(start, end):
                                        print(f"    {idx}: {lines[idx][:150]}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    main()
