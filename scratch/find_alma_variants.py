import pandas as pd

df = pd.read_csv('localhost_v2/products.csv')

handle = 'tresor-ring'
rows = df[df['Handle'] == handle]

print(f"Product Handle: {handle}")
print(f"Number of rows: {len(rows)}")

# Print unique values for Option1, Option2, Option3, and check columns
for col in ['Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value', 'Variant Price', 'Variant Image', 'Image Src']:
    if col in df.columns:
        print(f"Unique {col}: {rows[col].unique()}")

print("\nDetail of rows for tresor-ring:")
for idx, row in rows.iterrows():
    print(f"Row {idx}:")
    print(f"  Opt1 Value: {row.get('Option1 Value')} | Opt2 Value: {row.get('Option2 Value')} | Price: {row.get('Variant Price')}")
    print(f"  Image Src: {row.get('Image Src')} | Variant Image: {row.get('Variant Image')}")
