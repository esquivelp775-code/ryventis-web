# BLUEPRINT DE ARQUITECTURA DEL SISTEMA — RYVENTIS SOLUTIONS
**Plantilla:** TECNICO-01 | **Agente responsable:** 🟠 The Stack / The Insight  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Completar ANTES de escribir una sola línea de código. Este documento es el contrato técnico interno. The Stack construye exactamente lo que aquí se documenta. The Scribe lo archiva al cerrar el proyecto.

---

# BLUEPRINT DEL SISTEMA
## [NOMBRE DEL PROYECTO] — [NOMBRE DEL CLIENTE]

| Campo | Valor |
|-------|-------|
| Folio | RYV-TECH-[AÑO]-[NÚMERO] |
| Proyecto relacionado | RYV-OT-[AÑO]-[NÚMERO] |
| Fecha de creación | [FECHA] |
| Versión | 1.0 |
| Aprobado por CEO | ☐ Sí — Fecha: _______ ☐ Pendiente |

---

## RESUMEN EJECUTIVO (Para el CEO — sin tecnicismos)

> **¿Qué hace este sistema en palabras simples?**
> 
> [2-3 oraciones describiendo el resultado para el cliente. Ejemplo: "Este sistema hace que el bot de WhatsApp de la Clínica X responda automáticamente a los pacientes, agende citas en Google Calendar, y mande recordatorios 24 horas antes. El doctor no tiene que tocar el teléfono."]

**Resultado esperado para el negocio del cliente:**
- [Beneficio 1]: ___________________________
- [Beneficio 2]: ___________________________
- [Beneficio 3]: ___________________________

---

## DIAGRAMA DE FLUJO DEL SISTEMA

```
FLUJO PRINCIPAL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[USUARIO]
    │
    ▼ Mensaje en WhatsApp
[WhatsApp Business API]
    │
    ▼ Webhook dispara evento
[n8n — Nodo disparador (Webhook)]
    │
    ├─► ¿Es una pregunta frecuente? ──► [IA responde automáticamente]
    │                                          │
    │                                          ▼
    │                                  [Respuesta enviada]
    │
    ├─► ¿Quiere agendar cita?
    │           │
    │           ▼
    │   [Nodo: Verificar disponibilidad en Google Calendar]
    │           │
    │           ├─► Disponible ──► [Confirmar cita + enviar detalles]
    │           │                          │
    │           │                          ▼
    │           │                  [Registro en Google Sheets / Supabase]
    │           │
    │           └─► No disponible ──► [Ofrecer alternativas]
    │
    ├─► ¿Es una queja o caso complejo?
    │           │
    │           ▼
    │   [Escalar a humano — notificar al dueño]
    │
    └─► [Cerrar conversación después de X minutos sin respuesta]

FLUJO DE RECORDATORIOS (Disparado por cron):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Cron — Ejecuta diario a las [HORA]]
    │
    ▼
[Leer citas del día siguiente desde Google Calendar]
    │
    ▼
[Para cada cita: enviar recordatorio a WhatsApp del paciente]
    │
    ▼
[Registrar envío en log]
```

---

## STACK TECNOLÓGICO DEL PROYECTO

| Capa | Herramienta | Versión / Plan | Propósito |
|------|-------------|----------------|-----------|
| Orquestación | n8n | Self-hosted en Railway | Flujos de automatización |
| Mensajería | WhatsApp Business API | Meta Cloud | Envío/recepción de mensajes |
| IA | Claude API | claude-haiku-4-5-20251001 | Generación de respuestas |
| Base de datos | [Supabase / Google Sheets] | [Plan Free / Pro] | Almacenamiento de datos |
| Calendario | Google Calendar API | v3 | Gestión de citas |
| Hosting n8n | Railway | Starter | Servidor 24/7 |
| CRM | Airtable | [Plan] | Tracking de leads |
| Otros | _____________ | _____________ | _____________ |

---

## ESPECIFICACIONES DE CADA MÓDULO

### MÓDULO 1 — [NOMBRE DEL MÓDULO]

```
Nombre técnico: [nombre-del-flujo-en-n8n]
Tipo: ☐ Flujo webhook ☐ Flujo cron ☐ Flujo manual
Disparador: [descripción del evento que lo activa]

NODOS PRINCIPALES:
  1. [Nombre del nodo] — [Propósito]
  2. [Nombre del nodo] — [Propósito]
  3. [Nombre del nodo] — [Propósito]

ENTRADAS REQUERIDAS:
  - [Variable de entrada 1]: Tipo [string/number/object]
  - [Variable de entrada 2]: Tipo [string/number/object]

SALIDAS:
  - [Output 1]: [Descripción]
  - [Output 2]: [Descripción]

CASOS DE ERROR MANEJADOS:
  - [Error 1]: [Cómo se maneja]
  - [Error 2]: [Cómo se maneja]

CASOS DE BORDE:
  - ¿Qué pasa si el mensaje llega fuera de horario? → [Comportamiento]
  - ¿Qué pasa si la API de WhatsApp falla? → [Comportamiento]
  - ¿Qué pasa si Google Calendar no responde? → [Comportamiento]
```

