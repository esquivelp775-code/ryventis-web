from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUT = "C:/Agencia Ryventis Solutions/Contenido/informacion_para_presentacion_a_clientes/Reporte_Impacto_IA_Ryventis.pdf"

# ── Colors ──────────────────────────────────────────────────
CYAN    = colors.HexColor("#00E5CC")
VIOLET  = colors.HexColor("#7C3AED")
DARK    = colors.HexColor("#1A1A2E")
WHITE   = colors.white
LIGHT_BG= colors.HexColor("#F8F9FA")
GRAY    = colors.HexColor("#6B7280")
CYAN_BG = colors.HexColor("#E0FBF8")
VIOLET_BG = colors.HexColor("#F3EEFF")
RED_SOFT  = colors.HexColor("#FEE2E2")
GREEN_SOFT= colors.HexColor("#D1FAE5")

W, H = A4  # 595.27 x 841.89 pts

# ── Styles ───────────────────────────────────────────────────
def make_styles():
    s = {}

    s["cover_logo"] = ParagraphStyle("cover_logo",
        fontName="Helvetica-Bold", fontSize=32, textColor=CYAN,
        alignment=TA_CENTER, spaceAfter=4, leading=36)

    s["cover_tagline"] = ParagraphStyle("cover_tagline",
        fontName="Helvetica-Oblique", fontSize=12, textColor=GRAY,
        alignment=TA_CENTER, spaceAfter=40)

    s["cover_title"] = ParagraphStyle("cover_title",
        fontName="Helvetica-Bold", fontSize=22, textColor=DARK,
        alignment=TA_CENTER, spaceAfter=10, leading=28)

    s["cover_subtitle"] = ParagraphStyle("cover_subtitle",
        fontName="Helvetica", fontSize=13, textColor=GRAY,
        alignment=TA_CENTER, spaceAfter=8)

    s["cover_prep"] = ParagraphStyle("cover_prep",
        fontName="Helvetica", fontSize=10, textColor=GRAY,
        alignment=TA_CENTER, spaceAfter=0)

    s["section_label"] = ParagraphStyle("section_label",
        fontName="Helvetica-Bold", fontSize=9, textColor=CYAN,
        spaceAfter=4, spaceBefore=18, leading=11)

    s["section_title"] = ParagraphStyle("section_title",
        fontName="Helvetica-Bold", fontSize=18, textColor=DARK,
        spaceAfter=10, spaceBefore=2, leading=22)

    s["body"] = ParagraphStyle("body",
        fontName="Helvetica", fontSize=10.5, textColor=DARK,
        spaceAfter=8, leading=16)

    s["bullet"] = ParagraphStyle("bullet",
        fontName="Helvetica", fontSize=10.5, textColor=DARK,
        spaceAfter=5, leading=16, leftIndent=14, firstLineIndent=-14)

    s["highlight"] = ParagraphStyle("highlight",
        fontName="Helvetica-Bold", fontSize=11, textColor=DARK,
        spaceAfter=6, leading=16)

    s["stat_big"] = ParagraphStyle("stat_big",
        fontName="Helvetica-Bold", fontSize=38, textColor=CYAN,
        alignment=TA_CENTER, spaceAfter=2, leading=42)

    s["stat_label"] = ParagraphStyle("stat_label",
        fontName="Helvetica", fontSize=9, textColor=GRAY,
        alignment=TA_CENTER, spaceAfter=0)

    s["callout_title"] = ParagraphStyle("callout_title",
        fontName="Helvetica-Bold", fontSize=12, textColor=WHITE,
        spaceAfter=4, leading=15)

    s["callout_body"] = ParagraphStyle("callout_body",
        fontName="Helvetica", fontSize=10, textColor=WHITE,
        spaceAfter=0, leading=14)

    s["cta_title"] = ParagraphStyle("cta_title",
        fontName="Helvetica-Bold", fontSize=20, textColor=DARK,
        alignment=TA_CENTER, spaceAfter=10, leading=24)

    s["cta_body"] = ParagraphStyle("cta_body",
        fontName="Helvetica", fontSize=11, textColor=GRAY,
        alignment=TA_CENTER, spaceAfter=6, leading=16)

    s["footer"] = ParagraphStyle("footer",
        fontName="Helvetica", fontSize=8, textColor=GRAY,
        alignment=TA_CENTER)

    s["table_header"] = ParagraphStyle("table_header",
        fontName="Helvetica-Bold", fontSize=10, textColor=WHITE)

    s["table_cell"] = ParagraphStyle("table_cell",
        fontName="Helvetica", fontSize=10, textColor=DARK)

    s["table_cell_good"] = ParagraphStyle("table_cell_good",
        fontName="Helvetica-Bold", fontSize=10, textColor=colors.HexColor("#059669"))

    s["table_cell_bad"] = ParagraphStyle("table_cell_bad",
        fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#DC2626"))

    s["sector_title"] = ParagraphStyle("sector_title",
        fontName="Helvetica-Bold", fontSize=12, textColor=VIOLET,
        spaceAfter=4, leading=15)

    s["sector_row"] = ParagraphStyle("sector_row",
        fontName="Helvetica", fontSize=10, textColor=DARK,
        spaceAfter=3, leading=14, leftIndent=10)

    return s

# ── Header / Footer canvas callbacks ─────────────────────────
def draw_header(canvas, doc):
    canvas.saveState()
    # Top cyan bar
    canvas.setFillColor(CYAN)
    canvas.rect(0, H - 8, W, 8, fill=1, stroke=0)
    # Logo text top left
    canvas.setFillColor(DARK)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(20*mm, H - 6*mm, "RYVENTIS SOLUTIONS")
    # Page number top right
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY)
    canvas.drawRightString(W - 20*mm, H - 6*mm, f"Pág. {doc.page}")
    canvas.restoreState()

