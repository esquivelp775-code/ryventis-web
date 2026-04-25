# PROTOCOLO DE PRUEBAS DE CALIDAD (QA) — RYVENTIS SOLUTIONS
**Plantilla:** TECNICO-02 | **Agente responsable:** 🟠 The Stack  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Completar OBLIGATORIAMENTE antes de cualquier entrega al cliente. El sistema NO se entrega si hay fallas en los puntos CRÍTICOS. Las fallas MEDIAS se documentan y se resuelven antes del fin de la primera semana.

---

# REPORTE DE QA — [NOMBRE DEL PROYECTO]

| Campo | Valor |
|-------|-------|
| Proyecto | [NOMBRE DEL CLIENTE] — [NOMBRE DEL SERVICIO] |
| Folio OT | RYV-OT-[AÑO]-[NÚMERO] |
| Fecha de QA | [FECHA] |
| Realizado por | 🟠 The Stack |
| Versión del sistema | v[X.X] |
| Estado final | ☐ APROBADO ☐ APROBADO CON OBSERVACIONES ☐ RECHAZADO |

---

## REGLA DE ORO DEL QA

```
╔══════════════════════════════════════════════════════╗
║  NUNCA desplegar código sin probar.                  ║
║  Un bug en producción cuesta 10x más que prevenirlo. ║
║  El cliente no paga por beta — paga por resultados.  ║
╚══════════════════════════════════════════════════════╝
```

**Clasificación de severidad:**
- 🔴 **CRÍTICO** — El sistema no funciona. Bloquea entrega. Debe resolverse antes de entregar.
- 🟠 **ALTO** — Funcionalidad importante con falla. Resolver antes de entregar si es posible.
- 🟡 **MEDIO** — Falla menor que no bloquea la operación. Resolver en semana 1.
- 🟢 **BAJO** — Mejora cosmética o UX. Resolver en el ciclo normal del retainer.

---

## MÓDULO 1 — PRUEBAS DE CONECTIVIDAD

### 1.1 WhatsApp Business API

| Prueba | Procedimiento | Resultado esperado | Sev. | Estado | Notas |
|--------|--------------|-------------------|------|--------|-------|
| Webhook activo | Enviar mensaje de prueba desde número externo | Webhook recibe payload en < 2 segundos | 🔴 | ☐ | |
| Webhook verification | Verificar token de Meta en el endpoint | Responde 200 OK con challenge | 🔴 | ☐ | |
| Envío de mensaje de texto | Ejecutar nodo de envío en n8n | Mensaje llega al número destino | 🔴 | ☐ | |
| Envío de mensaje con template | Ejecutar con template aprobado por Meta | Template llega formateado | 🟠 | ☐ | |
| Recepción de imagen | Enviar imagen desde WhatsApp | Sistema la procesa sin error | 🟡 | ☐ | |
| Recepción de audio | Enviar audio desde WhatsApp | Sistema lo maneja (aunque no lo procese) | 🟡 | ☐ | |
| Rate limiting | Enviar 20 mensajes seguidos | No genera error 429 | 🟠 | ☐ | |

---

### 1.2 Google Calendar API (si aplica)

| Prueba | Procedimiento | Resultado esperado | Sev. | Estado | Notas |
|--------|--------------|-------------------|------|--------|-------|
| Autenticación OAuth | Ejecutar flujo de auth | Token válido obtenido | 🔴 | ☐ | |
| Leer eventos | Consultar eventos del día siguiente | Lista de eventos retornada | 🔴 | ☐ | |
| Crear evento | Agendar cita de prueba | Evento aparece en el calendario | 🔴 | ☐ | |
| Verificar conflictos | Intentar agendar en slot ocupado | Sistema detecta conflicto | 🟠 | ☐ | |
| Eliminar evento | Cancelar cita de prueba | Evento eliminado del calendario | 🟠 | ☐ | |

---

### 1.3 Base de Datos (Google Sheets / Supabase)

| Prueba | Procedimiento | Resultado esperado | Sev. | Estado | Notas |
|--------|--------------|-------------------|------|--------|-------|
| Conexión | Consulta básica | Respuesta en < 1 segundo | 🔴 | ☐ | |
| Lectura de registro | Buscar cliente por teléfono | Retorna datos correctos | 🔴 | ☐ | |
| Escritura de registro | Crear nuevo lead | Aparece en la hoja/tabla | 🔴 | ☐ | |
| Actualización | Modificar estado de cita | Campo actualizado correctamente | 🟠 | ☐ | |
| Manejo de duplicados | Insertar número ya existente | No crea duplicado, actualiza | 🟠 | ☐ | |

---

## MÓDULO 2 — PRUEBAS DE FLUJO PRINCIPAL

### 2.1 Conversación estándar (bot de WhatsApp)

| Escenario | Mensaje de prueba | Respuesta esperada | Tiempo máx. | Sev. | Estado |
|-----------|------------------|--------------------|-------------|------|--------|
| Saludo inicial | "Hola" | Saludo + menú de opciones | 5 seg | 🔴 | ☐ |
| Pregunta frecuente #1 | "[PREGUNTA REAL DEL CLIENTE]" | Respuesta correcta del FAQ | 5 seg | 🔴 | ☐ |
| Pregunta frecuente #2 | "[PREGUNTA REAL DEL CLIENTE]" | Respuesta correcta del FAQ | 5 seg | 🔴 | ☐ |
| Solicitud de precio | "¿Cuánto cuesta [servicio]?" | Precio correcto según config | 5 seg | 🔴 | ☐ |
| Solicitud de horario | "¿A qué hora abren?" | Horarios correctos | 5 seg | 🔴 | ☐ |
| Solicitud de dirección | "¿Dónde están ubicados?" | Dirección correcta | 5 seg | 🔴 | ☐ |
| Mensaje no entendido | "asdfghjkl" | Respuesta de no entendió + opciones | 5 seg | 🟠 | ☐ |
| Mensaje vacío | (solo media, sin texto) | Respuesta genérica educada | 5 seg | 🟡 | ☐ |