---

### MÓDULO 2 — [NOMBRE DEL MÓDULO]

```
[Repetir estructura del Módulo 1]
```

---

### MÓDULO 3 — [NOMBRE DEL MÓDULO]

```
[Repetir estructura del Módulo 1]
```

---

## PROMPTS DE IA

### Prompt Sistema Principal

```
ROL: Eres el asistente virtual de [NOMBRE DEL NEGOCIO], una [tipo de negocio]
ubicada en Puebla, México. Tu nombre es [NOMBRE DEL BOT].

TONO: [Profesional y cálido / Casual y amigable / Formal]

CONOCIMIENTO BASE:
[Descripción de los servicios, precios y horarios del cliente]

REGLAS:
1. Siempre saludar con el nombre del cliente si está disponible
2. Nunca inventar precios o disponibilidades — consultar los datos reales
3. Si no sabes algo, decir: "Déjame verificar eso y te confirmo en un momento"
4. Si hay una queja, no responder directamente — escalar al dueño inmediatamente
5. Máximo [X] intercambios antes de ofrecer hablar con el dueño

RESTRICCIONES:
- No hablar de competidores
- No hacer promesas que no estén en la base de conocimiento
- No recopilar datos bancarios o contraseñas
```

---

## VARIABLES DE ENTORNO (Credenciales — NO incluir valores reales)

```
# WhatsApp Business API
WHATSAPP_API_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_WEBHOOK_VERIFY_TOKEN=

# Google Calendar
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REFRESH_TOKEN=
GOOGLE_CALENDAR_ID=

# Claude API
ANTHROPIC_API_KEY=

# Base de datos
DATABASE_URL=
SUPABASE_ANON_KEY=

# n8n
N8N_WEBHOOK_URL=
N8N_API_KEY=

# Otros
[VARIABLE]=[DESCRIPCIÓN]
```

**Ubicación segura de credenciales reales:**  
☐ Railway Environment Variables  
☐ .env local (nunca commitear al repo)  
☐ Bitwarden / 1Password  

---

## ESTIMADOS DE RENDIMIENTO Y COSTOS

| Métrica | Estimado | Límite de alerta |
|---------|----------|-----------------|
| Mensajes/día esperados | _____ | _____ |
| Llamadas API Claude/día | _____ | _____ |
| Tokens consumidos/mes | _____ | _____ |
| Costo Claude API/mes | $_____ USD | $_____ USD |
| Costo Railway/mes | $_____ USD | |
| **Costo operativo total/mes** | $_____ USD (≈$_____ MXN) | |

---

## PLAN DE PRUEBAS (Resumen — ver TECNICO-02 para detalle)

| Caso de prueba | Resultado esperado | ☐ Pasa |
|----------------|-------------------|--------|
| Mensaje en horario laboral | Respuesta en < 5 segundos | ☐ |
| Mensaje fuera de horario | Respuesta con horarios | ☐ |
| Solicitud de cita disponible | Cita confirmada + evento en Calendar | ☐ |
| Solicitud de cita sin disponibilidad | Alternativas ofrecidas | ☐ |
| Recordatorio 24h antes | Mensaje enviado al cliente | ☐ |
| Mensaje con contenido inapropiado | Respuesta educada + escalado | ☐ |
| Falla de API externa | Mensaje de error amigable | ☐ |

---

## DECISIONES TÉCNICAS DOCUMENTADAS

*Registrar aquí cualquier decisión importante y el porqué*

| Decisión | Alternativa considerada | Razón de la elección |
|----------|------------------------|----------------------|
| Usar Claude Haiku en lugar de Sonnet | Sonnet para todo | Haiku reduce costo 10x manteniendo calidad suficiente para FAQ |
| Google Sheets como DB | Supabase | Cliente ya usa Google Workspace, menor fricción de adopción |
| [Otra decisión] | [Alternativa] | [Razón] |

---

## HISTORIAL DE VERSIONES DEL BLUEPRINT

| Versión | Fecha | Cambio | Motivo |
|---------|-------|--------|--------|
| 1.0 | [FECHA] | Documento inicial | Kickoff del proyecto |
| 1.1 | [FECHA] | [Cambio] | [Motivo] |

---

*Folio: RYV-TECH-[AÑO]-[NÚMERO] | Uso interno — The Stack / The Scribe*  
*Ryventis Solutions | ryventis.mx*
