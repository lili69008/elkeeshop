import glob, re

files = ['bagues.html', 'colliers.html', 'bracelets.html', 'boucles-doreilles.html', 'boutons-de-manchette.html', 'pendentifs.html']
for f in files:
    try:
        with open(f, encoding='utf-8') as file:
            html = file.read()
            
        html = re.sub(r'<script>\s*// Intersection Observer.*?</script>', '', html, flags=re.DOTALL)
        
        script = '''
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const observerOptions = { threshold: 0.1 };
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('reveal');
                        if (entry.target.tagName.toLowerCase() === 'section') {
                            entry.target.style.opacity = 1;
                            entry.target.style.transform = 'translateY(0)';
                        }
                    }
                });
            }, observerOptions);

            document.querySelectorAll('section, .card').forEach(el => {
                observer.observe(el);
            });
        });
    </script>
'''
        # Insert before </body> if it exists, else append
        if '</body>' in html:
            html = html.replace('</body>', script + '\n</body>')
        else:
            html += script
            
        # also forcibly set section opacity to 1 immediately as fallback
        html = html.replace('<section id="bagues-hero"', '<section id="bagues-hero" class="reveal"')
        html = html.replace('<section id="bagues-grid"', '<section id="bagues-grid" class="reveal"')
            
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
        print(f'Fixed {f}')
    except Exception as e:
        print(e)
