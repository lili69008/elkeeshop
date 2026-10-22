import json
import os

json_path = 'elkeberr.com_fr.2026-05-12T21_36_34.385Z.json'
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    dict_data = data.get('data', {})
    for key in ['metadata', 'json', 'summary']:
        val = dict_data.get(key)
        print(f"Key '{key}' type: {type(val)}")
        if isinstance(val, dict):
            print(f"  Keys: {list(val.keys())[:10]}")
        elif isinstance(val, str):
            print(f"  Length/Value: {len(val)} / {val[:200]}")
else:
    print(f"JSON file {json_path} does not exist!")
