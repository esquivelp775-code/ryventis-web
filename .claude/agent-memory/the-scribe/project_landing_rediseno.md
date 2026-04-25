---
name: Rediseño Landing Page ryventis.mx 2026-04-24
description: Patrones reutilizables y errores documentados del rediseño de la landing page a sitio multipage estático
type: project
---

El sitio pasó de SPA (1 página) a 5 páginas independientes: index, servicios, como-funciona, nosotros, contacto. Todos los archivos comparten el mismo bloque de security headers (CSP + X-Content-Type-Options + Referrer-Policy).

**Why:** El volumen de contenido por sección superaba lo manejable en una SPA sin framework de build. Las páginas independientes permiten SEO por URL y carga eficiente por sección.

**How to apply:** En futuros sitios de clientes con 4+ secciones de contenido denso, proponer arquitectura multipage desde el brief en lugar de SPA con anclas.

**Patrones reutilizables documentados:**
- `csp-html-estatico-sin-build`: `unsafe-inline` es el techo de seguridad alcanzable sin Webpack/Vite. Aceptado como tradeoff.
- `formulario-toggle-condicional`: JS puro que muestra campos según selección previa — reduce fricción en formularios de calificación.
- `intersection-observer-stagger`: Un solo observer con `data-delay` maneja todas las animaciones de entrada.
- `nav-multipage-dark`: Navbar con backdrop-filter y menú móvil en HTML puro.

**Errores recurrentes a prevenir (ERR-WEB-001/002/003):**
- Verificar email de contacto contra CLAUDE.md ANTES de escribir HTML.
- Solicitar número de WhatsApp Business como dato bloqueante en el brief inicial.
- Solicitar URLs de redes sociales reales antes de comenzar — nunca usar placeholders en archivos de producción.

**Pendiente al 2026-04-24:** Número WhatsApp y URLs sociales son placeholders. El sitio NO debe deployarse hasta que Pablo los confirme.
