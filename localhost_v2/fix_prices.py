import os
import glob

# Fix the HTML files directly
def fix_prices_in_html():
    files = glob.glob('*.html') + glob.glob('produits/*.html')
    count = 0
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace 0.00 CHF with Sur demande
        if "0.00 CHF" in content:
            new_content = content.replace("0.00 CHF", "Sur demande")
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            
    print(f"Fixed prices in {count} HTML files.")

# Fix the python generation scripts so future runs are correct
def fix_python_scripts():
    scripts = ['generate_product_pages.py', 'generate_collections.py', 'fix_categories.py', 'sort_by_color.py']
    for script in scripts:
        if os.path.exists(script):
            with open(script, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find price logic and update it to handle 0.00
            content = content.replace('p[\'price\'] != "0"', 'float(p[\'price\'].replace(",", "")) > 0')
            content = content.replace('price == "0"', 'float(str(price).replace(",", "")) == 0')
            
            with open(script, 'w', encoding='utf-8') as file:
                file.write(content)

if __name__ == "__main__":
    fix_prices_in_html()
    # fix_python_scripts() -> manual update might be safer for scripts, let's just do it simple
