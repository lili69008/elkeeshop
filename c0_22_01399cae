import os, json
from PIL import Image

root = r'c:\Users\lyies\Desktop\siteelk\localhost_v2'
img_dir = os.path.join(root, 'shopify_media')

imgs = []
for f in sorted(os.listdir(img_dir)):
    if f.lower().endswith(('.jpg','.jpeg','.png','.webp')):
        path = os.path.join(img_dir, f)
        try:
            im = Image.open(path)
            w, h = im.size
            kb = os.path.getsize(path) // 1024
            imgs.append({'file': f, 'w': w, 'h': h, 'kb': kb})
        except:
            pass

imgs.sort(key=lambda x: x['kb'], reverse=True)
print(f'Total unique: {len(imgs)}')
for im in imgs:
    print(f"{im['kb']:6d}KB  {im['w']}x{im['h']}  {im['file']}")
