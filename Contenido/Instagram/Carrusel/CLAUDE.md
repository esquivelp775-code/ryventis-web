# Sistema de Carruseles Ryventis IA — Prompt Maestro
**Versión:** 3.0 — Integrado con design_system.json + BRIEF_FEED_VISUAL.md  
**Marca:** @ryventis_ia / Ryventis Solutions  
**Handle IG:** @ryventisia  
**Sitio:** ryventis.mx

---

## CÓMO USAR ESTE DOCUMENTO

Antes de generar cualquier carrusel, lee este archivo completo. Contiene las reglas definitivas de:
1. Paleta de colores y proporciones
2. Tipografía (Syne + DM Sans)
3. Tres templates base (A, B, C) y cuándo usar cada uno
4. Arquitectura de slides por template
5. Componentes HTML reutilizables
6. Script de exportación a PNG 1080×1350px

Los archivos de referencia están en esta misma carpeta:
- `design_system.json` — tokens de diseño completos
- `BRIEF_FEED_VISUAL.md` — brief detallado con los 9 posts del grid de lanzamiento

---

## REGLA DE ORO: SIEMPRE LEE ESTE ARCHIVO PRIMERO

Cuando el usuario pida un carrusel de Ryventis, ejecutar en este orden:
1. Leer `CLAUDE.md` (este archivo)
2. Preguntar qué template (A/B/C) o determinar por el tipo de contenido
3. Preguntar el tema y contenido específico
4. Generar HTML siguiendo EXACTAMENTE las reglas de este archivo
5. Exportar con el script Playwright
6. Verificar visualmente cada slide

---

## BLOQUE 1 — PALETA DE COLORES DEFINITIVA

### Colores base (siempre disponibles)

```
NEGRO_PROFUNDO   = "#0A0A0F"   → Fondo principal — columna izquierda (Template A)
OSCURO_A         = "#111118"   → Fondo columna central (Template B)
OSCURO_B         = "#1C1C28"   → Fondo superior del gradiente (Template C) + fondo de badges
CIAN             = "#00E5CC"   → Acento primario: palabras clave, números, bordes de badge, líneas
CIAN_OSCURO      = "#00B8A3"   → Separadores internos dentro de carruseles
VIOLETA          = "#7C3AED"   → Solo Template C (columna derecha) y máx. 1 post cada 6
BLANCO_SUAVE     = "#F0F0F8"   → Todo el texto principal
GRIS_MUTED       = "#8888A8"   → Texto secundario, numeración slides, disclaimers
```

### Colores de producción Instagram (uso interno en slides)

```
FONDO_BADGE      = "#1C1C28"   → Rectángulo detrás de etiquetas tipo "DATO", "PASO 1"
BORDE_BADGE_CIAN = "#00E5CC"   → Contorno 1.5px badges — Templates A y B
BORDE_BADGE_VIO  = "#7C3AED"   → Contorno 1.5px badges — Template C únicamente
CTA_BOX_BG       = "rgba(0,229,204,0.12)"  → Fondo caja CTA (Templates A y B)
CTA_BOX_BORDER   = "#00E5CC"   → Borde 1px caja CTA
CTA_BOX_VIO_BG   = "rgba(124,58,237,0.12)" → Fondo caja CTA Template C
CTA_BOX_VIO_BDR  = "#7C3AED"   → Borde 1px caja CTA Template C
LINEA_DIV        = "#1C1C28"   → Línea horizontal 1px separadora dentro de slides
PUNTO_ENFASIS    = "#00E5CC"   → Círculo 8px viñeta en listas
NUMERO_STAT      = "#00E5CC"   → Números grandes estadísticos (mín. 64pt)
CIRCULO_PASO_BG  = "#111118"   → Fondo del círculo de numeración Template B
```

### Regla de proporciones por slide (OBLIGATORIA)

```
70% → negro/oscuro — fondos, espacio vacío, respiro visual
20% → blanco suave (#F0F0F8) — texto que comunica el mensaje
 8% → cian (#00E5CC) — acento que dirige la mirada
 2% → gris muted (#8888A8) — texto secundario, numeración, disclaimers
```

