const pptxgen = require("pptxgenjs");

const OUT_PATH = "C:/Agencia Ryventis Solutions/Contenido/informacion_para_presentacion_a_clientes/Presentacion_Venta_IA_Ryventis.pptx";

// Colors (no # prefix per pptxgenjs rules)
const C = {
  bg: "0A0A0F",
  surface: "111118",
  card: "1C1C28",
  cyan: "00E5CC",
  cyanDark: "00B8A3",
  violet: "7C3AED",
  white: "F0F0F8",
  gray: "8888A8",
  red: "E53E3E",
};

const makeShadow = () => ({ type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.35 });

let pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "Ryventis Solutions — Presentación de Ventas";
pres.author = "Ryventis Solutions";

// ─────────────────────────────────────────────────
// SLIDE 1: PORTADA
// ─────────────────────────────────────────────────
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Left cyan accent bar
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 0.06, h: 5.625, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 } });

  // Top right violet accent block
  s.addShape(pres.shapes.RECTANGLE, { x: 8.5, y: 0, w: 1.5, h: 0.06, fill: { color: C.violet }, line: { color: C.violet, width: 0 } });

  // Decorative large circle (background)
  s.addShape(pres.shapes.OVAL, { x: 6.5, y: -1.5, w: 5, h: 5, fill: { color: C.violet, transparency: 85 }, line: { color: C.violet, width: 0 } });
  s.addShape(pres.shapes.OVAL, { x: 7.2, y: -0.8, w: 3.5, h: 3.5, fill: { color: C.cyan, transparency: 90 }, line: { color: C.cyan, width: 0 } });

  // RYVENTIS logo text
  s.addText("RYVENTIS", {
    x: 0.45, y: 0.45, w: 5, h: 0.65,
    fontSize: 28, bold: true, color: C.cyan,
    fontFace: "Arial Black", charSpacing: 8, margin: 0,
  });

  // Tagline below logo
  s.addText("Tecnología que trabaja para ti", {
    x: 0.45, y: 1.08, w: 6, h: 0.35,
    fontSize: 10, color: C.gray, fontFace: "Arial", italic: true, margin: 0,
  });

  // Horizontal divider
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 1.52, w: 4.5, h: 0.025, fill: { color: C.cyan, transparency: 30 }, line: { color: C.cyan, width: 0 } });

  // Main headline
  s.addText("Tu negocio,\ntrabajando solo.", {
    x: 0.45, y: 1.75, w: 6.8, h: 2.3,
    fontSize: 48, bold: true, color: C.white, fontFace: "Arial Black",
    lineSpacingMultiple: 1.1, margin: 0,
  });

  // Subtitle
  s.addText("Automatización con IA para PYMEs en Puebla", {
    x: 0.45, y: 4.0, w: 7, h: 0.55,
    fontSize: 16, color: C.gray, fontFace: "Arial", margin: 0,
  });

  // Bottom cyan CTA bar
  s.addShape(pres.shapes.RECTANGLE, { x: 0.45, y: 4.8, w: 2.4, h: 0.5, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 }, shadow: makeShadow() });
  s.addText("Conoce más →", {
    x: 0.45, y: 4.8, w: 2.4, h: 0.5,
    fontSize: 13, bold: true, color: C.bg, fontFace: "Arial", align: "center", valign: "middle", margin: 0,
  });
}

