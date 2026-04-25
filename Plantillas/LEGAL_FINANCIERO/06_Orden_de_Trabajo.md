# ORDEN DE TRABAJO INTERNA — RYVENTIS SOLUTIONS
**Plantilla:** LEGAL-06 | **Agente responsable:** 🟢 The Treasurer → 🟠 The Stack  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** The Treasurer emite este documento DESPUÉS de confirmar el anticipo del 50%. Es la señal verde oficial que autoriza a The Stack a iniciar el trabajo. Sin este documento, no hay desarrollo.

---

# ORDEN DE TRABAJO — AUTORIZACIÓN DE INICIO

```
╔══════════════════════════════════════════════════════════════╗
║           🟢 VALIDACIÓN DE TREASURER — NIVEL 5               ║
║              PRODUCCIÓN AUTORIZADA PARA INICIAR              ║
╚══════════════════════════════════════════════════════════════╝
```

**Folio OT:** RYV-OT-[AÑO]-[NÚMERO]  
**Fecha de emisión:** [FECHA] [HORA]  
**Emitida por:** 🟢 The Treasurer (Nivel 5)  
**Dirigida a:** 🟠 The Stack (Nivel 4)  
**Copia a:** 🔵 The Driver (Nivel 1)

---

## SECCIÓN 1 — DATOS DEL PROYECTO

| Campo | Detalle |
|-------|---------|
| **Cliente** | [NOMBRE DEL NEGOCIO] |
| **Contrato de referencia** | RYV-CONT-[AÑO]-[NÚMERO] |
| **Servicio a desarrollar** | [NOMBRE DEL SERVICIO] |
| **Propuesta de referencia** | RYV-PROP-[AÑO]-[NÚMERO] |
| **Ejecutivo comercial** | [NOMBRE DEL CLOSER] |

---

## SECCIÓN 2 — CONFIRMACIÓN FINANCIERA (The Treasurer)

```
ANTICIPO RECIBIDO: ✅ CONFIRMADO

  Monto del anticipo:          $_________ MXN
  Fecha de recepción:          [FECHA]
  Hora de confirmación:        [HORA]
  Método de pago:              ☐ SPEI ☐ Tarjeta ☐ Efectivo
  Referencia de transferencia: _________________________
  Recibo emitido No.:          RYV-REC-[AÑO]-[NÚMERO]
  Factura emitida:             ☐ Sí — CFDI: _________ ☐ No requiere

SALDO PENDIENTE:               $_________ MXN
  (Exigible al entregar el sistema funcionando)

RETAINER ACORDADO:             $_________ MXN/mes
  (Inicia mes 2, día _____ de cada mes)

VALIDACIÓN FINANCIERA:         ✅ APROBADO — PROCEDER CON PRODUCCIÓN
```

---

## SECCIÓN 3 — ALCANCE TÉCNICO AUTORIZADO

*The Stack debe construir EXACTAMENTE lo siguiente. Nada más, nada menos.*

### Módulos a desarrollar:

| # | Módulo | Descripción técnica | Prioridad |
|---|--------|---------------------|-----------|
| 1 | [NOMBRE] | [Descripción del módulo] | Alta |
| 2 | [NOMBRE] | [Descripción del módulo] | Alta |
| 3 | [NOMBRE] | [Descripción del módulo] | Media |
| 4 | [NOMBRE] | [Descripción del módulo] | Media |

### Integraciones requeridas:

| Integración | Tipo | Credenciales del cliente | Estado |
|-------------|------|--------------------------|--------|
| WhatsApp Business API | _____ | ☐ Recibidas ☐ Pendientes | _____ |
| Google Calendar | _____ | ☐ Recibidas ☐ Pendientes | _____ |
| Google Sheets / Supabase | _____ | ☐ Recibidas ☐ Pendientes | _____ |
| [Otro] | _____ | ☐ Recibidas ☐ Pendientes | _____ |

---