Si el cian supera el 10%, la pieza pierde impacto. El cian funciona por contraste, no por volumen.

---

## BLOQUE 2 — TIPOGRAFÍA

### Fuentes (Google Fonts — cargar ambas siempre)

```html
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

```
.heading  → font-family: 'Syne', sans-serif;
.body     → font-family: 'DM Sans', sans-serif;
```

**REGLA DURA:** Solo Syne y DM Sans. Nunca Poppins, Lato, Montserrat, Space Grotesk ni ninguna otra.

### Escala tipográfica

| Elemento | Fuente | Peso | Tamaño en HTML (420px base) | Color |
|----------|--------|------|-----------------------------|-------|
| Badge/etiqueta de categoría | DM Sans | 500 | 10px (=14pt escalado) | `#00E5CC` (A/B) o `#7C3AED` (C) |
| Título portada | Syne | 800 | 28–34px | `#F0F0F8` (palabras clave en `#00E5CC`) |
| Número grande portada (Template B) | Syne | 800 | 80–96px | `#00E5CC` |
| Número protagonista (Template C) | Syne | 800 | 64–80px | `#00E5CC` |
| Número estadístico destacado | Syne | 800 | 44–52px | `#00E5CC` |
| Título de sección interna | Syne | 700 | 22–26px | `#F0F0F8` |
| Número de paso (círculo) | Syne | 800 | 16px | `#00E5CC` |
| Título del paso | Syne | 700 | 20–24px | `#F0F0F8` (1 palabra en `#00E5CC`) |
| Cuerpo / descripción | DM Sans | 400 | 13–14px | `#F0F0F8` |
| Texto secundario / fuente | DM Sans | 400 | 11px | `#8888A8` |
| Numeración slides | DM Sans | 400 | 10px | `#8888A8` |
| Subtexto portada | DM Sans | 400 | 12px | `#8888A8` |
| CTA texto | Syne | 700 | 18–22px | `#F0F0F8` |
| CTA subtexto | DM Sans | 400 | 12px | `#8888A8` |

*(Estos tamaños son para el viewport 420px; el scale factor 2.5714× los convierte a 1080px equivalente)*

---

## BLOQUE 3 — TRES TEMPLATES BASE

### Template A — Educativo / Datos
- **Cuándo usarlo:** contenido educativo, datos estadísticos, explicaciones conceptuales
- **Fondo portada:** `#0A0A0F` (negro profundo)
- **Fondo slides internas:** `#0A0A0F` (continuidad)
- **Badge borde:** `#00E5CC`
- **Badge texto:** `#00E5CC` en mayúsculas
- **Número de slides:** 4 (portada + 2 contenido + CTA)
- **Elemento visual firma:** línea cian 60×3px debajo del título

#### Estructura slide a slide — Template A

**SLIDE 1 — Portada**
```
[BADGE: fondo #1C1C28, borde #00E5CC 1.5px] ← top-left, 40px de bordes
[NUMERACIÓN: "01 / 04"] ← top-right, 40px de bordes, DM Sans 10px, #8888A8

[TÍTULO SYNE 800, 28-34px, #F0F0F8, izquierda]
  → 1-2 palabras clave en #00E5CC
  → máximo 3 líneas
[LÍNEA CIAN: 60×3px, #00E5CC, 20px debajo del título]
[SUBTEXTO: DM Sans 400 12px, #8888A8, "Desliza para ver →"]

[LOGO RYVENTIS: bottom-left, 40px de bordes]
[FLECHA/CHEVRON →: bottom-right, #00E5CC, DM Sans 500 12px]
```

**SLIDES 2–3 — Contenido**
```
[NUMERACIÓN: "02 / 04"] ← top-right
[TÍTULO SECCIÓN: Syne 700, 22px, #F0F0F8]
[LÍNEA CIAN: 60×3px]

[NÚMERO/DATO DESTACADO (si aplica): Syne 800, 44-52px, #00E5CC]
[CONTEXTO DEL NÚMERO: Syne 700, 18px, #F0F0F8]

[CUERPO: DM Sans 400, 13px, #F0F0F8, interlineado 1.55]
  → viñetas: círculo 8px #00E5CC como bullet si hay lista

[LOGO RYVENTIS: bottom-left]
```

