# COTIZADOR DINÁMICO DE PROYECTOS — RYVENTIS SOLUTIONS
**Plantilla:** LEGAL-02 | **Agente responsable:** 🟢 The Treasurer / 🟣 The Insight  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Completar esta hoja antes de generar cualquier propuesta. Calcula el precio real del proyecto considerando horas de trabajo, infraestructura, APIs y margen. El precio final al cliente NUNCA debe ser menor al "Precio Mínimo Aceptable".

---

## DATOS DEL PROYECTO

| Campo | Valor |
|-------|-------|
| Cliente | _________________________ |
| Servicio | _________________________ |
| Folio | RYV-COT-[AÑO]-[NÚMERO] |
| Elaborado por | _________________________ |
| Fecha | _________________________ |
| Revisado por (Treasurer) | _________________________ |

---

## BLOQUE 1 — HORAS DE TRABAJO ESTIMADAS

### Fase de Discovery / Diseño

| Tarea | Horas estimadas |
|-------|----------------|
| Reunión de diagnóstico y briefing | _____ hrs |
| Diseño de flujo / arquitectura del sistema | _____ hrs |
| Documentación del blueprint | _____ hrs |
| **Subtotal Discovery** | **_____ hrs** |

---

### Fase de Desarrollo

| Tarea | Horas estimadas |
|-------|----------------|
| Configuración base de n8n / plataforma | _____ hrs |
| Desarrollo flujo principal (módulo 1) | _____ hrs |
| Desarrollo flujo secundario (módulo 2) | _____ hrs |
| Desarrollo flujo secundario (módulo 3) | _____ hrs |
| Integración con WhatsApp Business API | _____ hrs |
| Integración con Google Calendar / Sheets | _____ hrs |
| Integración con CRM / base de datos | _____ hrs |
| Configuración de prompts de IA | _____ hrs |
| **Subtotal Desarrollo** | **_____ hrs** |

---

### Fase de QA y Entrega

| Tarea | Horas estimadas |
|-------|----------------|
| Pruebas de calidad (QA — 10 puntos) | _____ hrs |
| Correcciones post-QA | _____ hrs |
| Capacitación al cliente | _____ hrs |
| Preparación de documentación (manual) | _____ hrs |
| **Subtotal QA y Entrega** | **_____ hrs** |

---

### Fase de Soporte Mes 1 (incluido en proyecto)

| Tarea | Horas estimadas |
|-------|----------------|
| Monitoreo y ajustes semana 1 | _____ hrs |
| Revisión de resultados día 30 | _____ hrs |
| **Subtotal Soporte Mes 1** | **_____ hrs** |

---

### RESUMEN DE HORAS

| Fase | Horas |
|------|-------|
| Discovery / Diseño | _____ |
| Desarrollo | _____ |
| QA y Entrega | _____ |
| Soporte Mes 1 | _____ |
| **TOTAL HORAS PROYECTO** | **_____** |
| + Buffer de imprevistos (15%) | _____ |
| **TOTAL HORAS CON BUFFER** | **_____** |

---

## BLOQUE 2 — COMPLEJIDAD DE INTEGRACIONES

Sumar puntos según las integraciones requeridas:

| Integración | Puntos | ¿Incluida? | Puntos sumados |
|-------------|--------|-----------|----------------|
| WhatsApp Business API (básico) | 1 | ☐ | |
| WhatsApp Business API (avanzado con flujos) | 3 | ☐ | |
| Google Calendar (leer/escribir) | 1 | ☐ | |
| Google Sheets (leer/escribir) | 1 | ☐ | |
| Supabase / base de datos SQL | 2 | ☐ | |
| Airtable como CRM | 1 | ☐ | |
| CRM externo (HubSpot, Zoho, etc.) | 3 | ☐ | |
| Sistema POS o facturación del cliente | 4 | ☐ | |
| API personalizada del cliente | 5 | ☐ | |
| Pagos (Stripe, MercadoPago, etc.) | 3 | ☐ | |
| Email (envío automático) | 1 | ☐ | |
| Dashboard personalizado (frontend) | 4 | ☐ | |
| **TOTAL PUNTOS DE COMPLEJIDAD** | | | **_____** |

