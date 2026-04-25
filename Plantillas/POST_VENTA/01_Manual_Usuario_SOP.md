# MANUAL DE USUARIO — GUÍA DE OPERACIÓN
**Plantilla:** POST_VENTA-01 | **Agente responsable:** 🟢 The Bridge / ⚪ The Scribe  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** Personalizar con el nombre del cliente, capturas de pantalla reales del sistema y los flujos específicos implementados. Entregar al cliente en PDF y en versión editable.

---

# MANUAL DE USUARIO
## Tu Sistema de [NOMBRE DEL SERVICIO]
### [NOMBRE DEL NEGOCIO]

**Elaborado por:** Ryventis Solutions  
**Fecha de entrega:** [FECHA]  
**Versión del sistema:** v[X.X]

---

## BIENVENIDA

> Felicidades, **[NOMBRE DEL DUEÑO]**. Tu sistema ya está funcionando.
>
> Este manual te explica, en lenguaje simple, cómo convivir con tu nuevo sistema de automatización. No necesitas ser experto en tecnología — si puedes usar WhatsApp, puedes usar esto.
>
> Guarda este documento. Si algo no funciona como esperas o tienes una duda, aquí encontrarás la respuesta.

**Soporte disponible:**  
📱 WhatsApp de Ryventis: [NÚMERO]  
🕐 Horario: Lunes a Viernes, 9am – 7pm  
⚡ Urgencias (sistema caído): 24/7 — WhatsApp

---

## PARTE 1 — CÓMO FUNCIONA TU SISTEMA

### ¿Qué hace tu bot automáticamente?

Tu sistema hace estas cosas sin que tú tengas que tocar el teléfono:

| ¿Qué pasa? | ¿Qué hace el sistema? |
|-----------|----------------------|
| Un cliente escribe "Hola" | El bot saluda y muestra las opciones disponibles |
| Un cliente pregunta [PREGUNTA FRECUENTE 1] | El bot responde con la información correcta |
| Un cliente pregunta [PREGUNTA FRECUENTE 2] | El bot responde automáticamente |
| Un cliente quiere agendar una cita | El bot verifica disponibilidad y confirma |
| 24 horas antes de una cita | El bot manda un recordatorio al cliente |
| Un cliente tiene una queja compleja | Te avisa a ti directamente |

### ¿Cuándo interviene un humano (tú o tu equipo)?

El bot **NUNCA** toma decisiones importantes solo. Siempre te avisa cuando:

- Un cliente tiene una queja que no puede resolver
- El cliente pide hablar con el dueño directamente
- La situación es demasiado específica para respuesta automática

**Cuando el bot te avisa**, recibirás un mensaje como este:
```
🔔 CASO HUMANO — [NOMBRE DEL NEGOCIO]
Cliente: [nombre]
Número: [teléfono]
Mensaje: "[lo que dijo el cliente]"
Acción: Comunícate con este cliente directamente
```

---

## PARTE 2 — TU DASHBOARD (Si aplica)

### Dónde ver tus datos

Todos los registros de tus clientes están en:

**Google Sheets:** [NOMBRE DEL ARCHIVO]  
**Link directo:** [URL DEL ARCHIVO — si aplica]

### Las hojas que tienes

#### Hoja "Clientes"
Aquí aparece cada persona que ha escrito al bot.

| Columna | ¿Qué significa? |
|---------|----------------|
| Nombre | Cómo se presentó el cliente |
| Teléfono | Su número de WhatsApp |
| Primera visita | Cuándo escribió por primera vez |
| Estado | "activo" = cliente actual, "lead" = interesado, "inactivo" = no ha escrito en mucho tiempo |
| Notas | Puedes agregar comentarios aquí (columna libre para ti) |

> **Importante:** No borres ni modifiques las columnas con fondo de color. Son las que el sistema usa. La columna "Notas" es libre — puedes escribir lo que quieras ahí.

#### Hoja "Citas"
Todas las citas agendadas por el bot aparecen aquí Y en tu Google Calendar.

| Columna | ¿Qué significa? |
|---------|----------------|
| Nombre del cliente | ¿A quién le agendó? |
| Fecha y hora | ¿Cuándo? |
| Servicio | ¿Qué pidió? |
| Estado | pendiente / confirmada / cancelada |
| Recordatorio enviado | ✅ = ya le mandó el recordatorio, ❌ = aún no |

---

## PARTE 3 — TU GOOGLE CALENDAR

El sistema agrega y elimina citas en tu Google Calendar automáticamente.

### Cómo ver tus citas

1. Abre Google Calendar desde tu teléfono o computadora
2. Las citas del bot aparecen con el color [COLOR] y el título "[FORMATO DE CITA]"
3. Al hacer clic en la cita, ves el nombre y teléfono del cliente