**SLIDE FINAL — CTA**
```
[NUMERACIÓN: "04 / 04"]
[RECTÁNGULO CTA: fondo rgba(0,229,204,0.12), borde 1px #00E5CC, radio 8px, centrado]
  [CTA TEXTO: Syne 700, 18px, #F0F0F8, centrado]
  [CTA SUBTEXTO: DM Sans 400, 12px, #8888A8, centrado]
  → Ejemplo: "¿Cuántas horas recuperarías tú?"
  → subtexto: "Diagnóstico gratuito en ryventis.mx"
[LOGO RYVENTIS: bottom-left]
```

---

### Template B — Proceso / Paso a Paso
- **Cuándo usarlo:** explicar procesos, "cómo funciona", pasos numerados, flujos
- **Fondo portada:** `#111118` (diferente al A para variación en el grid)
- **Fondo slides de pasos:** `#0A0A0F`
- **Badge borde:** `#00E5CC`
- **Número de slides:** 5 (portada + 3 pasos + CTA)

#### Estructura slide a slide — Template B

**SLIDE 1 — Portada**
```
[BADGE: fondo #1C1C28, borde #00E5CC 1.5px] ← top-left
[NUMERACIÓN: "01 / 05"] ← top-right

[NÚMERO GRANDE: Syne 800, 80-96px, #00E5CC — solo en su línea]
  → Este número es el anzuelo: "4", "72", "3", etc.
[TÍTULO: Syne 800, 28px, #F0F0F8, máx 2 líneas]
  → Complementa el número: "pasos para automatizar tu WhatsApp"
[SUBTEXTO: DM Sans 400, 12px, #8888A8, "Desliza para ver cada paso →"]

[LOGO: bottom-left]
[CHEVRON →: bottom-right, #00E5CC]
```

**SLIDES DE PASOS (una por paso)**
```
[CÍRCULO PASO: 36px diámetro, fondo #111118, borde 1.5px #00E5CC]
  [NÚMERO: Syne 800, 16px, #00E5CC, centrado]
  ← posición: top-left, 40px bordes
[NUMERACIÓN: "02 / 05"] ← top-right

[TÍTULO DEL PASO: Syne 700, 20-24px, #F0F0F8]
  → UNA palabra clave en #00E5CC
[LÍNEA CIAN: 60×3px, #00E5CC, 20px debajo del título]
[DESCRIPCIÓN: DM Sans 400, 13px, #F0F0F8, interlineado 1.55, máx 4 líneas]

[CAJA DATO/MÉTRICA (opcional): fondo #1C1C28, radio 6px]
  [TEXTO: DM Sans 400, 11px, #8888A8]
  → Ejemplo: "Tiempo de este paso: 15 minutos"

[LOGO: bottom-left]
```

**SLIDE FINAL — CTA** (puede ser el último paso + CTA combinados)
```
[CÍRCULO PASO con último número] ← si hay paso final
[TÍTULO Y DESCRIPCIÓN del último paso]
[LÍNEA DIVISORIA: #1C1C28, 1px]
[RECTÁNGULO CTA: rgba(0,229,204,0.12), borde 1px #00E5CC, radio 8px]
  [CTA: Syne 700, 18px, #F0F0F8]
  [SUBTEXTO: DM Sans 400, 12px, #8888A8]
[LOGO: bottom-left]
```

---

### Template C — Resultado / Prueba Social
- **Cuándo usarlo:** casos de éxito, resultados, antes/después, estadísticas de impacto
- **Fondo portada:** gradiente `linear-gradient(180deg, #1C1C28 0%, #0A0A0F 100%)`
- **Fondo slide 2:** `#0A0A0F`
- **Badge borde:** `#7C3AED` (violeta — diferenciador visual)
- **Badge texto:** `#7C3AED`
- **Número de slides:** 3 (portada + detalle + CTA)

#### Estructura slide a slide — Template C