**Factor de complejidad:**
- 1-4 puntos: Factor 1.0 (sin ajuste)
- 5-8 puntos: Factor 1.15
- 9-12 puntos: Factor 1.30
- 13+ puntos: Factor 1.50 (proyecto Enterprise — requiere aprobación CEO)

**Factor aplicado:** _____

---

## BLOQUE 3 — COSTOS DE INFRAESTRUCTURA (Mensuales)

| Herramienta | Costo mensual | Responsable |
|-------------|---------------|-------------|
| Railway (hosting n8n) | $_____ MXN | ☐ Ryventis ☐ Cliente |
| n8n Cloud (si aplica) | $_____ MXN | ☐ Ryventis ☐ Cliente |
| WhatsApp Business API (Meta) | $_____ MXN | ☐ Ryventis ☐ Cliente |
| Supabase (plan free/pro) | $_____ MXN | ☐ Ryventis ☐ Cliente |
| Claude API (tokens estimados) | $_____ MXN | ☐ Ryventis ☐ Cliente |
| Airtable | $_____ MXN | ☐ Ryventis ☐ Cliente |
| Otros: _____________ | $_____ MXN | ☐ Ryventis ☐ Cliente |
| **TOTAL INFRAESTRUCTURA/MES** | **$_____ MXN** | |

**Infraestructura pagada por Ryventis durante el proyecto:** $_____ MXN  
**Infraestructura transferida al cliente post-entrega:** $_____ MXN/mes

---

## BLOQUE 4 — ESTIMADO DE CONSUMO DE TOKENS DE IA

| Métrica | Valor |
|---------|-------|
| Conversaciones esperadas por día | _____ |
| Mensajes promedio por conversación | _____ |
| Tokens promedio por mensaje (input + output) | _____ |
| **Total tokens/día** | _____ |
| **Total tokens/mes** | _____ |
| Costo por millón de tokens (Claude Haiku 4.5) | ~$0.30 USD |
| Costo por millón de tokens (Claude Sonnet 4.6) | ~$3.00 USD |
| Modelo a usar | ☐ Haiku ☐ Sonnet |
| **Costo estimado de IA/mes (USD)** | $_____ USD |
| **Costo estimado de IA/mes (MXN @$17)** | $_____ MXN |

> Regla: Si el costo de IA supera $500 MXN/mes, usar Haiku para conversaciones generales y Sonnet solo para análisis complejos.

---

## BLOQUE 5 — CÁLCULO DEL PRECIO

### Costo directo del proyecto

| Componente | Monto |
|------------|-------|
| Horas totales (con buffer) × $[TARIFA/HR] MXN | $_____ MXN |
| Factor de complejidad aplicado (×_____) | $_____ MXN |
| Infraestructura del proyecto (mes 1) | $_____ MXN |
| Tokens de IA durante desarrollo y pruebas | $_____ MXN |
| **COSTO DIRECTO TOTAL** | **$_____ MXN** |

---

### Precio final

| Concepto | Monto |
|----------|-------|
| Costo directo total | $_____ MXN |
| Margen operativo (objetivo 60-70%) | +$_____ MXN |
| **PRECIO BASE CALCULADO** | **$_____ MXN** |
| Redondeo al $500 MXN más cercano | $_____ MXN |
| **PRECIO FINAL AL CLIENTE** | **$_____ MXN** |
| **PRECIO MÍNIMO ACEPTABLE** (sin bajar de aquí) | **$_____ MXN** |
| Margen real si cierra en precio final | ____% |

---

### Precio del Retainer Mensual

| Componente | Monto/mes |
|------------|-----------|
| Horas de monitoreo y soporte estimadas (___hrs × $____/hr) | $_____ MXN |
| Infraestructura pagada por Ryventis | $_____ MXN |
| Costo de IA mensual | $_____ MXN |
| Margen retainer (objetivo 50%) | $_____ MXN |
| **PRECIO RETAINER MENSUAL** | **$_____ MXN** |
| **RETAINER MÍNIMO ACEPTABLE** | **$_____ MXN** |

---

## BLOQUE 6 — VALIDACIÓN DEL TREASURER

