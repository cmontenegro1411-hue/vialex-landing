import re
import os

files = [
    r'c:\Users\cmont\OneDrive (1)\Documentos\Montidigital\Proyectos Antigravity\Landing Page\index.html',
    r'c:\Users\cmont\OneDrive (1)\Documentos\Montidigital\Proyectos Antigravity\Landing Page\formulario-leads-vialex.html',
    r'c:\Users\cmont\OneDrive (1)\Documentos\Montidigital\Proyectos Antigravity\Landing Page\politica-de-privacidad.html',
    r'c:\Users\cmont\OneDrive (1)\Documentos\Montidigital\Proyectos Antigravity\Landing Page\proceso-snippet.html'
]

for file_path in files:
    if not os.path.exists(file_path): continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Colors
    content = re.sub(r'rgba\(45,\s*106,\s*79', r'rgba(42, 106, 123', content)
    content = re.sub(r'rgba\(201,\s*168,\s*76', r'rgba(92, 164, 147', content)
    
    content = content.replace('#2d6a4f', '#2a6a7b')
    content = content.replace('#1b4332', '#1b4551')
    content = content.replace('#c9a84c', '#5ca493')
    content = content.replace('#52b788', '#5ca493')
    content = content.replace('#1d9e75', '#368a96')

    # Logos
    old_nav_logo = '<a href="#" class="nav-logo">Monti<span style="color: var(--accent-green);">Digital</span></a>'
    new_nav_logo = '<a href="#" class="nav-logo" style="display:flex; align-items:center;"><img src="assets/vialex-logo.png" alt="Vialex" style="height: 32px; width: auto; object-fit: contain;"></a>'
    content = content.replace(old_nav_logo, new_nav_logo)
    
    content = content.replace('<div class="footer-logo">MontiDigital</div>', '<div class="footer-logo"><img src="assets/vialex-logo.png" alt="Vialex" style="height: 40px; width: auto; opacity: 0.8;"></div>')
    
    old_hero_img = '<img src="assets/hero-image.png" alt="MontiDigital Cabecera" class="hero-banner-img">'
    new_hero_img = '<img src="assets/vialex-logo.png" alt="Vialex Cabecera" class="hero-banner-img" style="object-fit: contain; padding: 2rem; background: rgba(255,255,255,0.02); height: 180px;">'
    content = content.replace(old_hero_img, new_hero_img)

    # General text mentions
    content = content.replace('MontiDigital', 'Vialex').replace('Montidigital', 'Vialex')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated files successfully')
