# Rediseño Completo — Landing Page Ryventis Solutions

**Fecha:** 2026-04-24
**Versión del documento:** 1.0
**Autor:** The Scribe [GRIS — Nivel 5]
**Proyecto relacionado:** Landing page ryventis.mx
**Agentes involucrados:** The Stack [NARANJA — Nivel 4], The Scribe [GRIS — Nivel 5]
**Estado:** Entregado — pendiente de deploy a producción

---

## Resumen Ejecutivo

Se rediseñó y amplió el sitio web de Ryventis Solutions de una sola página (SPA) a un sitio estructurado de cinco páginas. El objetivo fue alinear la presencia digital de la agencia con su posicionamiento real: honesto, sin promesas no verificadas, orientado al dolor del cliente. Se eliminaron afirmaciones no respaldadas ("en menos de 72 horas"), se reemplazó la sección de precios fijos por un mensaje de propuesta personalizada, y se reforzó la seguridad del sitio con controles estándar de la industria. El sitio ahora cubre la totalidad del ciclo informativo del prospecto — desde la primera impresión hasta el contacto — sin revelar información competitivamente sensible.

---

## Archivos Modificados y Creados

| Archivo | Acción | Descripción |
|---------|--------|-------------|
| `Web/index.html` | Modificado | Página principal — 20+ cambios de contenido, visual y seguridad |
| `Web/servicios.html` | Creado | Detalle de servicios con metodología completa |
| `Web/como-funciona.html` | Creado | Proceso de trabajo en 5 pasos + principios de operación |
| `Web/nosotros.html` | Creado | Identidad de marca, etimología de Ryventis, manifiesto |
| `Web/contacto.html` | Creado | Formulario de contacto con validación JS + sidebar de info |

---

## Cambios de Contenido en index.html

| # | Elemento | Antes | Después | Razón |
|---|----------|-------|---------|-------|
| 1 | Eyebrow hero | "PYMES · Puebla, México" | "Inteligencia artificial para empresas" | Amplía el alcance percibido sin mentir |
| 2 | Subtítulo hero | Incluía "en menos de 72 horas" | Eliminado | Promesa no verificada — riesgo legal y de credibilidad |
| 3 | Slogan hero | — | "Tecnología que piensa, soluciones que ejecutan." | Nuevo mensaje que enfatiza autonomía operativa |
| 4 | Sección stats | 4 contadores animados con JS | 4 tarjetas de beneficio estáticas | Elimina datos inventados; los beneficios son reales y verificables |
| 5 | Sección ROI/editorial | Presente | Eliminada | Era especulativa; puede confundir a prospectos exigentes |
| 6 | Sección servicios | 5 bloques | 6 bloques (fila "¿Tu solución no está aquí?") | Captura necesidades no estándar — abre conversación |
| 7 | Headline "Cómo funciona" | Mencionaba "72 horas" | Eliminado + nota de tiempos variables | Consistencia con el cambio del hero |
| 8 | Sección precios | 3 pricing cards con MXN visibles | Bloque de propuesta personalizada | Evita anclar mal al prospecto antes del diagnóstico |
| 9 | Copy de sectores | Texto enfocado en ROI | Texto enfocado en el problema que atacamos | Más empático y honesto al dolor del cliente |
| 10 | Email de contacto | Incorrecto | `ryventis.solutions@gmail.com` | Corrección de dato operativo |
| 11 | Footer | Copyright desactualizado | Actualizado | Mantenimiento rutinario |
| 12 | Nav | Links a anclas internas | Links a páginas independientes | Navegación multipage coherente |

---

## Cambios de Seguridad (Aplicados a los 5 Archivos)

Todos los archivos del sitio comparten el mismo encabezado de seguridad. Los controles aplicados son:

| Control | Implementación | Notas |
|---------|---------------|-------|
| Content Security Policy (CSP) | `default-src 'self'` con directivas por recurso | `unsafe-inline` necesario para CSS/JS inline en HTML estático sin build tool — tradeoff documentado y aceptado |
| X-Content-Type-Options | `nosniff` via meta tag | Previene MIME-type sniffing |
| Referrer-Policy | `strict-origin-when-cross-origin` | Limita información enviada en referrer a sitios externos |
| Sanitización de formularios | Función `sanitize()` + `encodeURIComponent()` en URLs WhatsApp | Protege contra inyección en formularios |
| Límite en inputs | `maxlength` en todos los campos de formulario | Previene entradas masivas |
| Links externos | `rel="noopener noreferrer"` en 28 ocurrencias verificadas | Protege contra tab-napping |
| Referencias internas al stack | "n8n" eliminado del copy visible | Protege información competitiva del pitch |
| Comentarios de código | "Colores originales de CLAUDE.md" → "Paleta de marca" | Limpieza de referencias internas inadvertidas |
| Datos legales (LFPDPPP) | "Puebla" y "PYMEs" PRESERVADOS en modales legales | Requerimiento legal — domicilio registrado del responsable de datos |

