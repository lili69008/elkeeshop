import pandas as pd
import os

df = pd.read_csv('localhost_v2/products.csv')
print("Unique product titles in CSV:")
for idx, row in df.drop_duplicates(subset=['Handle']).iterrows():
    handle = str(row['Handle'])
    title = str(row['Title'])
    p_type = str(row['Type'])
    
    # Check if this handle matches any of our known Zulay products or other candidates
    keywords = ['epure', 'linfini', 'alma', 'tresor', 'eclat', 'bond', 'link', 'complice', 'echo', 'essentiel']
    matched = False
    for kw in keywords:
        if kw in handle.lower() or kw in title.lower():
            matched = True
            break
            
    if matched:
        print(f"MATCH: Handle: {handle} | Title: {title} | Type: {p_type}")
