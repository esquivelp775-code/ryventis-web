# CHECKLIST DE DESPLIEGUE A PRODUCCIÓN — RYVENTIS SOLUTIONS
**Plantilla:** TECNICO-04 | **Agente responsable:** 🟠 The Stack  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Completar secuencialmente ANTES de hacer el deploy a producción. Si cualquier punto marcado con 🔴 no se cumple, NO desplegar. Este checklist es la última línea de defensa antes de que el cliente use el sistema.

---

# CHECKLIST DE DEPLOY A PRODUCCIÓN

| Campo | Valor |
|-------|-------|
| Proyecto | [NOMBRE DEL CLIENTE] |
| Entorno | ☐ Staging → ☐ Producción |
| Fecha de deploy | [FECHA] [HORA] |
| Responsable | The Stack |
| QA previo completado | ☐ Sí — Folio: RYV-QA-[AÑO]-[NÚMERO] |

---

## FASE 1 — PRE-DEPLOY: CÓDIGO Y CONFIGURACIÓN

### 1.1 Limpieza del código

| Item | Sev. | Estado | Notas |
|------|------|--------|-------|
| No hay credenciales hardcodeadas en ningún nodo | 🔴 | ☐ | |
| Todas las API keys están en variables de entorno | 🔴 | ☐ | |
| No hay datos de staging/prueba en la configuración | 🔴 | ☐ | |
| Números de teléfono de prueba removidos o comentados | 🔴 | ☐ | |
| Logs de debug desactivados o filtrados | 🟠 | ☐ | |
| URLs de entornos de prueba reemplazadas por producción | 🔴 | ☐ | |

---

### 1.2 Variables de entorno — Verificación

*Verificar que TODAS estas variables están configuradas en Railway / plataforma de hosting:*

| Variable | Configurada | Valor de prueba borrado |
|----------|-------------|------------------------|
| WHATSAPP_API_TOKEN | ☐ | ☐ |
| WHATSAPP_PHONE_NUMBER_ID | ☐ | ☐ |
| WHATSAPP_WEBHOOK_VERIFY_TOKEN | ☐ | ☐ |
| ANTHROPIC_API_KEY | ☐ | ☐ |
| GOOGLE_REFRESH_TOKEN | ☐ | ☐ |
| GOOGLE_CALENDAR_ID | ☐ | ☐ |
| DATABASE_URL | ☐ | ☐ |
| N8N_WEBHOOK_URL | ☐ | ☐ |
| [Variable específica del proyecto] | ☐ | ☐ |

---

### 1.3 Flujos de n8n

| Item | Sev. | Estado |
|------|------|--------|
| Todos los flujos están en estado "Active" | 🔴 | ☐ |
| Flujo principal tiene manejo de errores en cada nodo crítico | 🔴 | ☐ |
| Flujo de recordatorios tiene el cron configurado en zona horaria correcta (America/Mexico_City) | 🔴 | ☐ |
| No hay flujos de prueba activos que puedan interferir | 🟠 | ☐ |
| Todos los webhooks apuntan a la URL de producción | 🔴 | ☐ |
| Timeout de nodos HTTP configurado (no infinito) | 🟠 | ☐ |

---

## FASE 2 — INFRAESTRUCTURA

### 2.1 Railway / Hosting

| Item | Sev. | Estado | Notas |
|------|------|--------|-------|
| Servicio de n8n iniciado y estable (verde en Railway) | 🔴 | ☐ | |
| Memoria utilizada < 80% del plan contratado | 🟠 | ☐ | |
| SSL/HTTPS activo en el dominio del webhook | 🔴 | ☐ | |
| Restart policy configurada (reiniciar si falla) | 🔴 | ☐ | |
| Health check endpoint respondiendo | 🟠 | ☐ | |
| Logs de Railway accesibles y sin errores | 🟠 | ☐ | |

---

### 2.2 WhatsApp Business API — Configuración final

