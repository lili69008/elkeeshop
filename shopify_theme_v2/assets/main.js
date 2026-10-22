/**
 * ELKE BERR — Core Interactions
 * Shopify-migration ready: no external dependencies
 */

(function () {
    'use strict';

    /* ------------------------------------------------------------------
       UTILS
    ------------------------------------------------------------------ */
    const q  = (sel, ctx = document) => ctx.querySelector(sel);
    const qa = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

    /* Detect depth: root / 1-level (produits/) / 2-level (produits/rockn-rose/) */
    const base = q('link[href*="../../css/"]') ? '../../'
               : q('link[href*="../css/"]')    ? '../'
               : '';

    /* ------------------------------------------------------------------
       1. SCROLL REVEAL (Intersection Observer)
    ------------------------------------------------------------------ */
    function initReveal() {
        const io = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('reveal');
                    io.unobserve(entry.target);
                }
            });
        }, { threshold: 0.08, rootMargin: '0px 0px -60px 0px' });

        qa('section:not(.reveal), .will-reveal').forEach(el => {
            if (!el.classList.contains('reveal')) io.observe(el);
        });
    }

    /* ------------------------------------------------------------------
       2. STICKY NAV — hide on scroll down, show on scroll up
    ------------------------------------------------------------------ */
    function initStickyNav() {
        const nav = q('.nav-bar');
        if (!nav) return;

        let lastY = 0;
        let ticking = false;

        // Show nav instantly on mouse entering nav area
        nav.addEventListener('mouseenter', () => {
            nav.classList.remove('scroll-down');
            nav.classList.add('scroll-up');
        });

        window.addEventListener('scroll', () => {
            if (ticking) return;
            window.requestAnimationFrame(() => {
                const y = window.scrollY;
                const dropdownOpen = document.querySelector('.nav-links li.nav-open');
                if (y <= 10) {
                    nav.classList.remove('scroll-down', 'scroll-up');
                } else if (y > lastY + 5 && !dropdownOpen) {
                    nav.classList.add('scroll-down');
                    nav.classList.remove('scroll-up');
                } else if (y < lastY - 5) {
                    nav.classList.remove('scroll-down');
                    nav.classList.add('scroll-up');
                }
                lastY = y;
                ticking = false;
            });
            ticking = true;
        }, { passive: true });
    }

    /* ------------------------------------------------------------------
       3. DESKTOP NAV HOVER (JS — more reliable than CSS :hover for dropdowns)
    ------------------------------------------------------------------ */
    function initDesktopNav() {
        const navItems = qa('.nav-links > li');
        let closeTimer = null;

        navItems.forEach(li => {
            const menu = li.querySelector('.dropdown-menu, .mega-menu');
            if (!menu) return;

            function openMenu() {
                clearTimeout(closeTimer);
                // Close all other menus first
                navItems.forEach(other => {
                    if (other !== li) other.classList.remove('nav-open');
                });
                li.classList.add('nav-open');
            }

            function scheduleClose() {
                closeTimer = setTimeout(() => {
                    li.classList.remove('nav-open');
                }, 300);
            }

            li.addEventListener('mouseenter', openMenu);
            li.addEventListener('mouseleave', scheduleClose);
            menu.addEventListener('mouseenter', () => clearTimeout(closeTimer));
            menu.addEventListener('mouseleave', scheduleClose);
        });

        // Close all on click outside
        document.addEventListener('click', e => {
            if (!e.target.closest('.nav-links')) {
                navItems.forEach(li => li.classList.remove('nav-open'));
            }
        });
    }

    /* ------------------------------------------------------------------
       3b. MOBILE HAMBURGER MENU
    ------------------------------------------------------------------ */
    function initMobileNav() {
        const nav = q('.nav-bar');
        if (!nav) return;

        /* Inject hamburger button */
        const btn = document.createElement('button');
        btn.className = 'hamburger';
        btn.setAttribute('aria-label', 'Menu');
        btn.setAttribute('aria-expanded', 'false');
        btn.innerHTML = '<span></span><span></span><span></span>';
        nav.appendChild(btn);

        /* Build mobile overlay */
        const overlay = document.createElement('div');
        overlay.className = 'mobile-nav-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.innerHTML = getMobileNavHTML();
        document.body.appendChild(overlay);

        /* Toggle */
        btn.addEventListener('click', () => {
            const isOpen = document.body.classList.toggle('nav-open');
            btn.classList.toggle('is-active', isOpen);
            btn.setAttribute('aria-expanded', isOpen);
        });

        /* Close on overlay link click */
        qa('a', overlay).forEach(a => {
            a.addEventListener('click', closeNav);
        });

        /* Close on Escape */
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape') closeNav();
        });

        function closeNav() {
            document.body.classList.remove('nav-open');
            btn.classList.remove('is-active');
            btn.setAttribute('aria-expanded', 'false');
        }
    }

    function getMobileNavHTML() {
        const b = base;
        return `
        <ul class="mobile-nav-list">
            <li>
                <a href="${b}index.html">Accueil</a>
            </li>
            <li>
                <a href="${b}unbreakable.html">Unbreakable</a>
                <ul class="mobile-nav-sub">
                    <li><a href="${b}unbreakable-paul.html">Paul Pogba</a></li>
                    <li><a href="${b}unbreakable-zulay.html">Zulay Pogba</a></li>
                    <li><a href="${b}unbreakable-story.html">L'Histoire</a></li>
                    <li><a href="${b}unbreakable-villa.html">Lancement Villa Forbes</a></li>
                </ul>
            </li>
            <li>
                <a href="${b}private-jeweller.html">Joaillerie Privée</a>
            </li>
            <li>
                <a href="${b}haute-joaillerie.html">Haute Joaillerie</a>
                <ul class="mobile-nav-sub">
                    <li><a href="${b}haute-joaillerie-colliers.html">Colliers</a></li>
                    <li><a href="${b}haute-joaillerie-bagues.html">Bagues</a></li>
                    <li><a href="${b}haute-joaillerie-boucles-doreilles.html">Boucles d'oreilles</a></li>
                    <li><a href="${b}haute-joaillerie-bracelets.html">Bracelets</a></li>
                </ul>
            </li>
            <li>
                <a href="${b}bijoux.html">Bijoux</a>
                <ul class="mobile-nav-sub">
                    <li><a href="${b}rockn-rose.html">Rock'N Rose</a></li>
                    <li><a href="${b}singular.html">Singular</a></li>
                    <li><a href="${b}mysteria.html">Mysteria</a></li>
                    <li><a href="${b}waves.html">Waves</a></li>
                    <li><a href="${b}dolce.html">Dolce</a></li>
                    <li><a href="${b}me-you.html">Me &amp; You</a></li>
                    <li><a href="${b}milky-way.html">Milky Way</a></li>
                </ul>
            </li>
            <li>
                <a href="${b}maison.html">Maison EB</a>
                <ul class="mobile-nav-sub">
                    <li><a href="${b}maison-histoire.html">Histoire</a></li>
                    <li><a href="${b}maison-savoir-faire.html">Savoir-Faire</a></li>
                </ul>
            </li>
            <li><a href="${b}contact.html">Contact</a></li>
        </ul>
        <div class="mobile-nav-footer">
            <p style="font-size:0.6rem;letter-spacing:0.3em;text-transform:uppercase;color:var(--muted);">Genève — Depuis 1989</p>
            <div class="mobile-social">
                <a href="https://www.instagram.com/elkeberr_official/" target="_blank" rel="noopener" aria-label="Instagram">
                    ${svgInstagram()}
                </a>
                <a href="https://www.linkedin.com/company/elke-berr-cr-ations/?originalSubdomain=ch" target="_blank" rel="noopener" aria-label="LinkedIn">
                    ${svgLinkedIn()}
                </a>
                <a href="https://x.com/elkeberr_off" target="_blank" rel="noopener" aria-label="X">
                    ${svgX()}
                </a>
            </div>
        </div>`;
    }

    /* ------------------------------------------------------------------
       4. RICH FOOTER INJECTION
    ------------------------------------------------------------------ */
    function initFooter() {
        const footer = q('footer');
        if (!footer || footer.classList.contains('footer-rich')) return;

        const b = base;
        const richFooter = document.createElement('footer');
        richFooter.className = 'footer-rich';
        richFooter.innerHTML = `
            <div class="footer-inner">
                <div class="footer-brand-col">
                    <div class="footer-logo-mark">ELKE BERR</div>
                    <div class="footer-logo-sub">GENÈVE — DEPUIS 1989</div>
                    <p class="footer-tagline">L'Âme des Pierres Dicte l'Œuvre</p>
                    <div class="footer-social">
                        <a href="https://www.instagram.com/elkeberr_official/" target="_blank" rel="noopener" aria-label="Instagram">
                            ${svgInstagram()}
                        </a>
                        <a href="https://www.linkedin.com/company/elke-berr-cr-ations/?originalSubdomain=ch" target="_blank" rel="noopener" aria-label="LinkedIn">
                            ${svgLinkedIn()}
                        </a>
                        <a href="https://x.com/elkeberr_off" target="_blank" rel="noopener" aria-label="X">
                            ${svgX()}
                        </a>
                    </div>
                </div>
                <nav class="footer-nav-cols" aria-label="Navigation pied de page">
                    <div class="footer-nav-col">
                        <h6>Collections</h6>
                        <a href="${b}haute-joaillerie.html">Haute Joaillerie</a>
                        <a href="${b}bijoux.html">Bijoux</a>
                        <a href="${b}unbreakable.html">Unbreakable</a>
                        <a href="${b}rockn-rose.html">Rock'N Rose</a>
                        <a href="${b}singular.html">Singular</a>
                        <a href="${b}waves.html">Waves</a>
                    </div>
                    <div class="footer-nav-col">
                        <h6>Maison</h6>
                        <a href="${b}maison.html">Notre Histoire</a>
                        <a href="${b}maison-savoir-faire.html">Savoir-Faire</a>
                        <a href="${b}private-jeweller.html">Joaillerie Privée</a>
                        <a href="${b}news.html">Actualités</a>
                        <a href="${b}presse.html">Presse</a>
                        <a href="${b}contact.html">Contact</a>
                    </div>
                    <div class="footer-nav-col">
                        <h6>Information</h6>
                        <a href="${b}cgv.html">CGV</a>
                        <a href="${b}mentions-legales.html">Mentions Légales</a>
                        <a href="${b}confidentialite.html">Confidentialité</a>
                        <a href="${b}livraison-retours.html">Livraison &amp; Retours</a>
                    </div>
                </nav>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Elke Berr Creations — Rue du Cendrier, Genève, Suisse</p>
                <div class="footer-bottom-links">
                    <a href="${b}mentions-legales.html">Mentions Légales</a>
                    <a href="${b}confidentialite.html">Confidentialité</a>
                </div>
            </div>`;

        footer.replaceWith(richFooter);
    }

    /* ------------------------------------------------------------------
       5. PRODUCT GALLERY CAROUSEL
    ------------------------------------------------------------------ */
    function initProductGallery() {
        const gallery = q('.product-gallery');
        if (!gallery) return;

        const images = qa('img', gallery);
        if (images.length <= 1) return;

        /* Wrap first image in gallery-main */
        const mainDiv = document.createElement('div');
        mainDiv.className = 'gallery-main';
        const mainImg = images[0].cloneNode(true);
        mainImg.removeAttribute('style');
        mainDiv.appendChild(mainImg);
        gallery.innerHTML = '';
        gallery.appendChild(mainDiv);

        /* Build thumbnails row */
        const thumbsRow = document.createElement('div');
        thumbsRow.className = 'gallery-thumbs-row';

        images.forEach((src, idx) => {
            const thumb = document.createElement('div');
            thumb.className = 'gallery-thumb' + (idx === 0 ? ' is-active' : '');
            const tImg = src.cloneNode(true);
            thumb.appendChild(tImg);
            thumbsRow.appendChild(thumb);

            thumb.addEventListener('click', () => {
                mainImg.style.opacity = '0';
                setTimeout(() => {
                    mainImg.src = src.src;
                    mainImg.alt = src.alt;
                    mainImg.style.opacity = '1';
                }, 250);
                qa('.gallery-thumb', thumbsRow).forEach(t => t.classList.remove('is-active'));
                thumb.classList.add('is-active');
            });
        });

        gallery.appendChild(thumbsRow);

        /* Keyboard nav */
        let current = 0;
        document.addEventListener('keydown', e => {
            if (!q('.product-gallery')) return;
            if (e.key === 'ArrowRight') switchTo((current + 1) % images.length);
            if (e.key === 'ArrowLeft') switchTo((current - 1 + images.length) % images.length);
        });

        function switchTo(idx) {
            current = idx;
            const thumbs = qa('.gallery-thumb', thumbsRow);
            if (!thumbs[idx]) return;
            thumbs[idx].click();
        }
    }

    /* ------------------------------------------------------------------
       6. MARQUEE — duplicate content for seamless loop
    ------------------------------------------------------------------ */
    function initMarquee() {
        const track = q('.marquee-track');
        if (!track) return;
        /* Duplicate for seamless loop */
        track.innerHTML += track.innerHTML;
    }

    /* ------------------------------------------------------------------
       7. VIDEO — lazy play on visibility
    ------------------------------------------------------------------ */
    function initLazyVideos() {
        const videos = qa('video[data-lazy]');
        if (!videos.length) return;

        const io = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const v = entry.target;
                if (entry.isIntersecting) {
                    v.play().catch(() => {});
                } else {
                    v.pause();
                }
            });
        }, { threshold: 0.3 });

        videos.forEach(v => io.observe(v));
    }

    /* ------------------------------------------------------------------
       SVG ICONS (inline, no external deps)
    ------------------------------------------------------------------ */
    function svgInstagram() {
        return `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>`;
    }

    function svgLinkedIn() {
        return `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>`;
    }

    function svgX() {
        return `<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.259 5.631zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>`;
    }

    /* ------------------------------------------------------------------
       INIT
    ------------------------------------------------------------------ */
    document.addEventListener('DOMContentLoaded', () => {
        initReveal();
        initStickyNav();
        initDesktopNav();
        initMobileNav();
        initFooter();
        initProductGallery();
        initMarquee();
        initLazyVideos();
    });

})();