**SLIDE 1 — Portada**
```
[BADGE: fondo #1C1C28, borde #7C3AED 1.5px] ← top-left
[NUMERACIÓN: "01 / 03"] ← top-right

[NÚMERO PROTAGONISTA: Syne 800, 64-80px, #00E5CC — para el scroll]
  → Ejemplos: "50 hrs", "3×", "72 hrs", "87%", "$57,600"
[CONTEXTO: Syne 700, 22px, #F0F0F8, debajo del número]
  → Complementa: "recuperadas al mes"
[LÍNEA CIAN: 60×3px]
[DESCRIPCIÓN: DM Sans 400, 13px, #F0F0F8, máx 3 líneas]
[CTA BREVE OPCIONAL: DM Sans 500, 11px, #7C3AED, bottom-right]

[LOGO: bottom-left]
```

**SLIDE 2 — Antes / Después**
```
[NUMERACIÓN: "02 / 03"]

[BLOQUE ANTES:]
  [ETIQUETA "ANTES": DM Sans 500, 10px, #8888A8 — mayúsculas]
  [DESCRIPCIÓN: DM Sans 400, 13px, #F0F0F8]

[LÍNEA CIAN: 60×3px, separadora]

[BLOQUE DESPUÉS:]
  [ETIQUETA "DESPUÉS": DM Sans 500, 10px, #00E5CC — mayúsculas]
  [DESCRIPCIÓN: DM Sans 400, 13px, #F0F0F8]

[QUOTE (solo si hay testimonio real):]
  [RECTÁNGULO: fondo #1C1C28, borde-izq 3px #7C3AED]
  [TEXTO QUOTE: DM Sans 400 italic, 12px, #8888A8]
  [FIRMA: DM Sans 500, 11px, #F0F0F8, precedida de "—"]
  → NUNCA inventar citas. Si no hay testimonio real, omitir este bloque.

[LOGO: bottom-left]
```

**SLIDE 3 — CTA**
```
[NUMERACIÓN: "03 / 03"]
[GRADIENTE: linear-gradient(180deg, #1C1C28, #0A0A0F)]

[RECTÁNGULO CTA: rgba(124,58,237,0.12), borde 1px #7C3AED, radio 8px, centrado]
  [CTA: Syne 700, 18px, #F0F0F8]
  [SUBTEXTO: DM Sans 400, 12px, #8888A8]
  → Ejemplo: "¿Quieres este resultado?\nDiagnóstico gratuito en ryventis.mx"

[LOGO: bottom-left]
```

---

## BLOQUE 4 — COMPONENTES HTML REUTILIZABLES

### CSS Base (siempre en el `<style>`)

```css
:root {
  --negro:    #0A0A0F;
  --oscuro-a: #111118;
  --oscuro-b: #1C1C28;
  --cian:     #00E5CC;
  --cian-dark:#00B8A3;
  --violeta:  #7C3AED;
  --blanco:   #F0F0F8;
  --gris:     #8888A8;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
.heading { font-family: 'Syne', sans-serif; }
.body    { font-family: 'DM Sans', sans-serif; }

body {
  background: #1A1A1A;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 24px 20px;
  font-family: 'DM Sans', sans-serif;
}

/* IG Frame */
.ig-frame {
  width: 420px;
  background: var(--negro);
  border-radius: 12px;
  box-shadow: 0 12px 50px rgba(0,0,0,0.6);
  overflow: hidden;
  user-select: none;
}

/* Carousel */
.carousel-viewport {
  width: 420px;
  aspect-ratio: 4 / 5;
  overflow: hidden;
  cursor: grab;
  position: relative;
}
.carousel-viewport:active { cursor: grabbing; }
.carousel-track {
  display: flex;
  height: 100%;
  transition: transform 0.32s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Slide base */
.slide {
  width: 420px;
  height: 525px;
  flex-shrink: 0;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.slide-negro    { background: #0A0A0F; }
.slide-oscuro-a { background: #111118; }
.slide-oscuro-b { background: #1C1C28; }
.slide-gradient { background: linear-gradient(180deg, #1C1C28 0%, #0A0A0F 100%); }

/* Content layout */
.slide-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 0 28px 52px;
}
.slide-content.bottom { justify-content: flex-end; }
.slide-content.center { justify-content: center; align-items: center; text-align: center; }
.slide-content.space-between { justify-content: space-between; }
```

