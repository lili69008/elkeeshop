import os

def main():
    path = "c:/Users/lyies/Desktop/siteelk/site_files_inventory.txt"
    if not os.path.exists(path):
        print("File does not exist.")
        return
        
    keywords = ["evenement", "event", "cannes", "monaco", "nice", "geneve", "paris"]
    
    with open(path, 'r', encoding='utf-16') as f:
        lines = f.readlines()
        
    print(f"Total lines: {len(lines)}")
    matches = []
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(kw in line_lower for kw in keywords):
            matches.append((i+1, line.strip()))
            
    print(f"Total matches: {len(matches)}")
    for num, text in matches[:100]:
        print(f"Line {num}: {text}")

if __name__ == "__main__":
    main()
