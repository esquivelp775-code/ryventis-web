# DICCIONARIO DE DATOS Y APIs DEL SISTEMA — RYVENTIS SOLUTIONS
**Plantilla:** TECNICO-03 | **Agente responsable:** 🟠 The Stack / ⚪ The Scribe  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Completar durante el desarrollo. Entregar al cliente en versión simplificada (sin detalles técnicos internos). Archivar versión completa en Documentacion/.

---

# DICCIONARIO DE DATOS Y APIS
## [NOMBRE DEL PROYECTO] — [NOMBRE DEL CLIENTE]

**Versión:** 1.0 | **Fecha:** [FECHA]  
**Proyecto:** RYV-OT-[AÑO]-[NÚMERO]

---

## PARTE A — PARA EL CLIENTE (Versión simplificada)

### ¿Qué información maneja tu sistema?

Este documento explica de forma sencilla qué datos recopila, almacena y procesa el sistema que Ryventis construyó para **[NOMBRE DEL NEGOCIO]**.

---

### DATOS QUE EL SISTEMA RECOPILA AUTOMÁTICAMENTE

| Dato | ¿Para qué se usa? | ¿Dónde se guarda? | ¿Quién tiene acceso? |
|------|------------------|-------------------|----------------------|
| Número de WhatsApp del cliente | Responder mensajes y agendar citas | [Google Sheets / Supabase] | Solo tú (dueño) |
| Nombre del cliente | Personalizar la comunicación | [Google Sheets / Supabase] | Solo tú (dueño) |
| Fecha y hora de cita | Gestionar el calendario | Google Calendar | Solo tú (dueño) |
| Historial de mensajes | Dar contexto al bot en la conversación | Temporal (no se almacena) | Nadie — se borra |
| [Dato adicional] | [Propósito] | [Ubicación] | [Acceso] |

---

### DATOS QUE EL SISTEMA NO RECOPILA (NUNCA)

- Contraseñas ni datos bancarios
- Información médica sensible (salvo que el cliente lo configure expresamente)
- Ubicación GPS en tiempo real
- Conversaciones de otros canales distintos al acordado

---

### ¿Puedes exportar o borrar los datos?

**Sí.** Toda la información está en tu cuenta de Google Sheets / Supabase. Tú tienes acceso total y puedes:
- Ver todos los registros cuando quieras
- Exportar la base de datos en Excel/CSV en cualquier momento
- Borrar cualquier registro de cualquier cliente

---

## PARTE B — TÉCNICA INTERNA (Solo The Stack / The Scribe)

### ESTRUCTURA DE LA BASE DE DATOS

#### Tabla: `clientes` (o Hoja: "Clientes")

| Campo | Tipo | Descripción | Ejemplo | Obligatorio |
|-------|------|-------------|---------|-------------|
| `id` | UUID / Auto-increment | Identificador único | `c1a2b3-...` | ✅ |
| `telefono_whatsapp` | STRING(20) | Número con código de país | `+52155xxxxxxxx` | ✅ |
| `nombre` | STRING(100) | Nombre completo o como se presentó | `María García` | ☐ |
| `correo` | STRING(200) | Email si lo proporcionó | `maria@email.com` | ☐ |
| `fecha_primer_contacto` | TIMESTAMP | Cuándo escribió por primera vez | `2026-04-13 10:30:00` | ✅ |
| `ultima_interaccion` | TIMESTAMP | Último mensaje procesado | `2026-04-13 15:45:00` | ✅ |
| `estado` | ENUM | lead / activo / inactivo | `activo` | ✅ |
| `notas` | TEXT | Notas adicionales | `Prefiere citas en tarde` | ☐ |
| `created_at` | TIMESTAMP | Registro automático | `2026-04-13 10:30:00` | ✅ |

---

#### Tabla: `citas` (o Hoja: "Citas")

| Campo | Tipo | Descripción | Ejemplo | Obligatorio |
|-------|------|-------------|---------|-------------|
| `id` | UUID / Auto-increment | Identificador único | `cita-001` | ✅ |
| `cliente_id` | FK → clientes.id | Referencia al cliente | `c1a2b3-...` | ✅ |
| `telefono_cliente` | STRING(20) | Para enviar recordatorio | `+52155xxxxxxxx` | ✅ |
| `nombre_cliente` | STRING(100) | Para personalizar mensaje | `María García` | ✅ |
| `fecha_cita` | DATE | Fecha de la cita | `2026-04-15` | ✅ |
| `hora_cita` | TIME | Hora de la cita | `14:30:00` | ✅ |
| `servicio` | STRING(200) | Tipo de servicio solicitado | `Consulta general` | ✅ |
| `google_event_id` | STRING | ID del evento en Google Calendar | `abc123xyz...` | ✅ |
| `estado_cita` | ENUM | pendiente / confirmada / cancelada / completada | `confirmada` | ✅ |
| `recordatorio_enviado` | BOOLEAN | Si ya se envió el recordatorio | `false` | ✅ |
| `created_at` | TIMESTAMP | Cuándo se creó el registro | `2026-04-13 10:30:00` | ✅ |

