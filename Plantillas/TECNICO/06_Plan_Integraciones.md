# PLAN DE INTEGRACIONES DEL SISTEMA — RYVENTIS SOLUTIONS
**Plantilla:** TECNICO-06 | **Agente responsable:** 🟠 The Stack  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Completar ANTES de la reunión técnica con el cliente. Define qué sistemas se van a conectar, qué accesos se necesitan del cliente y qué dependencias externas pueden afectar el proyecto.

---

# PLAN DE INTEGRACIONES
## [NOMBRE DEL PROYECTO] — [NOMBRE DEL CLIENTE]

**Folio:** RYV-INT-[AÑO]-[NÚMERO] | **Fecha:** [FECHA]

---

## RESUMEN DE INTEGRACIONES (Para presentar al cliente)

> Este documento lista todos los sistemas que el bot/automatización de **[NOMBRE DEL NEGOCIO]** necesita conectar. Para cada uno, se indica qué acceso necesitas darnos y cuánto tiempo toma la configuración.

---

## MAPA DE INTEGRACIONES

```
SISTEMAS DEL CLIENTE:
  ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
  │  WhatsApp del   │    │ Google Calendar  │    │  Google Sheets  │
  │    Negocio      │    │  del Negocio     │    │  del Negocio    │
  └────────┬────────┘    └────────┬─────────┘    └────────┬────────┘
           │                      │                        │
           └──────────────────────┼────────────────────────┘
                                  │
                         ┌────────▼────────┐
                         │   SISTEMA       │
                         │   RYVENTIS      │
                         │   (n8n + IA)    │
                         └────────┬────────┘
                                  │
           ┌──────────────────────┼────────────────────────┐
           │                      │                        │
  ┌────────▼────────┐    ┌────────▼─────────┐    ┌────────▼────────┐
  │  Claude API     │    │   Base de Datos  │    │  Railway        │
  │  (Anthropic)    │    │  (Supabase /     │    │  (Hosting)      │
  │                 │    │  Google Sheets)  │    │                 │
  └─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## INTEGRACIÓN 1 — WHATSAPP BUSINESS API

### Información general

| Campo | Detalle |
|-------|---------|
| Proveedor | Meta (Facebook) |
| Tipo | WhatsApp Business Cloud API |
| Costo | Gratuito para las primeras 1,000 conversaciones/mes |
| Tiempo de configuración | 2-4 horas (incluye verificación de Meta) |
| Complejidad | Media |

### ¿Qué necesitamos del cliente?

```
REQUERIMIENTOS:
□ Número de teléfono EXCLUSIVO para el bot (no puede ser el teléfono personal)
  → El número puede ser nuevo o uno existente que se migrará
  → Recomendamos: línea nueva con SIM dedicada o número de VoIP

□ Cuenta de Facebook Business Manager del negocio
  → Si no tiene: la creamos juntos (30 minutos)
  → Requiere: documento de identidad del dueño + RFC de la empresa

□ Página de Facebook del negocio vinculada al Business Manager
  → Si no tiene página de FB: la creamos en 15 minutos

INFORMACIÓN QUE CAPTURAMOS NOSOTROS (no requiere acción del cliente):
  - Phone Number ID: lo obtenemos de Meta Developer
  - Access Token: lo generamos durante la configuración
  - Webhook Verify Token: lo creamos nosotros
```

### Proceso de configuración

```
PASO 1: Crear/acceder al Meta Developer App (Ryventis)
PASO 2: Agregar el número del cliente al Business Manager
PASO 3: Verificar el número con código SMS
PASO 4: Configurar webhook en Meta apuntando a Railway
PASO 5: Probar envío y recepción básica
PASO 6: Configurar templates si se requieren mensajes proactivos
```

### Dependencias y riesgos

| Riesgo | Probabilidad | Mitigación |
|--------|-------------|------------|
| Meta rechaza la cuenta Business | Baja | Documentación completa del negocio |
| Número en lista negra de Meta | Baja | Usar número nuevo si hay historial de spam |
| Demora en verificación de Meta | Media | Iniciar trámite en día 1 del proyecto |
| Cambios de política de Meta API | Baja | Monitorear Meta developers blog |

---

## INTEGRACIÓN 2 — GOOGLE CALENDAR

### Información general

| Campo | Detalle |
|-------|---------|
| Proveedor | Google |
| Tipo | Calendar API v3 + OAuth 2.0 |
| Costo | Gratuito con cuenta Google (límites muy altos) |
| Tiempo de configuración | 1-2 horas |
| Complejidad | Media |

### ¿Qué necesitamos del cliente?

```
REQUERIMIENTOS:
□ Cuenta de Google del negocio (Gmail Business o @gmail.com)
  → Recomendamos Google Workspace para imagen profesional

□ Acceso a Google Calendar que usarán para las citas
  → Durante la configuración, el cliente da acceso a Ryventis por 30 min
  → Después, el acceso queda solo en el sistema automatizado

□ Definición de horarios laborales del negocio:
  Días disponibles: _______________________________
  Hora de apertura: _______________________________
  Hora de cierre: _______________________________
  Tiempo por cita: _______ minutos
  Buffer entre citas: _______ minutos
  Días de descanso: _______________________________