### Badge/Etiqueta de categoría

```html
<!-- Template A / B (borde cian) -->
<div style="position:absolute;top:28px;left:28px;display:inline-flex;align-items:center;
  padding:6px 12px;background:#1C1C28;border:1.5px solid #00E5CC;border-radius:6px;">
  <span style="font-family:'DM Sans',sans-serif;font-size:10px;font-weight:500;
    color:#00E5CC;letter-spacing:1.5px;text-transform:uppercase;">EDUCACIÓN IA</span>
</div>

<!-- Template C (borde violeta) -->
<div style="position:absolute;top:28px;left:28px;display:inline-flex;align-items:center;
  padding:6px 12px;background:#1C1C28;border:1.5px solid #7C3AED;border-radius:6px;">
  <span style="font-family:'DM Sans',sans-serif;font-size:10px;font-weight:500;
    color:#7C3AED;letter-spacing:1.5px;text-transform:uppercase;">CASO REAL</span>
</div>
```

### Numeración de slide (siempre top-right)

```html
<div style="position:absolute;top:30px;right:28px;">
  <span style="font-family:'DM Sans',sans-serif;font-size:10px;font-weight:400;color:#8888A8;">
    01 / 04
  </span>
</div>
```

### Línea cian decorativa (firma visual bajo el título)

```html
<div style="width:48px;height:3px;background:#00E5CC;border-radius:2px;margin:14px 0 16px;"></div>
```

### Título con palabra clave en cian

```html
<h2 style="font-family:'Syne',sans-serif;font-weight:800;font-size:30px;
  color:#F0F0F8;line-height:1.15;letter-spacing:-0.3px;">
  La IA no reemplaza a tu equipo.
  <span style="color:#00E5CC;">Automatiza</span> lo que les roba el tiempo.
</h2>
```

### Número grande (portada Template B)

```html
<div style="font-family:'Syne',sans-serif;font-weight:800;font-size:80px;
  color:#00E5CC;line-height:1;letter-spacing:-3px;">4</div>
<div style="font-family:'Syne',sans-serif;font-weight:800;font-size:26px;
  color:#F0F0F8;line-height:1.2;margin-top:4px;">pasos para que tu<br>negocio responda solo</div>
```

### Número protagonista (portada Template C)

```html
<div style="font-family:'Syne',sans-serif;font-weight:800;font-size:64px;
  color:#00E5CC;line-height:1;letter-spacing:-2px;">50 hrs</div>
<div style="font-family:'Syne',sans-serif;font-weight:700;font-size:20px;
  color:#F0F0F8;line-height:1.25;margin-top:6px;">recuperadas al mes</div>
```

### Número/dato estadístico destacado (slide interna)

```html
<div style="font-family:'Syne',sans-serif;font-weight:800;font-size:44px;
  color:#00E5CC;line-height:1;letter-spacing:-2px;">3h</div>
<div style="font-family:'Syne',sans-serif;font-weight:700;font-size:18px;
  color:#F0F0F8;line-height:1.3;margin-top:4px;">promedio diario en tareas repetitivas</div>
```

### Círculo de paso (Template B)

```html
<div style="width:36px;height:36px;border-radius:50%;background:#111118;
  border:1.5px solid #00E5CC;display:flex;align-items:center;justify-content:center;
  flex-shrink:0;">
  <span style="font-family:'Syne',sans-serif;font-weight:800;font-size:16px;color:#00E5CC;">1</span>
</div>
```

### Texto cuerpo / descripción

```html
<p style="font-family:'DM Sans',sans-serif;font-size:13px;font-weight:400;
  color:#F0F0F8;line-height:1.55;">
  Responder los mismos mensajes. Confirmar citas a mano. Enviar recordatorios uno por uno.
  Eso lo puede hacer una máquina.
</p>
```

### Lista con puntos cian