def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#E5E7EB"))
    canvas.rect(0, 0, W, 10*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(W/2, 3.5*mm, "© 2026 Ryventis Solutions — Puebla, México  |  ryventis.mx  |  Tecnología que trabaja para ti")
    canvas.restoreState()

def draw_page(canvas, doc):
    draw_header(canvas, doc)
    draw_footer(canvas, doc)

def draw_cover_page(canvas, doc):
    canvas.saveState()
    # Full cyan top block
    canvas.setFillColor(CYAN)
    canvas.rect(0, H - 90*mm, W, 90*mm, fill=1, stroke=0)
    # Violet accent strip
    canvas.setFillColor(VIOLET)
    canvas.rect(0, H - 93*mm, W, 3*mm, fill=1, stroke=0)
    # Bottom footer bar
    canvas.setFillColor(DARK)
    canvas.rect(0, 0, W, 18*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(W/2, 6*mm, "© 2026 Ryventis Solutions — Puebla, México  |  ryventis.mx")
    canvas.restoreState()

# ── Helper: colored box flowable ─────────────────────────────
class ColorBox(Table):
    pass

def make_callout(text_title, text_body, bg_color, styles):
    data = [[
        Paragraph(text_title, styles["callout_title"]),
    ], [
        Paragraph(text_body, styles["callout_body"]),
    ]]
    t = Table(data, colWidths=[155*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg_color),
        ("ROUNDEDCORNERS", [6]),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (0,0), 10),
        ("BOTTOMPADDING", (0,-1), (-1,-1), 10),
        ("TOPPADDING", (0,1), (-1,-1), 2),
    ]))
    return t

def make_stat_row(stats, styles):
    cells = []
    for val, label in stats:
        inner = Table([
            [Paragraph(val, styles["stat_big"])],
            [Paragraph(label, styles["stat_label"])],
        ], colWidths=[47*mm])
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), CYAN_BG),
            ("LEFTPADDING", (0,0), (-1,-1), 6),
            ("RIGHTPADDING", (0,0), (-1,-1), 6),
            ("TOPPADDING", (0,0), (-1,-1), 10),
            ("BOTTOMPADDING", (0,-1), (-1,-1), 10),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ]))
        cells.append(inner)
    row = Table([cells], colWidths=[50*mm]*len(stats))
    row.setStyle(TableStyle([
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ]))
    return row