// ─────────────────────────────────────────────────
// SLIDE 2: EL PROBLEMA
// ─────────────────────────────────────────────────
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Top accent bar
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.055, fill: { color: C.red }, line: { color: C.red, width: 0 } });

  // Section label
  s.addText("EL PROBLEMA", {
    x: 0.5, y: 0.22, w: 3, h: 0.3,
    fontSize: 9, bold: true, color: C.red, fontFace: "Arial", charSpacing: 4, margin: 0,
  });

  // Title
  s.addText("¿Cuántas ventas pierdes\nmientras duermes?", {
    x: 0.5, y: 0.6, w: 9, h: 1.5,
    fontSize: 36, bold: true, color: C.white, fontFace: "Arial Black",
    lineSpacingMultiple: 1.15, margin: 0,
  });

  // 3 pain point cards
  const problems = [
    {
      icon: "70%",
      title: "Leads perdidos sin respuesta",
      body: "El 70% de los prospectos no reciben respuesta en los primeros 5 minutos — y se van con la competencia.",
    },
    {
      icon: "4h",
      title: "Horas perdidas en tareas repetitivas",
      body: "Tu equipo gasta 3-4 horas diarias respondiendo las mismas preguntas de precio, horario y ubicación.",
    },
    {
      icon: "$$$",
      title: "Sin seguimiento = dinero perdido",
      body: "Sin automatización de seguimiento, el 80% de los prospectos nunca reciben un segundo contacto.",
    },
  ];

  problems.forEach((p, i) => {
    const x = 0.3 + i * 3.25;
    const y = 2.35;
    const w = 3.0;
    const h = 2.75;

    // Card bg
    s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: C.card }, line: { color: C.violet, width: 1 }, shadow: makeShadow() });

    // Top accent
    s.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 0.05, fill: { color: C.red }, line: { color: C.red, width: 0 } });

    // Big stat
    s.addText(p.icon, {
      x: x + 0.18, y: y + 0.18, w: w - 0.36, h: 0.75,
      fontSize: 38, bold: true, color: C.red, fontFace: "Arial Black", align: "left", margin: 0,
    });

    // Title
    s.addText(p.title, {
      x: x + 0.18, y: y + 0.95, w: w - 0.36, h: 0.55,
      fontSize: 13, bold: true, color: C.cyan, fontFace: "Arial", margin: 0,
    });

    // Body
    s.addText(p.body, {
      x: x + 0.18, y: y + 1.55, w: w - 0.36, h: 1.1,
      fontSize: 11, color: C.white, fontFace: "Arial", lineSpacingMultiple: 1.3, margin: 0,
    });
  });

  // Footer tag
  s.addText("ryventis.mx", { x: 8.8, y: 5.35, w: 1.1, h: 0.22, fontSize: 8, color: C.gray, fontFace: "Arial", align: "right", margin: 0 });
}

// ─────────────────────────────────────────────────
// SLIDE 3: LA SOLUCIÓN
// ─────────────────────────────────────────────────
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Left panel (cyan)
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 3.6, h: 5.625, fill: { color: C.cyan, transparency: 8 }, line: { color: C.cyan, width: 0 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 3.55, y: 0, w: 0.05, h: 5.625, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 } });

  // Left panel content
  s.addText("LA\nSOLUCIÓN", {
    x: 0.3, y: 0.5, w: 3.0, h: 2.2,
    fontSize: 52, bold: true, color: C.bg, fontFace: "Arial Black",
    lineSpacingMultiple: 1.0, margin: 0,
  });

  s.addText("IA que trabaja\n24/7, sin descanso", {
    x: 0.3, y: 2.75, w: 3.1, h: 1.6,
    fontSize: 16, bold: true, color: C.bg, fontFace: "Arial",
    lineSpacingMultiple: 1.3, margin: 0,
  });

  s.addShape(pres.shapes.RECTANGLE, { x: 0.3, y: 4.55, w: 2.8, h: 0.45, fill: { color: C.bg, transparency: 20 }, line: { color: C.bg, width: 0 } });
  s.addText("Implementación en < 72 horas", {
    x: 0.3, y: 4.55, w: 2.8, h: 0.45,
    fontSize: 10, bold: true, color: C.bg, fontFace: "Arial", align: "center", valign: "middle", margin: 0,
  });

  // Right panel solutions
  const solutions = [
    {
      num: "01",
      title: "Chatbot Inteligente en WhatsApp",
      body: "Agenda citas, califica leads y responde dudas en segundos — sin intervención humana, 24/7.",
    },
    {
      num: "02",
      title: "Automatización de Procesos",
      body: "Elimina tareas repetitivas: cotizaciones, recordatorios y reportes automáticos sin esfuerzo.",
    },
    {
      num: "03",
      title: "Agente Autónomo de Ventas",
      body: "Da seguimiento a cada prospecto hasta cerrar la venta. Nunca más un lead olvidado.",
    },
  ];

  solutions.forEach((sol, i) => {
    const x = 3.9;
    const y = 0.45 + i * 1.7;

    // Number badge
    s.addShape(pres.shapes.OVAL, { x, y: y + 0.05, w: 0.55, h: 0.55, fill: { color: C.violet }, line: { color: C.violet, width: 0 } });
    s.addText(sol.num, { x, y: y + 0.05, w: 0.55, h: 0.55, fontSize: 14, bold: true, color: C.white, fontFace: "Arial Black", align: "center", valign: "middle", margin: 0 });

    // Title
    s.addText(sol.title, {
      x: x + 0.7, y, w: 5.3, h: 0.45,
      fontSize: 15, bold: true, color: C.cyan, fontFace: "Arial", margin: 0,
    });

    // Body
    s.addText(sol.body, {
      x: x + 0.7, y: y + 0.45, w: 5.3, h: 0.9,
      fontSize: 12, color: C.white, fontFace: "Arial", lineSpacingMultiple: 1.3, margin: 0,
    });

    // Divider (except last)
    if (i < 2) {
      s.addShape(pres.shapes.RECTANGLE, { x: 3.9, y: y + 1.55, w: 5.9, h: 0.012, fill: { color: C.gray, transparency: 60 }, line: { color: C.gray, width: 0 } });
    }
  });

  s.addText("ryventis.mx", { x: 8.8, y: 5.35, w: 1.1, h: 0.22, fontSize: 8, color: C.gray, fontFace: "Arial", align: "right", margin: 0 });
}