### Si necesitas cancelar una cita manualmente

1. Abre la cita en Google Calendar
2. Haz clic en "Eliminar"
3. El bot **no enviará recordatorio** automáticamente si la cita no existe en el calendario
4. Se recomienda avisar al cliente directamente por WhatsApp cuando canceles manualmente

---

## PARTE 4 — PREGUNTAS FRECUENTES

### ¿Qué hago si el bot responde algo incorrecto?

1. Anota el mensaje exacto que el cliente envió
2. Anota qué respondió el bot (puede verse en el chat del número)
3. Manda esa info a Ryventis por WhatsApp
4. Lo corregimos en menos de 24 horas

---

### ¿Puedo hablar yo directamente desde el mismo número que usa el bot?

**Sí, pero con cuidado:**  
- Si escribes desde el número del bot, el sistema puede confundirse
- Recomendamos responder a los clientes que el bot escala, no usar el número para iniciar conversaciones
- Si necesitas escribirle a un cliente desde ese número, hazlo normalmente — el bot solo responde cuando le escriben al número, no interrumpe conversaciones activas tuyas

---

### ¿Qué pasa si WhatsApp se cae?

WhatsApp (Meta) tiene sus propios problemas técnicos ocasionales que no dependen de Ryventis. Cuando pasa:
- El bot no puede recibir ni enviar mensajes
- Ryventis monitorea esto y te avisa si hay una interrupción mayor
- Cuando WhatsApp vuelve, el bot retoma normalmente

Para verificar el estado de WhatsApp: [ryventis te lo comunica o consulta metastatus.com]

---

### ¿Puedo agregar preguntas frecuentes nuevas al bot?

**Sí.** Cada mes (incluido en tu retainer), puedes pedir hasta [X] ajustes menores.  
Para agregar una pregunta frecuente:
1. Escríbele a Ryventis: "Quiero agregar esta respuesta al bot"
2. Dinos: la pregunta que hacen los clientes + la respuesta correcta
3. Lo tenemos listo en 24 horas hábiles

---

### ¿El bot funciona los fines de semana y días festivos?

**Sí, el bot funciona 24/7, 365 días al año.**

Si quieres que el bot NO agende citas en días festivos, avísanos con anticipación y lo bloqueamos en el calendario.

---

### ¿Qué pasa con mi sistema si cancelo el retainer?

- El sistema **sigue funcionando** — es tuyo
- Dejas de tener soporte activo y ajustes mensuales
- Si algo falla, podemos ayudarte con una cotización por hora

---

## PARTE 5 — LÍMITES DEL SISTEMA (Lo que el bot NO hace)

Para que no haya confusiones:

- ❌ El bot no cobra pagos ni procesa transacciones bancarias
- ❌ El bot no hace diagnósticos médicos ni da consejos especializados
- ❌ El bot no puede ver tu inventario en tiempo real (a menos que esté integrado)
- ❌ El bot no manda mensajes a clientes que no le hayan escrito primero (excepto los recordatorios de citas ya agendadas)
- ❌ El bot no puede iniciar conversaciones nuevas con personas que no estén en tu lista

---

## PARTE 6 — CONTACTO Y SOPORTE

**Para soporte regular (ajustes, preguntas, mejoras):**  
📱 WhatsApp: [NÚMERO DE RYVENTIS]  
🕐 Lunes a Viernes, 9am – 7pm  
⏱️ Respuesta en menos de 4 horas hábiles

**Para urgencias (sistema completamente caído):**  
📱 WhatsApp: [NÚMERO DE URGENCIAS]  
🕐 24/7  
⏱️ Respuesta en menos de 2 horas

**Para solicitar cambios de alcance (nuevas funciones):**  
1. Descríbenos por WhatsApp qué necesitas
2. Te enviamos una cotización en 24 horas
3. Decides si lo quieres

---

## GLOSARIO (Por si suena a chino)

| Término | ¿Qué significa en simple? |
|---------|--------------------------|
| Bot | El "empleado digital" que responde por WhatsApp |
| Webhook | La "antena" que recibe los mensajes y los manda al sistema |
| n8n | El "cerebro" que procesa todo (no necesitas saber usarlo) |
| API de WhatsApp | El permiso oficial de Meta para que el bot use tu número |
| Google Calendar | Tu agenda digital — donde se guardan las citas |
| Retainer | La cuota mensual de soporte y mantenimiento |

---

**Versión:** 1.0 | **Fecha:** [FECHA] | **Ryventis Solutions**  
*"Tecnología que trabaja para ti"*  
ryventis.mx