```html
<ul style="list-style:none;padding:0;margin-top:12px;display:flex;flex-direction:column;gap:10px;">
  <li style="display:flex;align-items:flex-start;gap:10px;">
    <div style="width:8px;height:8px;border-radius:50%;background:#00E5CC;
      flex-shrink:0;margin-top:4px;"></div>
    <span style="font-family:'DM Sans',sans-serif;font-size:13px;color:#F0F0F8;line-height:1.5;">
      Análisis de tu operación actual
    </span>
  </li>
</ul>
```

### Caja dato/métrica (Template B, slide de paso)

```html
<div style="background:#1C1C28;border-radius:6px;padding:10px 14px;margin-top:12px;
  display:inline-block;">
  <span style="font-family:'DM Sans',sans-serif;font-size:11px;color:#8888A8;">
    Duración: 30 minutos
  </span>
</div>
```

### Bloque ANTES / DESPUÉS (Template C)

```html
<div style="margin-bottom:14px;">
  <span style="font-family:'DM Sans',sans-serif;font-size:10px;font-weight:500;
    color:#8888A8;letter-spacing:1.5px;text-transform:uppercase;display:block;margin-bottom:8px;">
    ANTES
  </span>
  <p style="font-family:'DM Sans',sans-serif;font-size:13px;color:#F0F0F8;line-height:1.5;">
    2.5 horas/día contestando mensajes, confirmando citas...
  </p>
</div>

<div style="width:48px;height:3px;background:#00E5CC;border-radius:2px;margin:14px 0;"></div>

<div>
  <span style="font-family:'DM Sans',sans-serif;font-size:10px;font-weight:500;
    color:#00E5CC;letter-spacing:1.5px;text-transform:uppercase;display:block;margin-bottom:8px;">
    DESPUÉS
  </span>
  <p style="font-family:'DM Sans',sans-serif;font-size:13px;color:#F0F0F8;line-height:1.5;">
    El bot responde en segundos, agenda en el calendario...
  </p>
</div>
```

### Quote de cliente (Template C — solo si testimonio real)

```html
<div style="border-left:3px solid #7C3AED;background:#1C1C28;padding:12px 16px;
  border-radius:0 6px 6px 0;margin-top:14px;">
  <p style="font-family:'DM Sans',sans-serif;font-size:12px;font-style:italic;
    color:#8888A8;line-height:1.5;">
    "Con el bot respondemos el doble de clientes sin contratar más personal."
  </p>
  <p style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:500;
    color:#F0F0F8;margin-top:6px;">— Nombre del cliente, Empresa</p>
</div>
```

### CTA Box — Template A / B (cian)

```html
<div style="background:rgba(0,229,204,0.12);border:1px solid #00E5CC;border-radius:8px;
  padding:20px 24px;text-align:center;margin:0 auto;width:100%;">
  <p style="font-family:'Syne',sans-serif;font-weight:700;font-size:18px;
    color:#F0F0F8;line-height:1.3;">¿Cuántas horas recuperarías tú?</p>
  <p style="font-family:'DM Sans',sans-serif;font-size:12px;color:#8888A8;margin-top:8px;">
    Diagnóstico gratuito en ryventis.mx
  </p>
</div>
```

### CTA Box — Template C (violeta)

```html
<div style="background:rgba(124,58,237,0.12);border:1px solid #7C3AED;border-radius:8px;
  padding:20px 24px;text-align:center;margin:0 auto;width:100%;">
  <p style="font-family:'Syne',sans-serif;font-weight:700;font-size:18px;
    color:#F0F0F8;line-height:1.3;">¿Quieres este resultado?</p>
  <p style="font-family:'DM Sans',sans-serif;font-size:12px;color:#8888A8;margin-top:8px;">
    Diagnóstico gratuito en ryventis.mx
  </p>
</div>
```

### Logo Ryventis (siempre en bottom-left, TODAS las slides)

```html
<div style="position:absolute;bottom:20px;left:28px;display:flex;align-items:center;gap:8px;">
  <div style="width:24px;height:24px;border-radius:50%;
    background:linear-gradient(135deg,#00E5CC,#7C3AED);
    display:flex;align-items:center;justify-content:center;">
    <span style="font-family:'Syne',sans-serif;font-weight:800;font-size:11px;color:#0A0A0F;">R</span>
  </div>
  <span style="font-family:'DM Sans',sans-serif;font-size:10px;font-weight:500;
    color:#8888A8;letter-spacing:0.5px;">ryventisia</span>
</div>
```

