import re
import os

def search_file(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found.")
        return
        
    print(f"\n--- Searching in {os.path.basename(filepath)} ---")
    
    # We want to search for keywords related to the events:
    # Influential Women, White Art Party, Gem Genève, Monaco Film Festival, Cannes
    keywords = [
        r"influential\s+women", r"white\s+art", r"crémat", r"cremat", 
        r"gem\s*genève", r"gem\s*geneve", r"monaco\s+film", r"cannes", 
        r"frédérique\s+bel", r"frederique\s+bel", r"evenement", r"événement"
    ]
    
    # Compile regexes
    patterns = [re.compile(pattern, re.IGNORECASE) for pattern in keywords]
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Let's find context around matches (e.g. 200 chars before and after)
    for pattern in patterns:
        matches = list(pattern.finditer(content))
        print(f"Pattern '{pattern.pattern}': {len(matches)} matches")
        for i, match in enumerate(matches[:5]):
            start = max(0, match.start() - 150)
            end = min(len(content), match.end() + 150)
            snippet = content[start:end].replace('\n', ' ').strip()
            print(f"  Match {i+1}: ... {snippet} ...")

def main():
    search_file("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify.html")
    search_file("c:/Users/lyies/Desktop/siteelk/Elke Berr · Files · Shopify 2.html")

if __name__ == "__main__":
    main()
