import os
import re

# DIR TO PROCESS
BASE_DIR = r"c:\Users\lyies\Desktop\siteelk\localhost_v2"

# SIDEBAR NAV HTML (RESTORED VERSION)
SIDEBAR_NAV = """    <nav class="nav-bar">
        <div class="logo-container">
            <span class="logo-main">ELKE BERR</span>
            <span class="logo-sub">GENÈVE</span>
        </div>
        <div class="hamburger" id="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </nav>

    <div class="sidebar" id="sidebar">
        <div class="sidebar-links">
            <a href="index.html">Accueil</a>
            <a href="maison.html">La Maison</a>
            <div class="sidebar-dropdown">
                <a href="unbreakable.html">Unbreakable</a>
                <div class="unbreakable-sub">
                    <a href="unbreakable.html">The Story</a>
                    <a href="unbreakable-paul.html">Elke Berr X Paul Pogba</a>
                    <a href="unbreakable-zulay.html">Elke Berr X Zulay Pogba</a>
                </div>
            </div>
            
            <div class="sidebar-dropdown">
                <a href="bagues.html">Bijoux</a>
                <div class="sidebar-mega">
                    <div class="mega-group">
                        <h4>Catégories</h4>
                        <div class="mega-links">
                            <a href="bagues.html">Bagues</a>
                            <a href="colliers.html">Colliers</a>
                            <a href="bracelets.html">Bracelets</a>
                            <a href="boucles-doreilles.html">Boucles d'oreilles</a>
                            <a href="pendentifs.html">Pendentifs</a>
                        </div>
                    </div>
                    <div class="mega-group">
                        <h4>Collections</h4>
                        <div class="mega-links">
                            <a href="#">Rock'N Rose</a>
                            <a href="#">Singular</a>
                            <a href="#">Mysteria</a>
                            <a href="#">Waves</a>
                        </div>
                    </div>
                    <div class="mega-group">
                        <h4>Idées Cadeaux</h4>
                        <div class="mega-links">
                            <a href="#">Pour Elle</a>
                            <a href="#">Pour Lui</a>
                            <a href="#">Sélections</a>
                        </div>
                    </div>
                </div>
            </div>

            <a href="joaillerie.html">Haute Joaillerie</a>
            <a href="bespoke.html">Bespoke</a>
            <a href="news.html">News</a>
            <a href="contact.html">Contact</a>
        </div>
    </div>

    <script>
        const hamburger = document.getElementById('hamburger');
        const sidebar = document.getElementById('sidebar');

        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            sidebar.classList.toggle('active');
        });

        // Close sidebar when clicking outside
        document.addEventListener('click', (e) => {
            if (!sidebar.contains(e.target) && !hamburger.contains(e.target)) {
                sidebar.classList.remove('active');
                hamburger.classList.remove('active');
            }
        });
    </script>"""

def update_nav(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the <nav class="nav-bar">...</nav> block AND any following sidebar/script if they exist
    # Since the previous horizontal version only had <nav class="nav-bar">...</nav>, we replace that.
    nav_pattern = re.compile(r'<nav class="nav-bar">.*?</nav>', re.DOTALL)
    
    if nav_pattern.search(content):
        new_content = nav_pattern.sub(SIDEBAR_NAV, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {os.path.basename(file_path)}")
    else:
        print(f"No nav found in: {os.path.basename(file_path)}")

# RUN ON ALL HTML FILES
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]
for file in html_files:
    update_nav(os.path.join(BASE_DIR, file))

print("DONE: All pages REVERTED to sidebar drawer navigation.")
