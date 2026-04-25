# DOCUMENTACIÓN TÉCNICA DEL PROYECTO — RYVENTIS SOLUTIONS
**Plantilla:** TECNICO-05 | **Agente responsable:** 🟠 The Stack → ⚪ The Scribe  
**Versión:** 1.0 | **Fecha de creación:** 2026-04-13  
**Instrucciones de uso:** The Stack completa este documento al CERRAR cada proyecto. Es la memoria técnica permanente. The Scribe lo archiva en Documentacion/. En el futuro, antes de iniciar un proyecto similar, consultar este archivo primero.

---

# DOCUMENTACIÓN TÉCNICA POST-ENTREGA
## [NOMBRE DEL PROYECTO] — [NOMBRE DEL CLIENTE]

| Campo | Valor |
|-------|-------|
| Folio del proyecto | RYV-OT-[AÑO]-[NÚMERO] |
| Fecha de entrega | [FECHA] |
| Fecha de documentación | [FECHA] |
| Tiempo total invertido | _____ horas |
| Versión entregada | v[X.X] |

---

## 1. RESUMEN DEL PROYECTO

**¿Qué se construyó?**  
[1-2 párrafos describiendo el sistema entregado, en términos técnicos. Esta sección es para futuros desarrolladores de Ryventis, no para el cliente.]

**¿Cuál era el problema del cliente?**  
[Descripción del problema operativo que motivó el proyecto]

**¿Cómo lo resuelve el sistema?**  
[Descripción técnica de la solución implementada]

---

## 2. STACK TECNOLÓGICO FINAL

| Herramienta | Versión / Plan | Propósito | ¿Pagado por quién? |
|-------------|---------------|-----------|-------------------|
| n8n | _____ | Orquestación | ☐ Ryventis ☐ Cliente |
| WhatsApp Business API | _____ | Mensajería | ☐ Ryventis ☐ Cliente |
| Claude API | _____ | IA respuestas | ☐ Ryventis ☐ Cliente |
| Railway | _____ | Hosting | ☐ Ryventis ☐ Cliente |
| Google Calendar | _____ | Citas | ☐ Ryventis ☐ Cliente |
| [Herramienta] | _____ | _____ | ☐ Ryventis ☐ Cliente |

**Costo operativo mensual real:** $_____ MXN/mes  
**Costo operativo estimado original:** $_____ MXN/mes  
**Diferencia:** [Por encima / Por debajo / Exacto]

---

## 3. ARQUITECTURA IMPLEMENTADA

### Flujos de n8n creados:

| Nombre del flujo | Tipo | Propósito | Nodos principales |
|------------------|------|-----------|------------------|
| [flow-nombre-1] | Webhook | [propósito] | [nodo1, nodo2, nodo3] |
| [flow-nombre-2] | Cron | [propósito] | [nodo1, nodo2] |
| [flow-nombre-3] | Manual | [propósito] | [nodo1] |

### Credenciales de n8n configuradas:

| Tipo de credencial | Nombre en n8n | Propietario |
|-------------------|---------------|-------------|
| WhatsApp API | `wa_[cliente]_prod` | ☐ Ryventis ☐ Cliente |
| Google Calendar | `gc_[cliente]_prod` | ☐ Ryventis ☐ Cliente |
| HTTP Header Auth | `anthropic_api` | Ryventis |
| [Otro] | _____ | _____ |

---

## 4. ESTRUCTURA DE DATOS FINAL

*Documentar la estructura real como quedó en producción (puede diferir del diccionario inicial)*

### Base de datos / Google Sheets

**Hoja/Tabla 1:** [Nombre]
```
Columnas: [lista de columnas separadas por coma]
Registros actuales al entregar: [número]
Acceso del cliente: ☐ Editor ☐ Viewer
```

**Hoja/Tabla 2:** [Nombre]
```
Columnas: [lista de columnas]
```

---

## 5. DECISIONES TÉCNICAS TOMADAS Y PORQUÉ

*Esta sección es crucial para no repetir errores o re-descubrir decisiones ya evaluadas*

### Decisión 1: [Nombre de la decisión]

```
Contexto: [Qué problema había]
Opciones evaluadas:
  A) [Opción A] — Pros: _____ | Contras: _____
  B) [Opción B] — Pros: _____ | Contras: _____

Decisión tomada: [Opción elegida]
Razón: [Por qué se eligió]
Resultado: [Funcionó bien / Requirió ajuste / No funcionó]
```

### Decisión 2: [Nombre de la decisión]

```
[Repetir estructura]
```

---

## 6. PROBLEMAS ENCONTRADOS Y SOLUCIONES