// ─────────────────────────────────────────────────
// SLIDE 4: IMPACTO REAL (Métricas)
// ─────────────────────────────────────────────────
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Top bar
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 10, h: 0.055, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 } });

  // Section label
  s.addText("IMPACTO REAL", {
    x: 0.5, y: 0.22, w: 4, h: 0.3,
    fontSize: 9, bold: true, color: C.cyan, fontFace: "Arial", charSpacing: 4, margin: 0,
  });

  // Title
  s.addText("Resultados medibles desde el día 1", {
    x: 0.5, y: 0.62, w: 9, h: 0.85,
    fontSize: 30, bold: true, color: C.white, fontFace: "Arial Black", margin: 0,
  });

  // Table header
  const tableX = 0.5, tableY = 1.65, tableW = 9, colW = [3.8, 2.4, 2.7];
  const headerH = 0.5;

  // Header bg
  s.addShape(pres.shapes.RECTANGLE, { x: tableX, y: tableY, w: tableW, h: headerH, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 } });
  const headers = ["Métrica", "Sin Ryventis", "Con Ryventis"];
  let hx = tableX;
  headers.forEach((h, i) => {
    s.addText(h, { x: hx + 0.1, y: tableY, w: colW[i] - 0.1, h: headerH, fontSize: 13, bold: true, color: C.bg, fontFace: "Arial", valign: "middle", margin: 0 });
    hx += colW[i];
  });

  // Table rows
  const rows = [
    ["Tiempo de respuesta", "2 - 24 horas", "< 30 segundos"],
    ["Tasa de abandono de leads", "65%", "12%"],
    ["Horas/mes en tareas repetitivas", "45 horas", "5 horas"],
    ["Conversión de prospectos", "3.5%", "18 - 25%"],
  ];

  rows.forEach((row, ri) => {
    const ry = tableY + headerH + ri * 0.72;
    const rowFill = ri % 2 === 0 ? C.surface : C.card;

    s.addShape(pres.shapes.RECTANGLE, { x: tableX, y: ry, w: tableW, h: 0.72, fill: { color: rowFill }, line: { color: rowFill, width: 0 } });

    let rx = tableX;
    row.forEach((cell, ci) => {
      const isGood = ci === 2;
      const isBad = ci === 1;
      s.addText(cell, {
        x: rx + 0.12, y: ry, w: colW[ci] - 0.12, h: 0.72,
        fontSize: 13, bold: ci > 0, color: isGood ? C.cyan : isBad ? "E57373" : C.white,
        fontFace: "Arial", valign: "middle", margin: 0,
      });
      rx += colW[ci];
    });
  });

  // Bottom call-out
  s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 5.0, w: 9, h: 0.4, fill: { color: C.violet, transparency: 25 }, line: { color: C.violet, width: 1 } });
  s.addText("ROI promedio: recuperas tu inversión en menos de 90 días  ✓", {
    x: 0.5, y: 5.0, w: 9, h: 0.4,
    fontSize: 12, bold: true, color: C.white, fontFace: "Arial", align: "center", valign: "middle", margin: 0,
  });
}

