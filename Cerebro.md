# Cerebro - Vialex Landing Page

## Objetivo del Proyecto
Desarrollar una landing page de alta conversión para Vialex, una agencia de automatización de negocios con IA. El enfoque prioriza la carga rápida, alta mantenibilidad y una estética moderna de "agencia tecnológica".

## Decisiones Arquitectónicas

### 1. Stack Tecnológico
- **Marcado**: HTML5 semántico (`<header>`, `<main>`, `<section>`, `<footer>`).
- **Estilos**: CSS3 moderno (Custom Properties/Variables, Flexbox, CSS Grid). Todo dentro de un solo tag `<style>`.
- **Interactividad**: Vanilla JavaScript (sin bibliotecas ni dependencias). Todo dentro de un solo tag `<script>`.
- **Fuente**: Inter (Google Fonts).

### 2. Diseño (UI/UX)
- **Tema**: Dark mode por defecto.
- **Paleta de Colores**:
  - Fondo Global (`--bg-main`): `#0d0d0d`
  - Fondos Alternos: `--bg-alt-1` (`#111111`), `--bg-alt-2` (`#161616`)
  - Acento Principal (Verde): `#2d6a4f`
  - Acento Secundario (Dorado): `#c9a84c`
  - Textos: Blanco (`#ffffff`), Gris Claro (`#e2e8f0`).
- **Formas**: `border-radius: 12px` en tarjetas y botones.
- **Micro-interacciones**:
  - Hover effects con escalado y brillo (glow).
  - Sellos de confianza en el formulario con iconos dorados para resaltar legibilidad.
- **Botones**: Normalización de tamaño para botones de acción principal (ancho fijo de `240px` en formulario para coherencia con cabecera).
- **Responsive**: Estrategia Mobile-First, escalando componentes en el breakpoint de `768px` y `1024px`.

### 3. Rendimiento (Performance)
- Scroll suavizado nativo (`scroll-behavior: smooth`).
- Animaciones de carga controladas por `IntersectionObserver` (clase `fade-in`).
- Implementación de video nativo (`<video>`) optimizado con `object-fit: cover`.

### 4. Infraestructura y Despliegue
- **Hosting**: Vercel (Edge CDN, Zero-config, SSL automático).
- **Control de Versiones (CI/CD)**: Repositorio Git inicializado y vinculado a GitHub (`cmontenegro1411-hue/vialex-landing`).
- **Procesamiento de Formularios**: Arquitectura automatizada vía Webhooks.
  - Integración nativa con **Make.com** en tiempo real ("Immediately").
  - Almacenamiento centralizado en **Notion** (CRM).
  - Configuración de automatizaciones satélite: Notificaciones a Slack ("Speed to Lead") y Auto-respondedores en Gmail con plantilla HTML corporativa.
- **Seguridad y Privacidad**: Validación estricta en el Frontend; el envío se bloquea y los datos no salen del navegador si no se acepta explícitamente la política de privacidad, garantizando cumplimiento legal y evitando almacenamiento indebido.

## Estructura de Secciones (Orden Actualizado)
1. **Navbar**: Logo + Enlaces dinámicos + CTA "Solicitar Evaluación".
2. **Hero**: Propuesta de valor actualizada. Botón CTA primario y secundario ("Ver Soluciones").
3. **Servicios**: Grid con 3 pilares (Automatización, Agentes IA, Consultoría).
4. **Demostraciones (`#videos`)**: Título "¿Qué podemos hacer por tu empresa?".
   - Video RRHH: Optimización de procesos de contratación (Copy: "Gran parte del tiempo...").
   - Video Victoria: Asistente IA empresarial conectado a datos.
5. **Nuestro Proceso (`#proceso`)**: Infografía de 4 pasos (Descubrimiento, Diseño, Implementación, Entrega).
6. **FAQ (`#faq`)**: Acordeón con preguntas clave sobre seguridad y retorno de inversión.
7. **Recursos Gratuitos (`#recursos`)**: SECCIÓN OCULTA (Disponible en código para futura activación).
8. **Contacto (`#contacto`)**: Formulario de leads avanzado. Subtítulo enfocado en "Llamada de Evaluación".
9. **Footer**: Enlaces de navegación y redes sociales.

## Aspectos Legales y Navegación
- **Política de Privacidad**: Creación de `politica-de-privacidad.html` con términos legales estándar para el sector IA/Tech.
- **Navegación Fluida**: Se eliminó `target="_blank"` en enlaces internos de legalidad para evitar duplicidad de pestañas y mejorar la experiencia de usuario (SPA-like feel).

## Cambios Recientes Significativos
- Actualización de copy en RRHH: de "El 80%" a "Gran parte" para mayor naturalidad.
- Ajuste de dimensiones en el botón "Enviar" (240px) para igualar el impacto visual del botón de cabecera.
- Redacción de aviso de privacidad sin mención a "gratuidad" en la evaluación, enfocada en el proceso profesional.
- Intercalado de fondos corregido tras ocultar "Recursos": FAQ (Alt-1) -> Contacto (Alt-2) -> Footer (Main).
- **Rebranding completo a Vialex**:
  - Sustitución total de marca "MontiDigital" por "Vialex" en UI, Políticas de Privacidad y Reglas de Negocio.
  - Implementación de logotipo visual dual (Via-lex) en cabecera y pie de página en colores premium (blanco puro y `#2d6a4f`).
  - Creación de nuevo formulario standalone `formulario-leads-vialex.html`.
  - Actualización de scripts de soporte de color (`update_colors.py`, `revert_colors.py`) para evitar dependencias rotas.
