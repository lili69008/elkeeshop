import re
import os

files = [
    'bagues.html', 
    'colliers.html', 
    'bracelets.html', 
    'boucles-doreilles.html', 
    'boutons-de-manchette.html', 
    'pendentifs.html'
]

for f in files:
    if not os.path.exists(f):
        print(f"Skipping {f} (not found)")
        continue
        
    try:
        with open(f, "r", encoding="utf-8") as file:
            html = file.read()
            
        # Regex to match <section id="..." that does not already contain class="reveal"
        # and inject class="reveal"
        pattern = r'<section\s+([^>]*id="[^"]+"[^>]*)>'
        
        def replace_sec(match):
            attrs = match.group(1)
            if 'class=' not in attrs:
                # Add class="reveal"
                return f'<section class="reveal" {attrs}>'
            elif 'reveal' not in attrs:
                # class exists but doesn't have reveal, append it
                return f'<section {attrs.replace("class=\"", "class=\"reveal ")}>'
            return match.group(0) # already has it
            
        fixed_html = re.sub(pattern, replace_sec, html)
        
        # Save back
        if fixed_html != html:
            with open(f, "w", encoding="utf-8") as file:
                file.write(fixed_html)
            print(f"Successfully fixed visibility classes in {f}")
        else:
            print(f"No visibility modifications needed in {f}")
            
    except Exception as e:
        print(f"Error fixing {f}: {e}")