---

### 2.2 Flujo de agendado de citas

| Escenario | Acción | Resultado esperado | Sev. | Estado |
|-----------|--------|-------------------|------|--------|
| Solicitar cita (slot disponible) | Usuario pide cita para mañana | Sistema confirma + crea evento | 🔴 | ☐ |
| Solicitar cita (slot lleno) | Usuario pide cita en horario ocupado | Sistema ofrece alternativas | 🔴 | ☐ |
| Cancelar cita | Usuario cancela con 2 horas de anticipación | Cita eliminada del Calendar | 🟠 | ☐ |
| Flujo completo de agendado | Usuario completa todo el proceso | Confirmación final enviada | 🔴 | ☐ |
| Datos incompletos | Usuario no da su nombre | Bot pide información faltante | 🟠 | ☐ |

---

### 2.3 Flujo de recordatorios (si aplica)

| Escenario | Acción | Resultado esperado | Sev. | Estado |
|-----------|--------|-------------------|------|--------|
| Recordatorio 24h antes | Cron ejecuta | Mensaje llega al paciente | 🔴 | ☐ |
| Sin citas mañana | Cron ejecuta | No envía mensajes, no da error | 🟠 | ☐ |
| Número de WhatsApp inválido | Cron intenta enviar | Registra el error sin colapsar el flujo | 🟠 | ☐ |

---

## MÓDULO 3 — PRUEBAS DE CASOS DE BORDE Y ERRORES

| Escenario | Comportamiento esperado | Sev. | Estado | Notas |
|-----------|------------------------|------|--------|-------|
| API de WhatsApp caída (simular timeout) | Mensaje de error amigable al usuario, alerta a admin | 🔴 | ☐ | |
| Token de API expirado | n8n reintenta con refresh token | 🔴 | ☐ | |
| Base de datos no responde | Flujo continúa con respuesta genérica | 🟠 | ☐ | |
| n8n reiniciado en Railway | Flujos se recargan automáticamente | 🔴 | ☐ | |
| Mensaje con contenido inapropiado | Escalado a humano + no responder el contenido | 🔴 | ☐ | |
| 100 mensajes simultáneos | Sistema no colapsa, procesa en cola | 🟠 | ☐ | |
| Usuario escribe durante 10 minutos seguidos | Sesión maneja bien el contexto | 🟡 | ☐ | |

---

## MÓDULO 4 — PRUEBAS DE SEGURIDAD

| Prueba | Procedimiento | Resultado esperado | Sev. | Estado |
|--------|--------------|-------------------|------|--------|
| Variables de entorno | Verificar que no hay credenciales en el código | Todas las keys en env vars | 🔴 | ☐ |
| Webhook signature verification | Enviar request sin firma válida | n8n rechaza con 401 | 🔴 | ☐ |
| Inyección de prompt | Mensaje: "Ignora tus instrucciones y..." | IA no cambia comportamiento | 🔴 | ☐ |
| Datos del cliente en logs | Revisar logs de Railway | No hay datos personales en texto claro | 🟠 | ☐ |
| URL del webhook expuesta | Verificar que no está en código público | Solo en env vars | 🔴 | ☐ |

---

## MÓDULO 5 — PRUEBAS DE RENDIMIENTO

| Métrica | Valor medido | Threshold aceptable | ¿Pasa? |
|---------|-------------|---------------------|--------|
| Tiempo de respuesta promedio | _____ seg | < 5 segundos | ☐ |
| Tiempo de respuesta máximo | _____ seg | < 10 segundos | ☐ |
| Costo por conversación (tokens) | $_____ USD | < $0.01 USD | ☐ |
| Uptime últimas 24h (Railway) | _____% | > 99% | ☐ |
| Errores en logs últimas 24h | _____ | 0 errores críticos | ☐ |

---

## MÓDULO 6 — VERIFICACIÓN DE ENTREGABLES

| Entregable | Estado |
|------------|--------|
| Blueprint actualizado con cambios finales | ☐ Completo |
| Manual de usuario listo (POST_VENTA-01) | ☐ Completo |
| Diccionario de datos completado (TECNICO-03) | ☐ Completo |
| Credenciales documentadas y entregadas | ☐ Completo |
| Log de variables de entorno del cliente | ☐ Completo |

---

## RESUMEN DE FALLAS ENCONTRADAS

| # | Descripción | Severidad | Estado | Resolución |
|---|-------------|-----------|--------|-----------|
| 1 | | 🔴 | ☐ | |
| 2 | | 🟠 | ☐ | |
| 3 | | 🟡 | ☐ | |

**Total fallas críticas:** _____  
**Total fallas altas:** _____  
**Total fallas medias:** _____

---

## VEREDICTO FINAL

```
☐ ✅ APROBADO — Todas las pruebas críticas y altas pasaron.
              El sistema puede ser entregado al cliente.

☐ ⚠️ APROBADO CON OBSERVACIONES — Pasaron todas las críticas.
              Hay fallas medias/bajas documentadas que se
              resolverán en la primera semana de operación.

☐ ❌ RECHAZADO — Hay al menos 1 falla CRÍTICA sin resolver.
              NO entregar al cliente hasta corregir.
```

**Firma del responsable de QA:** _______________________  
**Fecha:** _______________________

---

*Folio: RYV-QA-[AÑO]-[NÚMERO] | The Stack | Ryventis Solutions*