| Item | Sev. | Estado |
|------|------|--------|
| Webhook URL de PRODUCCIÓN registrada en Meta Developer | 🔴 | ☐ |
| Webhook verification completada (✅ en Meta) | 🔴 | ☐ |
| Número de teléfono de PRODUCCIÓN del cliente registrado | 🔴 | ☐ |
| Suscripciones de webhook activas: `messages`, `message_status` | 🔴 | ☐ |
| Templates de mensajes aprobados por Meta (si aplica) | 🟠 | ☐ |
| Límite diario de mensajes verificado (tier 1: 1,000/día mínimo) | 🟠 | ☐ |

---

### 2.3 Google Calendar — Permisos

| Item | Sev. | Estado |
|------|------|--------|
| OAuth tokens de PRODUCCIÓN del cliente configurados | 🔴 | ☐ |
| Calendar ID de producción (no el de pruebas) | 🔴 | ☐ |
| Service account tiene permisos de editor en el calendario | 🔴 | ☐ |
| Zona horaria del calendario: America/Mexico_City | 🔴 | ☐ |

---

## FASE 3 — PRUEBA DE HUMO POST-DEPLOY

*Pruebas rápidas para confirmar que el deploy fue exitoso. Ejecutar en producción ANTES de avisar al cliente.*

| Prueba de humo | Procedimiento | Resultado | ☐ Pasa |
|----------------|--------------|-----------|--------|
| Mensaje básico | Enviar "Hola" desde número de prueba | Bot responde en < 5 seg | ☐ |
| FAQ básico | Preguntar algo del negocio | Respuesta correcta | ☐ |
| Agendado básico | Pedir una cita para mañana | Cita creada en Calendar | ☐ |
| Logs limpios | Ver Railway logs 5 min post-prueba | Sin errores 500 | ☐ |
| Costo de tokens | Revisar consumo API Claude | < $0.01 USD por conversación | ☐ |

---

## FASE 4 — DOCUMENTACIÓN FINAL ANTES DE ENTREGA

| Entregable | Destinatario | Estado |
|------------|-------------|--------|
| Blueprint actualizado con cambios de producción | The Scribe | ☐ |
| Variables de entorno documentadas (sin valores) | The Scribe | ☐ |
| Manual de usuario listo (POST_VENTA-01) | Cliente | ☐ |
| Diccionario de datos completado (TECNICO-03) | Cliente / Scribe | ☐ |
| Credenciales del cliente documentadas de forma segura | Treasurer | ☐ |
| Costo operativo mensual real calculado | Treasurer | ☐ |

---

## FASE 5 — NOTIFICACIONES POST-DEPLOY

| Acción | Estado |
|--------|--------|
| Notificar a The Driver: "Deploy completado — listo para entrega al cliente" | ☐ |
| Notificar a The Treasurer: "Sistema en producción — proceder con coordinación de saldo" | ☐ |
| Notificar a The Bridge: "Iniciar protocolo de entrega y onboarding (POST_VENTA-01)" | ☐ |
| Notificar a The Scribe: "Archivar Blueprint + QA + Diccionario" | ☐ |

---

## ROLLBACK PLAN (si algo sale mal en producción)

```
Si el sistema falla en producción dentro de las primeras 2 horas:

PASO 1: Desactivar flujos en n8n (no borrar — solo desactivar)
PASO 2: Notificar al cliente: "Detectamos un ajuste necesario, resolvemos en 30 min"
PASO 3: Revisar logs de Railway para identificar el error
PASO 4: Corregir en staging, re-testear, re-desplegar
PASO 5: Reactivar flujos

Si la falla es en WhatsApp API:
  - Verificar estado de Meta en https://www.metastatus.com
  - Si es falla de Meta: comunicar al cliente y esperar

Tiempo máximo para comunicar al cliente un fallo: 15 minutos
Tiempo máximo para resolver fallo crítico: 2 horas hábiles
```

---

## VEREDICTO DE DEPLOY

```
☐ ✅ DEPLOY APROBADO
   Todos los ítems críticos verificados. Sistema en producción.
   Fecha/hora: _______________________

☐ ❌ DEPLOY BLOQUEADO
   Hay ítems críticos sin completar.
   Ítems pendientes: _______________________
   Nuevo intento programado para: _______________________
```

**Firma:** _______________________ | **Fecha:** _______________________

---

*Folio: RYV-DEPLOY-[AÑO]-[NÚMERO] | The Stack | Ryventis Solutions*
