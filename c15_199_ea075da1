import json

def search_text(text, label, out):
    if not text:
        return
    text_lower = text.lower()
    keywords = ["evenement", "event", "cannes", "monaco", "nice", "geneve", "women", "gempages"]
    out.write(f"Searching in {label} (length: {len(text)}):\n")
    for kw in keywords:
        pos = 0
        count = 0
        while True:
            idx = text_lower.find(kw, pos)
            if idx == -1:
                break
            count += 1
            start = max(0, idx - 100)
            end = min(len(text), idx + 200)
            snippet = text[start:end].replace('\n', ' ')
            out.write(f"  Match '{kw}': ... {snippet} ...\n")
            pos = idx + len(kw)
            if count >= 10:  # print up to 10 matches
                out.write(f"  ... and more for '{kw}'\n")
                break

def main():
    path = "c:/Users/lyies/Desktop/siteelk/elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    subdata = data.get('data', {})
    
    with open("c:/Users/lyies/Desktop/siteelk/scratch/json_search_results.txt", "w", encoding="utf-8") as out:
        search_text(subdata.get('markdown', ''), 'markdown', out)
        search_text(subdata.get('summary', ''), 'summary', out)
        
    print("Done. Results written to scratch/json_search_results.txt")

if __name__ == "__main__":
    main()