```

### Proceso de configuración

```
PASO 1: Cliente comparte acceso temporal al calendario
PASO 2: Ryventis configura OAuth 2.0 con refresh token
PASO 3: Configurar nodos de n8n (leer/crear/eliminar eventos)
PASO 4: Configurar horarios y slots disponibles
PASO 5: Prueba de agendado completo
PASO 6: Revocar acceso temporal — solo queda el sistema
```

---

## INTEGRACIÓN 3 — BASE DE DATOS (Google Sheets / Supabase)

### ¿Cuándo usar Google Sheets?

- Cliente ya usa Google Workspace
- Equipo necesita ver/editar datos sin conocimiento técnico
- Proyecto de menor complejidad (< 1,000 registros activos)
- Presupuesto ajustado (es gratuito)

### ¿Cuándo usar Supabase?

- Proyectos con volumen alto de datos (> 1,000 transacciones/mes)
- Necesidad de consultas complejas o relaciones entre datos
- Múltiples sistemas escribiendo simultáneamente
- Cuando el cliente quiere escalar a una app móvil en el futuro

### Configuración requerida del cliente

```
GOOGLE SHEETS:
□ Crear carpeta "Ryventis — [NOMBRE DEL NEGOCIO]" en Google Drive
□ Dar acceso de editor al email de servicio de Ryventis
□ No modificar las columnas que creamos (sí pueden agregar filas o leer datos)

SUPABASE:
□ Ryventis crea el proyecto (el cliente no necesita hacer nada)
□ Ryventis entrega credenciales de acceso al final del proyecto
```

---

## INTEGRACIÓN 4 — CLAUDE API (Anthropic)

| Campo | Detalle |
|-------|---------|
| Proveedor | Anthropic |
| Modelo | claude-haiku-4-5-20251001 (por defecto) o claude-sonnet-4-6 |
| Costo | $0.80 / millón tokens input + $4.00 / millón tokens output (Haiku) |
| Tiempo de configuración | 30 minutos |
| Complejidad | Baja (solo API key) |
| Quién paga | Ryventis (incluido en el retainer) |

```
ESTIMADO DE COSTO MENSUAL PARA ESTE PROYECTO:
  Conversaciones/día esperadas: _____
  Tokens promedio/conversación: _____
  Total tokens/mes: _____
  Costo estimado: $_____ USD/mes (≈$_____ MXN)
```

---

## INTEGRACIÓN 5 — [INTEGRACIÓN ESPECÍFICA DEL PROYECTO]

*Copiar esta sección para cada integración adicional*

| Campo | Detalle |
|-------|---------|
| Nombre | [Nombre de la plataforma] |
| Tipo de integración | ☐ API REST ☐ Webhook ☐ OAuth ☐ CSV/Sheets ☐ Otro |
| Documentación oficial | [URL — solo incluir si es necesario para trabajo técnico] |
| Costo | [Gratuito / $X USD/mes] |
| Quién paga | ☐ Ryventis ☐ Cliente |
| Complejidad | ☐ Alta ☐ Media ☐ Baja |
| Tiempo estimado | _____ horas |

**Requerimientos del cliente para esta integración:**
```
□ [Requerimiento 1]
□ [Requerimiento 2]
```

**Riesgos específicos:**
```
- [Riesgo 1]: [Probabilidad] — [Mitigación]
```

---

## PLAN DE ONBOARDING DE INTEGRACIONES

*Orden recomendado para configurar todo sin bloqueos*

```
DÍA 1 (Reunión técnica con el cliente):
  [ ] Verificar cuenta de WhatsApp Business disponible
  [ ] Obtener acceso temporal a Google Calendar
  [ ] Confirmar que el número de WhatsApp del negocio está listo
  [ ] Resolver dudas sobre el alcance técnico

DÍA 1-2 (Ryventis trabaja solo):
  [ ] Configurar Meta Developer App + webhook
  [ ] Configurar OAuth Google Calendar
  [ ] Crear estructura de base de datos
  [ ] Configurar variables de entorno en Railway
  [ ] Primer flujo básico funcionando (prueba interna)

DÍA 2-3 (Desarrollo y pruebas):
  [ ] Completar todos los flujos
  [ ] QA completo (TECNICO-02)
  [ ] Revocar accesos temporales — solo quedan permanentes

DÍA 3 (Entrega):
  [ ] Deploy a producción (TECNICO-04)
  [ ] Prueba de humo con el cliente
  [ ] Capacitación
```

---

## REGISTRO DE ACCESOS ENTREGADOS AL CLIENTE

*Documentar todos los accesos que el cliente tiene al finalizar el proyecto*

| Plataforma | Usuario | Tipo de acceso | ¿Puede modificar el sistema? |
|------------|---------|---------------|------------------------------|
| Google Calendar | [email del cliente] | Editor | Sí — solo el contenido del calendario |
| Google Sheets | [email del cliente] | Editor | Solo columnas de notas y estado |
| Railway | No aplica | Sin acceso directo | No |
| n8n | No aplica | Sin acceso directo | No |
| WhatsApp | [número del negocio] | Propietario del número | Sí |

**Credenciales de la cuenta Meta Developer:**
```
Quién tiene acceso: Ryventis Solutions (para soporte)
En caso de cancelar el retainer: [protocolo de transferencia]
```

---

*Folio: RYV-INT-[AÑO]-[NÚMERO] | The Stack | Ryventis Solutions*