# ── Build document ────────────────────────────────────────────
def build():
    S = make_styles()

    # Two page templates: cover (no header/footer callbacks) and normal
    frame_cover = Frame(0, 0, W, H, leftPadding=25*mm, rightPadding=25*mm,
                        topPadding=100*mm, bottomPadding=22*mm)
    frame_normal = Frame(20*mm, 18*mm, W - 40*mm, H - 30*mm,
                         leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    cover_tpl  = PageTemplate(id="Cover",  frames=[frame_cover],  onPage=draw_cover_page)
    normal_tpl = PageTemplate(id="Normal", frames=[frame_normal], onPage=draw_page)

    doc = BaseDocTemplate(OUT, pagesize=A4, pageTemplates=[cover_tpl, normal_tpl])

    story = []

    # ── COVER ────────────────────────────────────────────────
    story.append(Paragraph("RYVENTIS SOLUTIONS", S["cover_logo"]))
    story.append(Paragraph("Tecnología que trabaja para ti", S["cover_tagline"]))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("Impacto de la Automatización con IA<br/>en la Mensajería Empresarial", S["cover_title"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Reporte Estratégico para PYMEs — Puebla, México 2026", S["cover_subtitle"]))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Preparado por: Ryventis Solutions  |  ryventis.mx", S["cover_prep"]))

    # Switch to normal template
    story.append(PageBreak())

    # ── SECTION 1 ─────────────────────────────────────────────
    story.append(Paragraph("SECCIÓN 1", S["section_label"]))
    story.append(Paragraph("El Panorama Actual de la Mensajería", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=12))

    story.append(make_stat_row([
        ("85%", "prefieren mensajería\nsobre llamada telefónica"),
        ("94%", "penetración de WhatsApp\nen smartphones en México"),
        ("5 min", "tiempo máximo de respuesta\nque el cliente acepta"),
    ], S))
    story.append(Spacer(1, 10*mm))

    story.append(Paragraph(
        "En 2026, el <b>85% de los clientes</b> prefieren comunicarse con empresas a través de canales de mensajería "
        "instantánea (WhatsApp, Instagram, Messenger) antes que por llamada telefónica.", S["body"]))
    story.append(Paragraph(
        "En México, WhatsApp tiene una penetración del <b>94%</b> entre usuarios de smartphone, "
        "convirtiéndolo en el canal de comunicación comercial más importante para PYMEs.", S["body"]))
    story.append(Spacer(1, 3*mm))
    story.append(make_callout(
        "El problema crítico",
        "La mayoría de las PYMEs operan su comunicación de forma manual, generando tiempos de respuesta "
        "de 2 a 24 horas — en un mercado donde el cliente espera respuesta en menos de 5 minutos.",
        DARK, S
    ))

    # ── SECTION 2 ─────────────────────────────────────────────
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("SECCIÓN 2", S["section_label"]))
    story.append(Paragraph("El Costo de la Espera (ROI)", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    # Conversion table
    header = [
        Paragraph("Tiempo de respuesta", S["table_header"]),
        Paragraph("Probabilidad de conversión", S["table_header"]),
    ]
    rows = [
        [Paragraph("Menos de 5 minutos", S["table_cell"]),  Paragraph("✓  100% (base)", S["table_cell_good"])],
        [Paragraph("Entre 5 y 30 minutos", S["table_cell"]), Paragraph("↓  60% menor", S["table_cell_bad"])],
        [Paragraph("Entre 30 min y 2 horas", S["table_cell"]),Paragraph("↓  85% menor", S["table_cell_bad"])],
        [Paragraph("Más de 2 horas", S["table_cell"]),       Paragraph("✗  95% menor — el lead ya se fue", S["table_cell_bad"])],
    ]
    conv_table = Table([header] + rows, colWidths=[80*mm, 75*mm])
    conv_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK),
        ("BACKGROUND", (0,1), (-1,1), GREEN_SOFT),
        ("BACKGROUND", (0,2), (-1,2), LIGHT_BG),
        ("BACKGROUND", (0,3), (-1,3), RED_SOFT),
        ("BACKGROUND", (0,4), (-1,4), RED_SOFT),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [GREEN_SOFT, LIGHT_BG, RED_SOFT, RED_SOFT]),
    ]))
    story.append(conv_table)
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph(
        "Un lead que no es contactado en los primeros 5 minutos tiene hasta <b>400% menos de probabilidades</b> "
        "de convertir. Para una PYME que recibe 50 leads al mes con ticket promedio de $5,000 MXN, "
        "responder tarde puede representar hasta <b>$150,000 MXN en ingresos perdidos</b> mensualmente.", S["body"]))

    # Loss formula box
    formula_data = [
        [Paragraph("Cálculo de pérdida mensual estimada", S["callout_title"])],
        [Paragraph(
            "• Leads mensuales: 50<br/>"
            "• Tasa de abandono por respuesta lenta: 65%<br/>"
            "• Leads perdidos: ~32 por mes<br/>"
            "• Ticket promedio: $5,000 MXN<br/>"
            "• <b>Pérdida mensual estimada: $160,000 MXN</b>",
            S["callout_body"])],
    ]
    fbox = Table(formula_data, colWidths=[155*mm])
    fbox.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), VIOLET),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING", (0,0), (0,0), 10),
        ("BOTTOMPADDING", (0,-1), (-1,-1), 12),
        ("TOPPADDING", (0,1), (-1,-1), 4),
    ]))
    story.append(fbox)

    # ── SECTION 3 ─────────────────────────────────────────────
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("SECCIÓN 3", S["section_label"]))
    story.append(Paragraph("Eficiencia Operativa: Horas Ahorradas", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    story.append(Paragraph(
        "Un empleado de atención al cliente promedio gasta el <b>60% de su tiempo</b> respondiendo preguntas de Nivel 1:", S["body"]))
    for q in ["¿Cuánto cuesta?", "¿Dónde están ubicados?", "¿Tienen citas disponibles?", "¿Cuáles son sus horarios?"]:
        story.append(Paragraph(f"• \"{q}\"", S["bullet"]))
    story.append(Spacer(1, 4*mm))

    # Hours impact table
    hours_rows = [
        [Paragraph("Indicador", S["table_header"]), Paragraph("Valor", S["table_header"])],
        [Paragraph("Horas/día en preguntas repetitivas (por empleado)", S["table_cell"]),
         Paragraph("3.5 horas", S["table_cell_bad"])],
        [Paragraph("Horas/mes", S["table_cell"]),
         Paragraph("77 horas", S["table_cell_bad"])],
        [Paragraph("Costo mensual de esas horas (salario $8,000 MXN/mes)", S["table_cell"]),
         Paragraph("~$3,850 MXN desperdiciados", S["table_cell_bad"])],
        [Paragraph("Con automatización Ryventis — horas/mes residuales", S["table_cell"]),
         Paragraph("< 10 horas  ✓", S["table_cell_good"])],
    ]
    h_table = Table(hours_rows, colWidths=[115*mm, 40*mm])
    h_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK),
        ("BACKGROUND", (0,1), (-1,1), LIGHT_BG),
        ("BACKGROUND", (0,2), (-1,2), colors.white),
        ("BACKGROUND", (0,3), (-1,3), LIGHT_BG),
        ("BACKGROUND", (0,4), (-1,4), GREEN_SOFT),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
    ]))
    story.append(h_table)

    # ── SECTION 4 ─────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("SECCIÓN 4", S["section_label"]))
    story.append(Paragraph("Tabla Comparativa: Sin Ryventis vs. Con Ryventis IA", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    comp_header = [
        Paragraph("Métrica", S["table_header"]),
        Paragraph("Sin Automatización", S["table_header"]),
        Paragraph("Con Ryventis IA", S["table_header"]),
    ]
    comp_rows = [
        ["Tiempo de respuesta", "2 - 24 horas", "< 30 segundos"],
        ["Tasa de abandono de leads", "65%", "12%"],
        ["Horas/mes en tareas repetitivas", "77 horas", "10 horas"],
        ["Conversión de prospectos", "3.5%", "18% - 25%"],
        ["Atención fuera de horario", "0%", "100%"],
        ["Costo de atención inicial por lead", "$85 MXN", "$4 MXN"],
        ["Seguimiento automático", "No", "Sí (24/7)"],
    ]
    comp_data = [comp_header]
    for i, row in enumerate(comp_rows):
        comp_data.append([
            Paragraph(row[0], S["table_cell"]),
            Paragraph(row[1], S["table_cell_bad"]),
            Paragraph(row[2], S["table_cell_good"]),
        ])

    comp_table = Table(comp_data, colWidths=[70*mm, 40*mm, 45*mm])
    row_colors = []
    for i in range(1, len(comp_data)):
        bg = LIGHT_BG if i % 2 == 0 else colors.white
        row_colors.append(("BACKGROUND", (0,i), (-1,i), bg))

    comp_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 9),
        ("BOTTOMPADDING", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("BACKGROUND", (2,1), (2,-1), GREEN_SOFT),
        ("BACKGROUND", (1,1), (1,-1), RED_SOFT),
    ] + row_colors))
    story.append(comp_table)

    # ── SECTION 5 ─────────────────────────────────────────────
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("SECCIÓN 5", S["section_label"]))
    story.append(Paragraph("Omnicanalidad Real", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    story.append(Paragraph(
        "Los clientes modernos no usan un solo canal. Saltan entre WhatsApp, Instagram DM, "
        "Facebook Messenger y formularios web — a veces en el mismo día.", S["body"]))
    story.append(Paragraph(
        "<b>Sin automatización:</b> cada canal requiere personal dedicado, generando inconsistencias "
        "en la respuesta y pérdida de contexto del cliente.", S["body"]))
    story.append(Paragraph(
        "<b>Con Ryventis:</b> un solo sistema integrado gestiona todos los canales con el mismo tono "
        "de marca, el mismo tiempo de respuesta, y memoria de cada conversación previa.", S["body"]))

    channels = [
        ("WhatsApp Business API", "Canal principal — 94% penetración en México"),
        ("Instagram Direct", "Para clientes captados por contenido orgánico"),
        ("Facebook Messenger", "Para leads desde Facebook Ads"),
        ("Web Chat", "Para visitantes del sitio web"),
    ]
    ch_data = [[
        Paragraph(f"<b>{ch}</b>", S["table_cell"]),
        Paragraph(desc, S["table_cell"]),
    ] for ch, desc in channels]
    ch_table = Table(ch_data, colWidths=[60*mm, 95*mm])
    ch_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (0,-1), CYAN_BG),
        ("BACKGROUND", (1,0), (1,-1), LIGHT_BG),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 9),
        ("BOTTOMPADDING", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [CYAN_BG, colors.white, CYAN_BG, colors.white]),
    ]))
    story.append(ch_table)

    # ── SECTION 6 ─────────────────────────────────────────────
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("SECCIÓN 6", S["section_label"]))
    story.append(Paragraph("Calificación Inteligente de Leads", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    story.append(Paragraph(
        "No todos los prospectos son iguales. El sistema de Ryventis implementa un flujo de calificación "
        "automática que separa a tus leads en tres categorías:", S["body"]))

    leads = [
        ("LEADS CALIENTES", CYAN,  CYAN_BG,
         "Responden preguntas clave, tienen presupuesto definido, necesidad urgente.<br/>"
         "<b>Acción:</b> Escalar inmediatamente al vendedor humano."),
        ("LEADS TIBIOS",   VIOLET, VIOLET_BG,
         "Están explorando opciones, comparando precios.<br/>"
         "<b>Acción:</b> Secuencia de nurturing automático (3-7 mensajes en 14 días)."),
        ("LEADS FRÍOS",    GRAY,   LIGHT_BG,
         "Preguntas muy generales, sin compromiso.<br/>"
         "<b>Acción:</b> Agregar a lista de contenido educativo mensual."),
    ]
    for title, color, bg, text in leads:
        badge_style = ParagraphStyle("badge",
            fontName="Helvetica-Bold", fontSize=10, textColor=WHITE)
        inner = Table([
            [Paragraph(title, badge_style)],
            [Paragraph(text, S["body"])],
        ], colWidths=[155*mm])
        inner.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), color),
            ("BACKGROUND", (0,1), (-1,1), bg),
            ("LEFTPADDING", (0,0), (-1,-1), 12),
            ("RIGHTPADDING", (0,0), (-1,-1), 12),
            ("TOPPADDING", (0,0), (0,0), 8),
            ("BOTTOMPADDING", (0,0), (0,0), 8),
            ("TOPPADDING", (0,1), (-1,-1), 8),
            ("BOTTOMPADDING", (0,1), (-1,-1), 10),
        ]))
        story.append(inner)
        story.append(Spacer(1, 3*mm))

    story.append(make_callout(
        "Resultado clave",
        "El equipo de ventas humano solo recibe leads calientes — "
        "su tasa de cierre sube del 8% al 35%.",
        DARK, S
    ))

    # ── SECTION 7 ─────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("SECCIÓN 7", S["section_label"]))
    story.append(Paragraph("Casos de Uso por Sector — Puebla", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    sectors = [
        ("Clínicas y Consultorios",
         "Llamadas perdidas, pacientes que no confirman citas, agenda desorganizada.",
         "Bot de agendado en WhatsApp + recordatorios automáticos 24h antes.",
         "40% menos de inasistencias, 3 horas/día liberadas para la recepcionista."),
        ("Inmobiliarias",
         "Leads de portales no atendidos en tiempo real, seguimiento manual inconsistente.",
         "Agente de calificación + seguimiento automático por WhatsApp.",
         "Primer contacto: de 6 horas a 45 segundos. Conversión +18%."),
        ("Talleres Mecánicos",
         "Clientes que preguntan precio y no regresan, sin seguimiento post-servicio.",
         "Bot de cotización + recordatorio de servicio cada 3 meses.",
         "+25% en retención de clientes existentes."),
        ("Despachos Contables",
         "Preguntas repetitivas sobre fechas de declaración y documentos requeridos.",
         "FAQ automatizado + alertas fiscales automáticas.",
         "2 horas/día liberadas del contador para trabajo de alto valor."),
    ]
    for sector, problem, solution, result in sectors:
        sec_data = [
            [Paragraph(sector, S["sector_title"])],
            [Table([
                [Paragraph("<b>Problema:</b>", S["table_cell"]),  Paragraph(problem, S["table_cell"])],
                [Paragraph("<b>Solución:</b>", S["table_cell"]),  Paragraph(solution, S["table_cell"])],
                [Paragraph("<b>Resultado:</b>", S["table_cell_good"]), Paragraph(result, S["table_cell_good"])],
            ], colWidths=[28*mm, 122*mm], style=TableStyle([
                ("LEFTPADDING", (0,0), (-1,-1), 0),
                ("RIGHTPADDING", (0,0), (-1,-1), 0),
                ("TOPPADDING", (0,0), (-1,-1), 4),
                ("BOTTOMPADDING", (0,0), (-1,-1), 4),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
            ]))],
        ]
        sec_block = Table(sec_data, colWidths=[155*mm])
        sec_block.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), LIGHT_BG),
            ("LEFTPADDING", (0,0), (-1,-1), 12),
            ("RIGHTPADDING", (0,0), (-1,-1), 12),
            ("TOPPADDING", (0,0), (0,0), 10),
            ("BOTTOMPADDING", (0,-1), (-1,-1), 12),
            ("TOPPADDING", (0,1), (-1,-1), 4),
            ("LINEABOVE", (0,0), (-1,0), 3, VIOLET),
        ]))
        story.append(sec_block)
        story.append(Spacer(1, 5*mm))

    # ── SECTION 8 ─────────────────────────────────────────────
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph("SECCIÓN 8", S["section_label"]))
    story.append(Paragraph("Inversión y Retorno", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    story.append(Paragraph(
        "Precios de lanzamiento para los primeros 5 clientes (vigentes hasta octubre 2026):", S["body"]))

    price_header = [
        Paragraph("Servicio", S["table_header"]),
        Paragraph("Setup", S["table_header"]),
        Paragraph("Retainer/mes", S["table_header"]),
    ]
    price_rows = [
        ["Chatbot Inteligente (WhatsApp/Web)", "$18,000 MXN", "$4,500 MXN"],
        ["Automatización de Procesos (n8n)", "$14,000 MXN", "$3,500 MXN"],
        ["Pack Starter IA (Chatbot + Automatización)", "$28,500 MXN", "$5,800 MXN"],
        ["Agente Autónomo de Ventas/Soporte", "$28,000 MXN", "$7,000 MXN"],
    ]
    price_data = [price_header] + [
        [Paragraph(r[0], S["table_cell"]), Paragraph(r[1], S["table_cell"]), Paragraph(r[2], S["table_cell_good"])]
        for r in price_rows
    ]
    price_table = Table(price_data, colWidths=[90*mm, 32*mm, 33*mm])
    price_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 9),
        ("BOTTOMPADDING", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [LIGHT_BG, colors.white, CYAN_BG, LIGHT_BG]),
        ("FONTNAME", (0,3), (-1,3), "Helvetica-Bold"),
    ]))
    story.append(price_table)
    story.append(Spacer(1, 6*mm))

    story.append(Paragraph("<b>ROI estimado — ejemplo Pack Starter IA:</b>", S["highlight"]))
    roi_data = [
        [Paragraph("Concepto", S["table_header"]), Paragraph("Valor", S["table_header"])],
        [Paragraph("Inversión mes 1 (setup + retainer)", S["table_cell"]), Paragraph("$34,300 MXN", S["table_cell"])],
        [Paragraph("Ahorro mensual en horas de trabajo", S["table_cell"]), Paragraph("+$3,850 MXN", S["table_cell_good"])],
        [Paragraph("Leads recuperados × conversión × ticket", S["table_cell"]), Paragraph("+$24,000 MXN/mes", S["table_cell_good"])],
        [Paragraph("Ingreso adicional mensual estimado", S["table_cell"]), Paragraph("+$27,850 MXN", S["table_cell_good"])],
        [Paragraph("Punto de equilibrio", S["table_cell"]), Paragraph("Mes 2", S["table_cell_good"])],
        [Paragraph("ROI acumulado a 6 meses", S["table_cell"]), Paragraph("+287%", S["table_cell_good"])],
    ]
    roi_table = Table(roi_data, colWidths=[110*mm, 45*mm])
    roi_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), DARK),
        ("BACKGROUND", (0,-1), (-1,-1), GREEN_SOFT),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 9),
        ("BOTTOMPADDING", (0,0), (-1,-1), 9),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#E5E7EB")),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [LIGHT_BG, colors.white, LIGHT_BG, colors.white, LIGHT_BG]),
        ("FONTNAME", (0,-1), (-1,-1), "Helvetica-Bold"),
        ("FONTSIZE", (1,-1), (1,-1), 13),
    ]))
    story.append(roi_table)

    # ── SECTION 9 ─────────────────────────────────────────────
    story.append(PageBreak())
    story.append(Paragraph("SECCIÓN 9", S["section_label"]))
    story.append(Paragraph("¿Por Qué Ryventis?", S["section_title"]))
    story.append(HRFlowable(width="100%", thickness=2, color=CYAN, spaceAfter=10))

    reasons = [
        ("Implementación local en Puebla", "Sin intermediarios internacionales. Tu socio tecnológico está aquí."),
        ("Entrega garantizada < 72 horas", "De la firma al bot activo en menos de 3 días."),
        ("Sin contratos de largo plazo forzosos", "Confía en los resultados, no en cláusulas."),
        ("Capacitación incluida para tu equipo", "Tu personal domina la herramienta desde el día 1."),
        ("Soporte continuo post-entrega", "No desaparecemos después de entregar. Somos tu equipo de IA."),
        ("Tecnología 2026 de última generación", "Modelos de IA actualizados, flujos probados en producción."),
        ("Enfoque 100% en ROI", "Medimos resultados reales, no promesas vacías."),
    ]
    for i, (title, desc) in enumerate(reasons):
        r_data = [[
            Paragraph(f"0{i+1}", ParagraphStyle("num", fontName="Helvetica-Bold",
                fontSize=18, textColor=WHITE, alignment=TA_CENTER)),
            Table([
                [Paragraph(title, S["highlight"])],
                [Paragraph(desc, S["body"])],
            ], colWidths=[128*mm], style=TableStyle([
                ("LEFTPADDING", (0,0), (-1,-1), 0),
                ("RIGHTPADDING", (0,0), (-1,-1), 0),
                ("TOPPADDING", (0,0), (-1,-1), 0),
                ("BOTTOMPADDING", (0,0), (-1,-1), 0),
            ])),
        ]]
        r_block = Table(r_data, colWidths=[20*mm, 135*mm])
        r_block.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,0), CYAN if i % 2 == 0 else VIOLET),
            ("BACKGROUND", (1,0), (1,0), LIGHT_BG),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("LEFTPADDING", (0,0), (-1,-1), 10),
            ("RIGHTPADDING", (0,0), (-1,-1), 12),
            ("TOPPADDING", (0,0), (-1,-1), 10),
            ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ]))
        story.append(r_block)
        story.append(Spacer(1, 3*mm))

    # ── CTA ───────────────────────────────────────────────────
    story.append(Spacer(1, 8*mm))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

    cta_box_data = [
        [Paragraph("¿Listo para que tu negocio trabaje solo?", S["cta_title"])],
        [Paragraph(
            "El diagnóstico inicial es <b>completamente gratuito</b>. En 60 minutos identificamos "
            "exactamente qué automatizar primero y calculamos tu ROI potencial — sin costo y sin compromisos.",
            S["cta_body"])],
        [Spacer(1, 4*mm)],
        [Table([
            [
                Paragraph("<b>Email:</b> ryventis.solutions@gmail.com", S["cta_body"]),
                Paragraph("<b>Web:</b> ryventis.mx", S["cta_body"]),
            ]
        ], colWidths=[80*mm, 75*mm], style=TableStyle([
            ("LEFTPADDING", (0,0), (-1,-1), 0),
            ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ]))],
        [Spacer(1, 2*mm)],
        [Paragraph("WhatsApp disponible en ryventis.mx", S["cta_body"])],
    ]
    cta_block = Table(cta_box_data, colWidths=[155*mm])
    cta_block.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CYAN_BG),
        ("LEFTPADDING", (0,0), (-1,-1), 16),
        ("RIGHTPADDING", (0,0), (-1,-1), 16),
        ("TOPPADDING", (0,0), (0,0), 18),
        ("BOTTOMPADDING", (0,-1), (-1,-1), 18),
        ("TOPPADDING", (0,1), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-2), 4),
        ("LINEABOVE", (0,0), (-1,0), 4, CYAN),
        ("LINEBELOW", (0,-1), (-1,-1), 4, CYAN),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ]))
    story.append(cta_block)

    doc.build(story)
    print(f"PDF generado: {OUT}")

if __name__ == "__main__":
    build()
