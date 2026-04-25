# EduAI Platform — Descripción del MVP

## Flujo del MVP (alcance mínimo para demo funcional)

```
1. Usuario sube archivo de audio (MP3/M4A/WAV, máx 2 horas)
2. Sistema transcribe el audio con Whisper API
3. Claude procesa la transcripción y genera:
   - Resumen ejecutivo (3-5 párrafos)
   - Lista de puntos clave (bullet points)
   - 5-10 preguntas de repaso para estudio
4. Resultado disponible en página web con URL única compartible
5. Usuario puede descargar el resultado como PDF
```

## Funcionalidades del MVP (lo mínimo que debe funcionar)

### Entrada
- Subida de archivo de audio: MP3, M4A, WAV, OGG (máx 120 minutos o 200MB)
- Campo opcional de contexto: "Esta clase es de [materia] sobre [tema]" — mejora la calidad del resumen
- Sin registro requerido para la primera prueba (freemium)

### Procesamiento
- Transcripción vía OpenAI Whisper API (modelo `whisper-1`)
- Idioma: español (detección automática, soporte multiidioma en v2)
- Tiempo estimado de procesamiento: 1-3 minutos por hora de audio

### Salida (página de resultados)
- **Transcripción completa** (texto, con marcas de tiempo opcionales)
- **Resumen ejecutivo** — párrafos cohesivos del contenido principal
- **Puntos clave** — bullet list con los conceptos más importantes
- **Preguntas de repaso** — generadas por IA para facilitar el estudio
- URL única por procesamiento: `eduai.mx/r/[ID]` (válida 30 días gratis)
- Botón de descarga en PDF
- Botón de copiar al portapapeles

### Panel del usuario (básico)
- Registro con email + contraseña
- Historial de procesados (últimos 10 en plan gratis)
- Contador de créditos restantes

## Prompt de Claude para el resumen (candidato inicial)

```
Eres un asistente académico experto. A continuación tienes la transcripción de una clase universitaria.
Tu tarea es generar:

1. RESUMEN EJECUTIVO (3-5 párrafos): Los conceptos principales explicados de forma clara y concisa.
2. PUNTOS CLAVE (8-12 bullets): Los conceptos, términos o ideas más importantes.
3. PREGUNTAS DE REPASO (5-8 preguntas): Preguntas que un profesor podría usar en un examen sobre este material.

Transcripción:
[TRANSCRIPCION]

Contexto adicional del estudiante: [CONTEXTO_OPCIONAL]
```

## Métricas de éxito del MVP

- Al menos 1 usuario externo (no Pablo) completa el flujo de inicio a fin
- El resumen generado es evaluado como "útil" por el usuario
- El tiempo de procesamiento < 5 minutos para 1 hora de audio
- La app no falla con archivos de 60+ minutos

## Fuera del MVP

- Procesamiento de video (extraer audio de MP4)
- Notas colaborativas (varios estudiantes ven el mismo resumen)
- Integración con Google Drive para subir directamente
- Flashcards automáticas (Anki-compatible)
- Análisis de asistencia a temas por clase