---

## Decisiones de Arquitectura

### 1. Migración de SPA a sitio multipage
**Decisión:** Pasar de un único `index.html` (SPA con anclas) a cinco páginas independientes.
**Justificación:** El volumen de contenido y el nivel de detalle por sección superaban lo manejable en una sola página sin un framework. Las cinco páginas permiten navegación directa, mejor SEO por URL, y carga más eficiente por sección.
**Tradeoff aceptado:** Sin routing client-side, las transiciones entre páginas son recargas completas. Aceptable dado que no hay framework de build y el sitio es estático.

### 2. Precios ocultos en index.html, visibles en servicios.html
**Decisión:** `display:none` en `.service-price` en la página principal; precios mostrados en `servicios.html`.
**Justificación:** El prospecto que llega al index por primera vez no tiene contexto de valor. El precio sin diagnóstico puede generar rechazo prematuro. En `servicios.html`, el prospecto ya leyó la metodología y el proceso — contexto necesario para anclar correctamente.

### 3. Formulario de contacto con toggle condicional JS
**Decisión:** El textarea de descripción del proyecto aparece solo cuando el usuario selecciona un sector y un servicio.
**Justificación:** Reduce la fricción inicial del formulario. Invita al prospecto a comprometerse gradualmente en lugar de enfrentarlo con un formulario largo desde el inicio.

### 4. `unsafe-inline` en CSP
**Decisión:** Mantener `unsafe-inline` para `script-src` y `style-src`.
**Justificación:** El sitio es HTML estático puro — sin build tool (Webpack, Vite, Parcel) no es posible extraer CSS/JS a archivos externos y generar hashes de integridad dinámicamente. El tradeoff es necesario para mantener la arquitectura sin dependencias de build.
**Mitigación:** El resto de la CSP es estricto (`connect-src 'none'`, `frame-src 'none'`, `object-src 'none'`). No hay recursos de terceros cargados dinámicamente.
**Revisión futura:** Si el sitio migra a un build tool, eliminar `unsafe-inline` y usar hashes CSP.

### 5. Sistema de animaciones con IntersectionObserver unificado
**Decisión:** Un único observer maneja todas las animaciones de entrada (`.reveal`, `.reveal-left`, `.reveal-right`) con `data-delay` para stagger.
**Justificación:** Evita múltiples observers y event listeners redundantes. El stagger por `data-delay` permite control granular sin duplicar código.
**Accesibilidad:** Se respeta `prefers-reduced-motion` — las animaciones no se reproducen en dispositivos con esta preferencia activada.

---

## Estructura de las Páginas Nuevas

### servicios.html
- Metodología compartida de 5 fases: Diagnóstico → Blueprint → Build + QA → Deploy → Retención
- 6 bloques de servicio: Chatbot, Automatización, Agente Autónomo, Análisis de Datos, Consultoría, Pack Starter
- Cada bloque incluye: descripción, proceso específico, resultado esperado

### como-funciona.html
- Timeline vertical de 5 pasos del proceso de trabajo
- 4 principios de operación de Ryventis
- Nota explícita: los tiempos varían según complejidad — sin promesas de "72 horas"

### nosotros.html
- Etimología del nombre: Ry (ritmo) + Ventis (Ventus/dirección) + Solutions (destino)
- Manifiesto de la agencia
- 5 principios numerados de la forma de trabajar

### contacto.html
- Formulario con campos: nombre, empresa, sector (select), servicio de interés (select), textarea condicional
- Sidebar: email, teléfono (placeholder), ubicación, horario de respuesta
- Validación JS del lado del cliente antes del envío

---

## Pendientes Antes de Publicar en Produccion

> CRITICO: El sitio NO debe publicarse a ryventis.mx hasta que estos tres items esten resueltos.