```
Revisado por: _______________________________
Fecha de revisión: _______________________________

¿El precio cubre todos los costos directos?: ☐ SÍ ☐ NO — Ajustar antes de proponer
¿El margen es >= 50%?: ☐ SÍ ☐ NO — Si no, escalar al CEO
¿Los costos de infraestructura están bien definidos?: ☐ SÍ ☐ NO
¿El retainer cubre el costo de operación mensual?: ☐ SÍ ☐ NO

VALIDACIÓN: ☐ APROBADO PARA PROPUESTA ☐ REQUIERE AJUSTE
```

---

## BLOQUE 7 — TABLA DE REFERENCIA DE PRECIOS RYVENTIS (v2 · Revisada 2026-04-20)

> **Ancla de mercado PYME:** Precios validados por estudio de mercado y ajustados por Pablo (CEO) el 2026-04-20 para accesibilidad PYME. El precio calculado en Bloque 5 NO debe ser menor al Setup Lanzamiento de referencia para el servicio equivalente.
>
> **Precio de Fundadores:** Aplica para los primeros 5 clientes hasta octubre 2026. Después, usar columna "Regular".

### Servicios por Proyecto

| Servicio | Setup Lanzamiento | Setup Regular | Retainer Lanzamiento | Retainer Regular |
|----------|:-----------------:|:-------------:|:--------------------:|:----------------:|
| Chatbot Inteligente (WhatsApp/Web) | **$9,500** | $12,000 | **$2,500/mes** | $3,500/mes |
| Automatización de Procesos (n8n/Make) | **$8,000** | $11,000 | **$2,000/mes** | $3,000/mes |
| Agente Autónomo de Ventas/Soporte | **$18,000** | $25,000 | **$4,500/mes** | $6,500/mes |
| Análisis de Datos con IA (Dashboard) | **$12,000** | $16,000 | **$2,800/mes** | $4,000/mes |
| Consultoría en Adopción de IA | **GRATIS** (diagnóstico 60 min) | — | **$4,500** reporte | $6,000 reporte |
| Pack Starter IA (Chatbot + Automatización) | **$16,000** | $21,000 | **$3,500/mes** | $5,000/mes |

### Suscripciones Mensuales (Tiers)

| Tier | Nombre | Incluye | Lanzamiento/mes | Regular/mes |
|------|--------|---------|:---------------:|:-----------:|
| Básico | **Starter AI** | 1 chatbot + soporte básico + reporte mensual | **$2,500** | $3,500 |
| Medio | **Pro AI** | Chatbot + 2 automatizaciones + dashboard + soporte prioritario | **$5,500** | $7,500 |
| Premium | **Enterprise AI** | Agente autónomo + análisis + automatizaciones + account manager | **$10,000** | $14,000 |

### ROI de Referencia por Sector (para validar justificación del precio)

| Sector | Costo manual mensual | Ahorro estimado | Punto de recuperación |
|--------|---------------------|-----------------|----------------------|
| Clínica dental — confirmación de citas (2h/día × $88/h) | $5,280 MXN | $3,168 en tiempo + citas recuperadas | **Mes 1-2** |
| Taller mecánico — cotizaciones y seguimiento (1.5h/día) | $3,960 MXN | $2,376 recuperados | **Mes 2** |
| Inmobiliaria — leads no respondidos (5/sem × $12,000 comisión) | $60,000 oportunidad perdida | Capturar 20% = $12,000/mes | **Mes 1** |
| Despacho contable — recordatorios documentos (1h/día) | $2,640 MXN | $1,584 recuperados | **Mes 3-4** |

> **Umbral psicológico PYME:** Sin aprobación de junta: < $8,000/mes. Con justificación de ROI: $5,000–$15,000/mes. Requiere aprobación formal: > $15,000 setup o > $10,000/mes.

---

## HISTORIAL DE VERSIONES DEL COTIZADOR

| Versión | Fecha | Cambio | Motivo |
|---------|-------|--------|--------|
| 1.0 | 2026-04-13 | Cotización inicial | Creación del sistema de plantillas |
| 2.0 | 2026-04-20 | Revisión de tabla de referencia de precios | Ajuste a accesibilidad PYME — decisión CEO Pablo |

---

*Documento de uso interno — NO compartir con el cliente*  
*Ryventis Solutions | ryventis.mx*