## SECCIÓN 4 — RESTRICCIONES DE ALCANCE

**The Stack NO debe implementar sin cotización adicional aprobada:**

- [ ] [Restricción 1 — ej: Dashboard frontend]
- [ ] [Restricción 2 — ej: Integración con POS]
- [ ] Cualquier funcionalidad no listada en la Sección 3

Si durante el desarrollo el cliente solicita cambios de alcance, The Stack debe:
1. Parar el trabajo en el cambio
2. Notificar a The Driver con estimado de tiempo/costo
3. Esperar validación del CEO antes de continuar

---

## SECCIÓN 5 — PLAZOS Y ENTREGABLES

| Entregable | Fecha límite | Responsable |
|------------|-------------|-------------|
| Blueprint / arquitectura documentada | [FECHA] | The Stack → The Scribe |
| Desarrollo completado | [FECHA] | The Stack |
| QA 10 puntos completado | [FECHA] | The Stack |
| Entrega al cliente + capacitación | [FECHA] | The Stack + Closer |
| Manual de usuario entregado | [FECHA] | The Stack + Scribe |

**Fecha límite absoluta de entrega:** [FECHA]  
*(Esta fecha fue prometida al cliente en el contrato)*

---

## SECCIÓN 6 — INFRAESTRUCTURA Y COSTOS AUTORIZADOS

*The Stack puede incurrir en los siguientes gastos sin aprobación adicional:*

| Herramienta | Costo máximo autorizado | Pagado por |
|-------------|------------------------|------------|
| Railway (hosting) | $[X] MXN/mes | Ryventis |
| n8n / nodos | $[X] MXN | Ryventis |
| Tokens de Claude API | $[X] USD (≈$[X] MXN) | Ryventis |
| [Otro] | $[X] MXN | ☐ Ryventis ☐ Cliente |

**Presupuesto máximo de infraestructura:** $_________ MXN  
*(Si se proyecta superar este monto, escalar a The Driver antes de continuar)*

---

## SECCIÓN 7 — PROTOCOLO DE CIERRE DEL PROYECTO

The Stack confirma entrega cuando:
- [ ] QA de 10 puntos completado sin errores críticos (ver TECNICO-02)
- [ ] Manual de usuario entregado al cliente (POST_VENTA-01)
- [ ] Capacitación al cliente completada y confirmada
- [ ] Credenciales y accesos transferidos al cliente
- [ ] Documentación técnica enviada a The Scribe
- [ ] The Treasurer notificado para cobro del saldo final

---

## SECCIÓN 8 — FIRMA DE AUTORIZACIÓN

```
🟢 THE TREASURER — VALIDACIÓN FINANCIERA

  Nombre: _______________________________
  Fecha:  _______________________________
  Firma:  _______________________________

  ESTADO: ✅ ANTICIPO CONFIRMADO — PRODUCCIÓN AUTORIZADA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔵 THE DRIVER — ASIGNACIÓN OFICIAL

  "The Stack: tienes luz verde para iniciar el proyecto
   RYV-OT-[AÑO]-[NÚMERO]. Fecha límite: [FECHA].
   Reporta progreso diario en el canal del proyecto."

  Firma del Driver: _______________________________
  Fecha de asignación: _______________________________
```

---

## REGISTRO DE HITOS (The Stack actualiza durante el proyecto)

| Fecha | Hito | Estado | Notas |
|-------|------|--------|-------|
| _____ | Blueprint aprobado | ☐ | |
| _____ | Desarrollo módulo 1 | ☐ | |
| _____ | Desarrollo módulo 2 | ☐ | |
| _____ | Integraciones conectadas | ☐ | |
| _____ | QA completado | ☐ | |
| _____ | Entrega al cliente | ☐ | |
| _____ | Saldo cobrado | ☐ | |
| _____ | Documentación entregada al Scribe | ☐ | |

---

*Folio: RYV-OT-[AÑO]-[NÚMERO] | Documento de uso interno | Ryventis Solutions*
