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
