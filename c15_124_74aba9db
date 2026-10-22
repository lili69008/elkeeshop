import pandas as pd

df = pd.read_csv('localhost_v2/products.csv')

handles = [
    'epure-necklace', 'linfini-necklace', 'alma-ring', 'tresor-ring', 
    'eclat-earrings', 'bond-earrings', 'link-earrings', 
    'complice-bangle', 'echo-bangle', 'essentiel-bangle'
]

print("All Zulay Pogba products variant mapping:")
for handle in handles:
    rows = df[df['Handle'] == handle]
    print(f"\n======================================")
    print(f"Product Handle: {handle}")
    print(f"Number of rows: {len(rows)}")
    
    # We want to trace the Option1 values
    variants = []
    # In Shopify CSV, Title, Option1 Name are only present on the first row of a product,
    # and subsequent rows have these empty but have Option1 Value, Price, etc.
    # Let's inspect the actual values in the rows
    for idx, row in rows.iterrows():
        opt1_val = row.get('Option1 Value')
        price = row.get('Variant Price')
        img_src = row.get('Image Src')
        var_img = row.get('Variant Image')
        print(f"  Row {idx}: Option1 Value: {opt1_val} | Price: {price} | Image Src: {img_src} | Variant Image: {var_img}")
