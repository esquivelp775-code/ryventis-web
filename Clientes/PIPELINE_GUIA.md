# PIPELINE DE CLIENTES — RYVENTIS SOLUTIONS
**Documento:** Guía operativa del ciclo de vida de prospectos y clientes  
**Responsable:** 🔴 The Hunter + 🔵 The Driver  
**Versión:** 1.0 | **Fecha:** 2026-04-13

---

## ESTRUCTURA DEL PIPELINE

```
Clientes/
├── PIPELINE_GUIA.md              ← Este archivo
├── Prospectos/                   ← Etapa 1: resultados de búsqueda (The Hunter)
│   └── YYYY-MM-DD_Sesion_N_[Sector]/
│       ├── RESUMEN_SESION.md     ← Índice de todos los prospectos de esa sesión
│       └── [NombreNegocio]/      ← Una carpeta por prospecto encontrado
│           └── PERFIL_PROSPECTO.md
│
├── En_Diagnostico/               ← Etapa 2: primer contacto confirmado
│   └── [NombreNegocio]/
│       ├── PERFIL_PROSPECTO.md   ← Heredado de Prospectos/
│       └── BRIEFING_DESCUBRIMIENTO.md
│
├── Propuesta_Enviada/            ← Etapa 3: propuesta formal entregada
│   └── [NombreNegocio]/
│       ├── PERFIL_PROSPECTO.md
│       └── PROPUESTA_[FECHA].md
│
├── En_Curso/                     ← Etapa 4: contrato firmado, proyecto activo
│   └── [NombreNegocio]/
│       ├── CONTRATO.md
│       ├── ORDEN_DE_TRABAJO.md
│       ├── BLUEPRINT.md
│       └── [archivos del proyecto]
│
├── Activos_Retainer/             ← Etapa 5: proyecto entregado, retainer activo
│   └── [NombreNegocio]/
│       ├── MANUAL_USUARIO.md
│       ├── REPORTES/
│       └── CHECKPOINTS/
│
└── Cerrados/                     ← Etapa 6: relación finalizada (ganada o perdida)
    └── [NombreNegocio]/
        └── LECCION_APRENDIDA.md
```

---

## REGLAS DE NOMENCLATURA

### Carpeta de sesión de prospección:
```
YYYY-MM-DD_Sesion_[N]_[Sector]
Ejemplo: 2026-04-13_Sesion_01_Clinicas
         2026-04-20_Sesion_02_Inmobiliarias
         2026-04-20_Sesion_03_Clinicas     ← si hay segunda sesión del mismo sector
```

### Carpeta de negocio/prospecto:
```
[NombreNegocio_SinEspacios]
Ejemplo: ClinicaDentalPerez
         TallerMecanicoRamirez
         InmobiliariaAzul
```

---

## FLUJO DE MOVIMIENTO ENTRE ETAPAS

```
BÚSQUEDA (The Hunter)
  → Crear: Prospectos/YYYY-MM-DD_Sesion_N_[Sector]/
  → Crear: RESUMEN_SESION.md + carpetas por prospecto

PRIMER CONTACTO CONFIRMADO
  → Mover carpeta: Prospectos/[Sesion]/[Nombre]/ → En_Diagnostico/[Nombre]/
  → Agregar: BRIEFING_DESCUBRIMIENTO.md (COMERCIAL-01)

PROPUESTA ENVIADA
  → Mover carpeta: En_Diagnostico/[Nombre]/ → Propuesta_Enviada/[Nombre]/
  → Agregar: PROPUESTA_[FECHA].md

CONTRATO FIRMADO + ANTICIPO CONFIRMADO
  → Mover carpeta: Propuesta_Enviada/[Nombre]/ → En_Curso/[Nombre]/
  → Agregar: CONTRATO.md + ORDEN_DE_TRABAJO.md + BLUEPRINT.md

PROYECTO ENTREGADO
  → Mover carpeta: En_Curso/[Nombre]/ → Activos_Retainer/[Nombre]/
  → Agregar: MANUAL_USUARIO.md + carpeta REPORTES/ + carpeta CHECKPOINTS/

RELACIÓN FINALIZADA
  → Mover carpeta a: Cerrados/[Nombre]/
  → Completar: LECCION_APRENDIDA.md (POST_VENTA-04)
```

---

## ESTRUCTURA DEL RESUMEN_SESION.md

Cada sesión de búsqueda debe generar un `RESUMEN_SESION.md` con:

```markdown
# RESUMEN DE SESIÓN DE PROSPECCIÓN
Fecha: YYYY-MM-DD | Sesión: N | Sector: [Sector]
Agente: 🔴 The Hunter | Herramienta: Google Maps / Redes

## Resumen rápido
- Total prospectos encontrados: X
- Calificados (score ≥ 3): X
- Descartados: X
- Prioridad alta (contactar esta semana): X

## Tabla de prospectos

| # | Nombre del Negocio | Carpeta | Score | Prioridad | Estado |
|---|--------------------|---------|-------|-----------|--------|
| 1 | [Nombre] | [Nombre_Carpeta]/ | X/5 | Alta/Media/Baja | Pendiente |

## Notas del Hunter
[Observaciones del sector, patrones, señales de mercado]
```

---

## PLANTILLAS ASOCIADAS POR ETAPA

| Etapa | Plantilla a usar |
|-------|-----------------|
| Prospectos | COMERCIAL-05: Perfil Prospecto Calificado |
| En_Diagnostico | COMERCIAL-01: Briefing Descubrimiento + COMERCIAL-06: Script Llamada |
| Propuesta_Enviada | COMERCIAL-02: Auditoría + COMERCIAL-03 o 07: Propuesta |
| En_Curso | LEGAL-01: Contrato + LEGAL-06: Orden de Trabajo + TECNICO-01: Blueprint |
| Activos_Retainer | POST_VENTA-01: Manual + LEGAL-04: Retainer + POST_VENTA-03: Reporte Mensual |
| Cerrados | POST_VENTA-04: Lección Aprendida |

---

*Pipeline Guide v1.0 | The Hunter + The Driver | Ryventis Solutions*
