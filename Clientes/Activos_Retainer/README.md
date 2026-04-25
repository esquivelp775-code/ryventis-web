# ETAPA 5 — ACTIVOS EN RETAINER
**Agente responsable:** 🟢 The Bridge  
**Descripción:** Clientes con proyecto entregado y retainer mensual activo. Máxima prioridad de retención.

---

## Cuándo se usa esta carpeta

Un cliente llega aquí cuando:
- El sistema fue entregado y el cliente lo confirmó (saldo final pagado)
- El Acuerdo de Mantenimiento Retainer (LEGAL-04) está firmado

## Estructura esperada

```
Activos_Retainer/
└── ClinicaDentalPerez/
    ├── [archivos heredados de En_Curso/]
    ├── MANUAL_USUARIO.md           ← POST_VENTA-01
    ├── ACUERDO_RETAINER.md         ← LEGAL-04 firmado
    ├── REPORTES/
    │   ├── Reporte_2026-05.md      ← POST_VENTA-03 mensual
    │   └── Reporte_2026-06.md
    ├── CHECKPOINTS/
    │   ├── Checkpoint_30dias.md    ← POST_VENTA-05
    │   └── Checkpoint_60dias.md
    └── UPSELL/
        └── Oportunidad_Dashboard.md ← POST_VENTA-06
```

## Cómo avanzar

Si el cliente cancela el retainer → mover a `../Cerrados/` + completar POST_VENTA-04 (Lección Aprendida)

---

*Ver PIPELINE_GUIA.md para el flujo completo.*
