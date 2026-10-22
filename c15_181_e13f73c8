import pandas as pd
import os

df = pd.read_csv('localhost_v2/products.csv')

# Let's inspect the column names
print("CSV columns:", list(df.columns))

# Let's filter for one of our Zulay products, for example 'epure-necklace' or 'alma-ring'
handle = 'epure-necklace'
rows = df[df['Handle'] == handle]

print(f"\nAll CSV rows for handle '{handle}' (Count: {len(rows)}):")
for idx, row in rows.iterrows():
    print(f"Row {idx}:")
    print(f"  Title: {row.get('Title')}")
    print(f"  Option1 Name: {row.get('Option1 Name')} | Option1 Value: {row.get('Option1 Value')}")
    print(f"  Option2 Name: {row.get('Option2 Name')} | Option2 Value: {row.get('Option2 Value')}")
    print(f"  Variant SKU: {row.get('Variant SKU')}")
    # Let's see some other columns like price, image src, etc.
    print(f"  Variant Price: {row.get('Variant Price')}")
    print(f"  Image Src: {row.get('Image Src')}")
    print(f"  Variant Image: {row.get('Variant Image')}")
