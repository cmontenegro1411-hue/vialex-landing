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

    # Revert Logos
    old_nav_logo = '<a href="#" class="nav-logo" style="display:flex; align-items:center;"><img src="assets/vialex-logo.png" alt="Vialex" style="height: 32px; width: auto; object-fit: contain;"></a>'
    new_nav_logo = '<a href="#" class="nav-logo">Monti<span style="color: var(--accent-green);">Digital</span></a>'
    content = content.replace(old_nav_logo, new_nav_logo)
    
    old_footer_logo = '<div class="footer-logo"><img src="assets/vialex-logo.png" alt="Vialex" style="height: 40px; width: auto; opacity: 0.8;"></div>'
    new_footer_logo = '<div class="footer-logo">MontiDigital</div>'
    content = content.replace(old_footer_logo, new_footer_logo)
    
    old_hero_img = '<img src="assets/vialex-logo.png" alt="Vialex Cabecera" class="hero-banner-img" style="object-fit: contain; padding: 2rem; background: rgba(255,255,255,0.02); height: 180px;">'
    new_hero_img = '<img src="assets/hero-image.png" alt="MontiDigital Cabecera" class="hero-banner-img">'
    content = content.replace(old_hero_img, new_hero_img)

    # Revert General text mentions
    content = content.replace('Vialex', 'MontiDigital')

    # Revert Colors
    content = content.replace('rgba(42, 106, 123', 'rgba(45, 106, 79')
    content = content.replace('rgba(92, 164, 147', 'rgba(201, 168, 76')
    
    content = content.replace('#2a6a7b', '#2d6a4f')
    content = content.replace('#1b4551', '#1b4332')
    content = content.replace('#368a96', '#1d9e75')

    # Revert #5ca493. 
    # Because #c9a84c and #52b788 were both changed to #5ca493, we need to map them back intelligently based on the context.
    # In index.html, #52b788 was used for:
    # color: #52b788;
    #   in .lead-badge
    #   in .privacy-row label a
    #   in .success-time
    #   in .proceso-step-number.color-green
    #   in .proceso-highlight-icon
    
    # To be safe, we change ALL #5ca493 to #c9a84c
    content = content.replace('#5ca493', '#c9a84c')
    
    # Then we restore the specific #52b788 ones
    content = content.replace('color: #c9a84c;\n            border: 1px solid rgba(45,106,79,0.3);', 'color: #52b788;\n            border: 1px solid rgba(45,106,79,0.3);')
    content = content.replace('color: #c9a84c; text-decoration: none;', 'color: #52b788; text-decoration: none;')
    content = content.replace('color: #c9a84c;\n            border-radius: 6px;', 'color: #52b788;\n            border-radius: 6px;')
    content = content.replace('color: #c9a84c;\n        }', 'color: #52b788;\n        }')
    content = content.replace('color: #c9a84c;\n            flex-shrink: 0;', 'color: #52b788;\n            flex-shrink: 0;')
    # For .lead-badge the exact original was:
    # color: #52b788;
    # border: 1px solid rgba(45,106,79,0.3);
    # Which I replaced above.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Reverted files successfully')