### Progress Bar (bottom de cada slide)

```html
<!-- Variable: progress = ((slideIndex+1)/total)*100 -->
<div style="position:absolute;bottom:0;left:0;right:0;padding:10px 28px 16px;
  display:flex;align-items:center;gap:8px;z-index:10;">
  <div style="flex:1;height:2px;background:rgba(255,255,255,0.1);border-radius:1px;overflow:hidden;">
    <div style="height:100%;width:14.28%;background:#00E5CC;border-radius:1px;"></div>
  </div>
</div>
```

### Swipe Arrow (right edge — todas menos la última)

```html
<div style="position:absolute;right:0;top:0;bottom:0;width:40px;z-index:9;
  display:flex;align-items:center;justify-content:center;
  background:linear-gradient(to right,transparent,rgba(255,255,255,0.05));">
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
    <path d="M9 6l6 6-6 6" stroke="rgba(255,255,255,0.3)" stroke-width="2.5"
      stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
```

---

## BLOQUE 5 — INSTAGRAM FRAME WRAPPER

El frame de IG tiene fondo oscuro (`#0A0A0F`) para mantener coherencia con el look Ryventis.

```html
<!-- IG Header -->
<div style="display:flex;align-items:center;gap:10px;padding:11px 14px;
  border-bottom:1px solid #1C1C28;background:#0A0A0F;">
  <div style="width:34px;height:34px;border-radius:50%;
    background:linear-gradient(135deg,#00E5CC,#7C3AED);
    display:flex;align-items:center;justify-content:center;">
    <span style="font-family:'Syne',sans-serif;font-weight:800;font-size:13px;color:#0A0A0F;">R</span>
  </div>
  <div style="display:flex;flex-direction:column;">
    <span style="font-family:'DM Sans',sans-serif;font-weight:600;font-size:13px;color:#F0F0F8;">ryventisia</span>
    <span style="font-family:'DM Sans',sans-serif;font-size:11px;color:#8888A8;">Ryventis Solutions</span>
  </div>
  <span style="margin-left:auto;font-size:18px;color:#8888A8;letter-spacing:2px;">···</span>
</div>
```

---

## BLOQUE 6 — REGLAS DE GENERACIÓN

### Antes de escribir el HTML

1. **Determinar el template** (A / B / C) según el tipo de contenido
2. **Contar los slides** (A=4, B=5, C=3 — pueden variar entre 3 y 6)
3. **Preparar los textos** siguiendo los posts del BRIEF_FEED_VISUAL.md si son del grid de lanzamiento
4. **Aplicar la proporción de color** (70% negro, 20% blanco, 8% cian, 2% gris)
5. **Verificar**: nunca fondos blancos ni grises claros en ningún slide

### Reglas duras que nunca se rompen

- Fondos: solo `#0A0A0F`, `#111118`, gradiente `#1C1C28→#0A0A0F`. Nunca blanco ni gris claro.
- Fuentes: solo Syne + DM Sans. Sin excepciones.
- Cian máx. 10% del área visual por slide.
- Violeta solo en Template C.
- Logo Ryventis en el 100% de las slides. Sin excepción.
- Numeración de slide en esquina superior derecha de cada slide.
- Padding mínimo 28px desde todos los bordes.
- No inventar citas de clientes.
- El CTA solo va en la slide final de cada carrusel.

---

## BLOQUE 7 — SCRIPT DE EXPORTACIÓN