| # | Pendiente | Archivo(s) afectado(s) | Responsable |
|---|-----------|----------------------|-------------|
| 1 | Reemplazar `+52 222 000 0000` con el numero real de WhatsApp Business | `index.html`, `contacto.html`, `servicios.html`, `como-funciona.html`, `nosotros.html` | Pablo (CEO) |
| 2 | Reemplazar URLs de redes sociales genericas con URLs reales de Ryventis (TikTok, Instagram, LinkedIn) | Las 4 paginas nuevas | Pablo (CEO) |
| 3 | Ejecutar `bash deploy.sh` para sincronizar con GitHub y Hostinger | — | Pablo (CEO) o The Stack |

---

## Lecciones Aprendidas

### Lo que funciono bien

1. **Separar contenido honesto de contenido aspiracional desde el inicio.** Eliminar "72 horas" y los contadores animados desde el rediseno — no como correccion posterior — es mas limpio y coherente. Aplicar en futuros sitios desde el brief.

2. **CSP en HTML estatico sin build tool.** El patron `default-src 'self'` + directivas por tipo de recurso + `unsafe-inline` solo para script/style es el nivel optimo de seguridad alcanzable sin pipeline de build. Documentado como patron reutilizable.

3. **Toggle condicional de formulario con JS puro.** El patron de mostrar campos adicionales segun la seleccion previa reduce la friccion sin necesidad de frameworks. Reutilizable en cualquier formulario de calificacion de leads.

4. **IntersectionObserver unificado con data-delay.** Un solo bloque de JS maneja todas las animaciones de entrada. Patron limpio y extensible. Reutilizar en futuros proyectos de sitios estaticos para clientes.

### Que debe mejorarse

1. **Definir el numero de WhatsApp Business antes de iniciar el rediseno.** En este proyecto el numero era un placeholder. En futuros proyectos, solicitar todos los datos operativos al CEO antes de escribir la primera linea de HTML.

2. **Solicitar URLs de redes sociales en el brief inicial.** Lo mismo aplica: pedir las URLs reales de TikTok, Instagram y LinkedIn antes de comenzar — no despues.

3. **Documentar el deploy.sh antes de entregar.** El script existe pero no fue revisado en este ciclo. En futuros redisenos de landing, verificar que el pipeline CI/CD funciona como parte del QA.

---

## Bloques Modulares Extraidos

Los siguientes patrones fueron identificados como reutilizables en futuros proyectos de clientes:

| Bloque | Descripcion | Aplicabilidad |
|--------|-------------|---------------|
| `formulario-toggle-condicional` | Formulario HTML + JS puro que muestra campos segun seleccion previa | Calificacion de leads en cualquier sector |
| `csp-html-estatico-sin-build` | Encabezado CSP completo para sitios HTML estaticos sin pipeline de build | Todos los sitios estaticos de clientes |
| `intersection-observer-stagger` | Observer unificado con data-delay para animaciones de entrada escalonadas | Todos los sitios estaticos con animaciones |
| `nav-multipage-dark` | Navbar con backdrop-filter, links activos y menu movil en HTML puro | Sitios multipage sin framework |

> Referencia: Extraer estos bloques a `Documentacion/Base-de-Conocimiento/Bloques-Modulares/` en el siguiente ciclo de actualizacion de la base de conocimiento.

---

## Clasificacion de Errores Encontrados

| ID | Descripcion | Causa Raiz | Quick Fix | Prevencion |
|----|-------------|------------|-----------|------------|
| ERR-WEB-001 | Email de contacto incorrecto en produccion | No se verifico el dato contra la fuente autoritativa (CLAUDE.md) antes de publicar | Buscar y reemplazar en todos los archivos HTML | En el brief: listar todos los datos de contacto y verificarlos contra CLAUDE.md antes de iniciar |
| ERR-WEB-002 | Numero de WhatsApp placeholder en produccion | El numero real no se definio antes de comenzar el desarrollo | Reemplazar `+52 222 000 0000` en todos los archivos antes del deploy | Solicitar numero de WhatsApp Business como dato bloqueante en el brief inicial |
| ERR-WEB-003 | URLs de redes sociales genericas en paginas nuevas | Las URLs reales no se solicitaron en el brief | Reemplazar con URLs reales antes del deploy | Incluir "URLs de redes sociales" en el checklist de brief de cualquier sitio web |

---

## Tags

`landing-page` `html-estatico` `multipage` `seguridad-web` `csp` `formulario` `animaciones` `ryventis-mx` `2026-04` `the-stack` `the-scribe`
