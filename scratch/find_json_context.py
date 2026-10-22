import json

def main():
    json_path = r"c:\Users\lyies\Desktop\siteelk\elkeberr.com_fr.2026-05-12T21_36_34.385Z.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    html = data['data']['html']
    
    hashes = ["106fcdf4e1fd4c2fb54807207e16658f", "42f4f9dfa08f4137acafe4d6346d11f8"]
    for h in hashes:
        print(f"\n--- Context for hash {h} ---")
        idx = html.find(h)
        while idx != -1:
            start = max(0, idx - 300)
            end = min(len(html), idx + 300)
            print(html[start:end])
            print("====================================")
            idx = html.find(h, idx + 1)

if __name__ == "__main__":
    main()