- **Implementación de Infraestructura y Despliegue**:
  - Inyección de lógica `fetch` en el frontend hacia la URL del Webhook de Make.com.
  - Despliegue exitoso en producción (Vercel) con automatización CI/CD (GitHub).
  - Definición estratégica para el enlace de dominio personalizado (DNS).

---

## 📅 Sesión 4 de Agosto 2026

### Banner Hero
- Se actualizó la imagen del hero banner (`assets/logo-footer.png` → `assets/hero-image.png`).
- Se ajustó el `object-position` del hero de `center` → `25%` → `40%` → `32%` hasta lograr que el vaso quedara perfectamente centrado visualmente.
- Altura del banner ajustada a `380px`.

### Tipografía de Marca (VIALEX)
- Se importó la fuente **Nunito** (peso 700/800/900) desde Google Fonts para representar la identidad tipográfica del logo de Vialex.
- Se creó la clase CSS `.brand-text` con `font-family: Nunito`, `font-weight: 800` y `text-transform: uppercase`.
- Se aplicó la clase `.brand-text` a **todas las apariciones** del nombre Vialex en la página:
  - Logo del **Navbar** (cabecera): `VIA` en blanco + `LEX` en verde `#2d6a4f`.
  - Botón **VIALEX AI Hub** en la navbar (con separador `&nbsp;` para evitar colapso del texto).
  - Logo del **Footer** (pie de página): misma regla bicolor.
  - Texto de derechos de autor en el footer.

### Logo en el Footer
- Se reemplazó el texto `VIA<span>LEX</span>` del pie de página por una etiqueta `<img>` apuntando a `assets/logo-footer.png`.
- El archivo `logo-footer.png` fue copiado por el cliente a la carpeta `assets/` y pusheado a GitHub.
- Se ajustó el color de fondo del footer de `var(--bg-main)` (`#0d0d0d`) a **negro puro `#000000`** para eliminar el contraste visible entre el fondo del logo y la página.

### Estado Final del Footer
- Fondo: `#000000`
- Logo: imagen `assets/logo-footer.png` con `max-height: 80px`
- Texto derechos: `© 2025 VIALEX · Automatización con IA para pymes y emprendedores`

### Próximos Pasos Pendientes
- Revisar si el contraste del footer quedó completamente resuelto en producción.
- Evaluar si se necesita agregar una versión SVG o PNG con fondo transparente del logo para mayor flexibilidad.
- Continuar con ajustes de diseño o nuevas secciones según requerimientos del cliente.

## 📅 Sesión 11 de Agosto 2026

### Ajustes Visuales del Hero y Navegación
- **Ocultamiento del Botón Navbar Inicial**: Se añadió lógica CSS y JS para ocultar el CTA de la cabecera cuando se está en la cima de la página, mostrándolo gradualmente al hacer scroll.
- **Rediseño del Hero Banner**: 
  - Se eliminó el botón secundario ("Ver Soluciones").
  - Se estableció un diseño equilibrado a 2 columnas para no ocultar la marca de agua del fondo (la V).
  - Se integró una **Glass Card** (tarjeta estilo cristal) en la columna derecha para envolver el CTA, mejorando la estética premium.
  - Los textos ("Copy") de la propuesta de valor principal se acortaron para ser más directos.
- **Restauración de Enlace AI Hub**: Se descomentó el botón "VIALEX AI Hub" en la cabecera y se enlazó a su nuevo dominio en Vercel (`https://vialex-io-portal.vercel.app/`).
- **Unificación de Llamado a la Acción**: Todos los botones superiores y flotantes ahora muestran el texto unificado **"Solicitar Diagnóstico"**.

### Refinamiento de Copy (Sección Servicios)
- **Consultoría Estratégica**: Se ajustó el texto para enfocarse en la entrega llave en mano y capacitación del sistema.
- **Reportes Automáticos**: Se acortó el título de la tarjeta de "Reportes y Dashboards Inteligentes" para ser más ágil.
- **Automatización**: Se reformularon los textos de la tarjeta para listar explícitamente las herramientas conectadas (Excel, CRM, correos).

### Fortalecimiento de Seguridad y Tracking en Formulario
- Se añadieron atributos `required` para validación HTML5 nativa como respaldo al JavaScript.
- Se configuró semánticamente `method="POST"`.
- Se añadió una trampa **Anti-spam (Honeypot)** mediante un campo `_gotcha` oculto; bloquea envíos automatizados silenciosamente.
- Se incorporaron inputs ocultos e inyección JS para capturar variables **UTM** de campañas de marketing.
- Se incluyó integración nativa con el `dataLayer` de GTM (evento `form_submission`) al completarse el envío para registro de conversiones (Ads/Analytics).

### Optimización SEO y Rastreadores
- Se inyectaron metaetiquetas esenciales (`<meta name="description">`, `<meta name="keywords">`) para correcta indexación en Google.
- Se configuraron tarjetas Open Graph (`og:`) y Twitter Cards para enriquecer las previsualizaciones al compartir enlaces en redes sociales y WhatsApp.
- **⚠️ NOTA IMPORTANTE PENDIENTE:** Recordar actualizar la URL base de las etiquetas `og:url`, `og:image`, `twitter:url` y `twitter:image` una vez que se conecte el dominio personalizado definitivo. Actualmente apuntan a Vercel.