// ─────────────────────────────────────────────────
// SLIDE 5: CTA — DIAGNÓSTICO GRATUITO
// ─────────────────────────────────────────────────
{
  let s = pres.addSlide();
  s.background = { color: C.bg };

  // Full background accent shapes
  s.addShape(pres.shapes.OVAL, { x: -1, y: 2.5, w: 5, h: 5, fill: { color: C.cyan, transparency: 90 }, line: { color: C.cyan, width: 0 } });
  s.addShape(pres.shapes.OVAL, { x: 7, y: -2, w: 6, h: 6, fill: { color: C.violet, transparency: 85 }, line: { color: C.violet, width: 0 } });

  // Center card
  const cx = 1.5, cy = 0.7, cw = 7, ch = 4.0;
  s.addShape(pres.shapes.RECTANGLE, { x: cx, y: cy, w: cw, h: ch, fill: { color: C.surface }, line: { color: C.cyan, width: 1.5 }, shadow: makeShadow() });

  // Top cyan bar on card
  s.addShape(pres.shapes.RECTANGLE, { x: cx, y: cy, w: cw, h: 0.06, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 } });

  // GRATIS badge
  s.addShape(pres.shapes.RECTANGLE, { x: 3.7, y: cy + 0.25, w: 2.6, h: 0.45, fill: { color: C.violet }, line: { color: C.violet, width: 0 } });
  s.addText("COMPLETAMENTE GRATUITO", {
    x: 3.7, y: cy + 0.25, w: 2.6, h: 0.45,
    fontSize: 9, bold: true, color: C.white, fontFace: "Arial", align: "center", valign: "middle", charSpacing: 1, margin: 0,
  });

  // Headline
  s.addText("Diagnóstico gratuito\nen 60 minutos", {
    x: cx + 0.35, y: cy + 0.85, w: cw - 0.7, h: 1.5,
    fontSize: 34, bold: true, color: C.white, fontFace: "Arial Black",
    lineSpacingMultiple: 1.1, align: "center", margin: 0,
  });

  // Subtitle
  s.addText("Sin costo. Sin compromisos. Solo claridad sobre qué automatizar primero.", {
    x: cx + 0.35, y: cy + 2.35, w: cw - 0.7, h: 0.55,
    fontSize: 13, color: C.gray, fontFace: "Arial", align: "center", margin: 0,
  });

  // CTA Button
  s.addShape(pres.shapes.RECTANGLE, { x: 3.25, y: cy + 3.05, w: 3.5, h: 0.6, fill: { color: C.cyan }, line: { color: C.cyan, width: 0 }, shadow: makeShadow() });
  s.addText("Agenda tu sesión hoy →", {
    x: 3.25, y: cy + 3.05, w: 3.5, h: 0.6,
    fontSize: 14, bold: true, color: C.bg, fontFace: "Arial", align: "center", valign: "middle", margin: 0,
  });

  // Contact info below card
  s.addText("ryventis.solutions@gmail.com   |   ryventis.mx", {
    x: 1.5, y: 5.05, w: 7, h: 0.35,
    fontSize: 10, color: C.gray, fontFace: "Arial", align: "center", margin: 0,
  });

  // Logo bottom right
  s.addText("RYVENTIS", {
    x: 7.8, y: 5.25, w: 2.1, h: 0.3,
    fontSize: 11, bold: true, color: C.cyan, fontFace: "Arial Black", charSpacing: 3, align: "right", margin: 0,
  });
}

// Write file
pres.writeFile({ fileName: OUT_PATH })
  .then(() => console.log("✅ Archivo generado: " + OUT_PATH))
  .catch(err => { console.error("❌ Error:", err); process.exit(1); });