```python
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT_HTML   = Path("/path/to/carousel.html")
OUTPUT_DIR   = Path("/sessions/adoring-kind-cray/mnt/Carrusel/slides_[nombre]")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TOTAL_SLIDES = 4    # Actualizar según el carrusel
VIEW_W = 420
VIEW_H = 525
SCALE  = 1080 / 420   # 2.5714...

async def export_slides():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": VIEW_W, "height": VIEW_H},
            device_scale_factor=SCALE,
        )

        html_content = INPUT_HTML.read_text(encoding="utf-8")
        await page.set_content(html_content, wait_until="networkidle")
        await page.wait_for_timeout(3000)   # esperar Syne + DM Sans de Google Fonts

        # Ocultar chrome del IG frame, aislar viewport 420×525
        await page.evaluate("""() => {
            document.querySelectorAll('.ig-header,.ig-dots,.ig-actions,.ig-caption,.ig-time')
                .forEach(el => el.style.display = 'none');
            const frame = document.querySelector('.ig-frame');
            frame.style.cssText = 'width:420px;height:525px;max-width:none;border-radius:0;box-shadow:none;overflow:hidden;margin:0;';
            const vp = document.querySelector('.carousel-viewport');
            vp.style.cssText = 'width:420px;height:525px;aspect-ratio:unset;overflow:hidden;cursor:default;';
            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;background:#0A0A0F;';
        }""")

        await page.wait_for_timeout(500)

        for i in range(TOTAL_SLIDES):
            await page.evaluate("""(idx) => {
                const track = document.querySelector('.carousel-track');
                track.style.transition = 'none';
                track.style.transform  = 'translateX(' + (-idx * 420) + 'px)';
            }""", i)
            await page.wait_for_timeout(400)

            out_path = OUTPUT_DIR / f"slide_{i+1:02d}.png"
            await page.screenshot(
                path=str(out_path),
                clip={"x": 0, "y": 0, "width": VIEW_W, "height": VIEW_H},
            )
            print(f"  ✓ Slide {i+1}/{TOTAL_SLIDES} → {out_path.name}")

        await browser.close()

asyncio.run(export_slides())
```

**Errores comunes a evitar:**
- No usar shell scripts para generar HTML (interpola variables $)
- No cambiar el viewport a 1080px (rompe el layout)
- No saltarse el `wait_for_timeout(3000)` (los slides salen con tipografía fallback)

---

## BLOQUE 8 — GRID DE LANZAMIENTO (referencia rápida)

Para los 9 posts del grid inicial, usa exactamente el contenido de `BRIEF_FEED_VISUAL.md` (Bloque 3).

| Post | Template | Fondo portada | Badge | Tema |
|------|----------|---------------|-------|------|
| 1 | A | `#0A0A0F` | EDUCACIÓN IA | La IA no reemplaza tu equipo |
| 2 | B | `#111118` | EN 4 PASOS | 4 pasos para responder solo |
| 3 | C | gradiente | CASO REAL | 50 hrs recuperadas al mes |
| 4 | A | `#111118` | DATO DEL DÍA | 3 preguntas antes de contratar IA |
| 5 | B | `#111118` | CÓMO FUNCIONA | 72 horas de implementación |
| 6 | C | gradiente | RESULTADO | 72 hrs de implementación |
| 7 | A | `#0A0A0F` | ¿SABÍAS QUE? | La IA no es cara, el tiempo sí |
| 8 | B | `#111118` | EL PROCESO | 3 cosas en un diagnóstico |
| 9 | C | gradiente | DIAGNÓSTICO GRATIS | 60 min que cambian tu negocio |

Ver `BRIEF_FEED_VISUAL.md` → Bloque 3 para el contenido completo de cada slide de cada post.

---

## FLUJO COMPLETO DE TRABAJO

Cuando el usuario pide un carrusel de Ryventis:

```
1. Leer este CLAUDE.md
2. Identificar template (A/B/C) según tipo de contenido
3. Si es un post del grid de lanzamiento → leer BRIEF_FEED_VISUAL.md para el contenido exacto
4. Generar el HTML completo siguiendo:
   - CSS de este documento (Syne + DM Sans, variables de color)
   - Estructura de slides del template correspondiente
   - Componentes HTML de este documento
5. Guardar en /sessions/adoring-kind-cray/ como carousel_[nombre].html
6. Ejecutar script Playwright → guardar PNGs en Carrusel/slides_[nombre]/
7. Verificar visualmente cada slide (Read para cada PNG)
8. Copiar HTML final a Carrusel/ para entrega
```

---

*Sistema integrado por Claude · Basado en design_system.json + BRIEF_FEED_VISUAL.md*  
*Ryventis Solutions · @ryventisia · ryventis.mx*