---

#### Tabla: `mensajes_log` (o Hoja: "Log_Mensajes")

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `id` | UUID | Identificador | `log-001` |
| `telefono` | STRING | Número del remitente | `+52155xxxxxxxx` |
| `tipo` | ENUM | entrante / saliente | `entrante` |
| `contenido_hash` | STRING | Hash del contenido (no el texto real) | `sha256:abc...` |
| `timestamp` | TIMESTAMP | Cuándo ocurrió | `2026-04-13 10:30:00` |
| `flujo_activado` | STRING | Qué flujo procesó el mensaje | `flujo-agendado` |
| `tokens_usados` | INTEGER | Tokens de Claude consumidos | `450` |
| `costo_usd` | DECIMAL | Costo de este mensaje | `0.0002` |

> **Nota de privacidad:** Los contenidos de mensajes NO se almacenan en texto claro. Solo se guarda el hash para auditoría.

---

### INTEGRACIONES CON APIs EXTERNAS

#### WhatsApp Business API (Meta)

```
Endpoint base:    https://graph.facebook.com/v18.0/
Autenticación:    Bearer Token (WHATSAPP_API_TOKEN)
Rate limit:       1,000 mensajes/día (tier 1 por defecto)
Webhooks:         POST /webhook/whatsapp → n8n

Eventos que escuchamos:
  - messages (mensajes de usuarios)
  - message_status (entregado, leído)

Eventos que ignoramos:
  - contacts (cambios de perfil)
  - account_alerts

Documentación oficial:
  https://developers.facebook.com/docs/whatsapp/cloud-api
```

---

#### Google Calendar API v3

```
Endpoint base:    https://www.googleapis.com/calendar/v3/
Autenticación:    OAuth 2.0 (service account o user OAuth)
Scopes requeridos:
  - https://www.googleapis.com/auth/calendar
  - https://www.googleapis.com/auth/calendar.events

Operaciones que usamos:
  - GET /calendars/{calendarId}/events — listar eventos
  - POST /calendars/{calendarId}/events — crear evento
  - DELETE /calendars/{calendarId}/events/{eventId} — eliminar

Formato de fecha:  RFC3339 (2026-04-15T14:30:00-06:00)
Zona horaria:      America/Mexico_City
```

---

#### Claude API (Anthropic)

```
Endpoint:         https://api.anthropic.com/v1/messages
Modelo usado:     claude-haiku-4-5-20251001
Autenticación:    x-api-key: ANTHROPIC_API_KEY

Parámetros de llamada típica:
  max_tokens: 500
  temperature: 0.3 (respuestas consistentes)
  system: [Prompt del sistema — ver Blueprint]

Costos aproximados (Haiku):
  Input:  $0.80 USD / millón de tokens
  Output: $4.00 USD / millón de tokens

Prompt caching activado: Sí (el system prompt se cachea)
```

---

### FLUJO DE DATOS (Técnico)

```
[WhatsApp] → [Webhook en Railway] → [n8n Trigger]
                                          │
                                          ▼
                              [Extraer: telefono, mensaje, timestamp]
                                          │
                                          ▼
                              [Buscar cliente en DB]
                                          │
                              ┌───────────┴───────────┐
                           Existe                  No existe
                              │                       │
                              ▼                       ▼
                    [Cargar contexto]          [Crear registro]
                              │                       │
                              └───────────┬───────────┘
                                          ▼
                              [Clasificar intención con Claude]
                                          │
                         ┌────────────────┼────────────────┐
                      FAQ                Cita            Escalado
                         │               │                │
                         ▼               ▼                ▼
                   [Respuesta]    [Flujo Calendar]   [Notif. dueño]
                         │               │                │
                         └───────────────┼────────────────┘
                                         ▼
                              [Enviar respuesta WhatsApp]
                                         │
                                         ▼
                              [Log en DB — hash del mensaje]
```

---

### RETENCIÓN Y ELIMINACIÓN DE DATOS

| Tipo de dato | Retención | Proceso de eliminación |
|--------------|-----------|------------------------|
| Datos de clientes | Indefinida (mientras el retainer esté activo) | Manual desde Sheets/Supabase |
| Log de mensajes | 90 días | Limpieza automática mensual |
| Contenido de mensajes | No se almacena | N/A |
| Tokens de API | No se almacenan | N/A |
| Eventos de Google Calendar | Controlado por el cliente | Desde Google Calendar |

---

*Folio: RYV-DICT-[AÑO]-[NÚMERO] | The Stack / The Scribe | Ryventis Solutions*