*Base de conocimiento para proyectos futuros*

### Problema 1: [Título del problema]

```
Descripción: [Qué pasó]
Síntoma: [Cómo se manifestó — error específico, comportamiento inesperado]
Causa raíz: [Por qué ocurrió]
Solución aplicada: [Paso a paso de cómo se resolvió]
Tiempo de diagnóstico: _____ minutos
Tiempo de resolución: _____ minutos
¿Prevenible?: ☐ Sí — Cómo: _____ ☐ No
Relevancia para proyectos futuros: [Alta / Media / Baja]
```

### Problema 2: [Título del problema]

```
[Repetir estructura]
```

---

## 7. OPTIMIZACIONES REALIZADAS POST-QA

| Optimización | Motivación | Impacto medido |
|--------------|-----------|----------------|
| [Optimización 1] | [Por qué] | [Resultado medible] |
| [Optimización 2] | [Por qué] | [Resultado medible] |

---

## 8. MÉTRICAS DE RENDIMIENTO EN PRODUCCIÓN (Semana 1)

| Métrica | Valor medido | Meta original | ¿Alcanzada? |
|---------|-------------|---------------|-------------|
| Tiempo promedio de respuesta | _____ seg | < 5 seg | ☐ |
| Mensajes procesados día 1 | _____ | _____ estimado | N/A |
| Costo promedio por conversación | $_____ USD | < $0.01 | ☐ |
| Errores en primeros 7 días | _____ | 0 críticos | ☐ |
| Tokens promedio por conversación | _____ | _____ | ☐ |

---

## 9. INSTRUCCIONES PARA FUTURO MANTENIMIENTO

*Para The Stack o cualquier técnico que tome este proyecto después*

### Para actualizar el sistema:

```
1. Acceder a n8n: [URL del servidor Railway]
   Credenciales: en Railway environment variables

2. Antes de cualquier cambio en producción:
   a) Exportar copia del flujo (botón Export en n8n)
   b) Hacer el cambio
   c) Probar con número de staging

3. Flujos críticos que NO modificar sin QA completo:
   - [Nombre del flujo principal]
   - [Nombre del flujo de recordatorios]

4. Variables de entorno en Railway:
   [URL de Railway del proyecto]
```

### Para resolver los errores más comunes:

```
Error: [Mensaje de error más común]
Causa: [Por qué ocurre]
Solución rápida: [Pasos para resolverlo]

Error: [Otro mensaje de error]
Causa: [Por qué ocurre]
Solución rápida: [Pasos]
```

---

## 10. TRANSFERENCIA DE CONOCIMIENTO AL CLIENTE

| Tema cubierto en capacitación | ¿Cubierto? | Reacción del cliente |
|-------------------------------|-----------|----------------------|
| Cómo funciona el bot básico | ☐ | |
| Cómo ver las citas en Google Calendar | ☐ | |
| Cómo ver los datos en Sheets/Supabase | ☐ | |
| Qué hacer cuando un cliente escala (caso humano) | ☐ | |
| Cómo reportar un problema a Ryventis | ☐ | |
| Qué NO hacer (cambiar cosas sin avisar) | ☐ | |

**Nivel de comprensión del cliente al finalizar capacitación:**
- ☐ Alto — entiende todo perfectamente
- ☐ Medio — entiende los conceptos básicos
- ☐ Bajo — necesitará soporte frecuente en el retainer

---

## 11. LECCIONES APRENDIDAS

**¿Qué funcionó mejor de lo esperado?**
```
[Descripción]
```

**¿Qué fue más difícil de lo esperado?**
```
[Descripción]
```

**¿Qué haría diferente en el próximo proyecto similar?**
```
[Descripción]
```

**¿Qué plantilla o componente se puede reutilizar en proyectos futuros?**
```
[Descripción — nombre del componente, dónde está guardado]
```

---

## 12. ESTADO FINAL DEL PROYECTO

```
☐ ✅ ENTREGADO Y FUNCIONANDO
  Fecha de entrega: _______________________
  Saldo cobrado: ☐ Sí ☐ Pendiente
  Retainer activo: ☐ Sí — $_____ MXN/mes ☐ No

☐ 📄 DOCUMENTADO POR THE SCRIBE
  Fecha de archivo: _______________________
  Ubicación: Documentacion/[NOMBRE-PROYECTO]/

☐ 💰 CICLO FINANCIERO CERRADO (The Treasurer)
  Total cobrado: $_____ MXN
  Margen real: _____% (estimado: ____%)
```

---

*Folio: RYV-DOC-[AÑO]-[NÚMERO] | The Stack → The Scribe | Ryventis Solutions*
