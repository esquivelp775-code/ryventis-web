# EduAI Platform — Stack Tecnológico

## Arquitectura del MVP

```
[Usuario] → [Next.js Frontend] → [API Route] → [Whisper API] → [Claude API] → [Supabase] → [PDF generado]
```

## Stack seleccionado

| Capa | Tecnología | Razón |
|------|-----------|-------|
| Frontend | **Next.js 14 (App Router)** | SSR + API routes en un solo proyecto, deploy sencillo en Vercel/Railway |
| Estilos | **Tailwind CSS** | Velocidad de desarrollo, responsive por defecto |
| Backend/API | **Next.js API Routes** | Evita un servidor separado para el MVP |
| Transcripción | **OpenAI Whisper API** (`whisper-1`) | Mejor calidad en español de todos los modelos open source |
| Generación de resumen | **Claude Sonnet 4.x** | Mejor razonamiento para síntesis académica, costo razonable |
| Base de datos | **Supabase (PostgreSQL)** | Gratis hasta 500MB, auth incluido, storage para archivos |
| Storage de audio | **Supabase Storage** | Guardar archivos subidos temporalmente (24h luego se eliminan) |
| Autenticación | **Supabase Auth** | Email/password + magic link |
| Hosting | **Railway** | Ya en el stack de Ryventis, fácil de desplegar Next.js |
| Generación PDF | **@react-pdf/renderer** o **puppeteer** | Exportar resultado como PDF descargable |

## Esquema de base de datos (MVP)

```sql
-- Usuarios
users (id, email, created_at, credits_remaining)

-- Procesados
processings (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users,
  file_name TEXT,
  file_url TEXT,          -- URL temporal en Supabase Storage
  context TEXT,           -- contexto opcional del usuario
  transcript TEXT,        -- transcripción completa
  summary TEXT,           -- resumen ejecutivo
  key_points JSONB,       -- array de bullet points
  review_questions JSONB, -- array de preguntas
  status TEXT,            -- pending | processing | done | error
  created_at TIMESTAMP,
  expires_at TIMESTAMP    -- 30 días para usuarios gratis
)
```

## Estimación de costos por procesamiento (1 hora de audio)

| Concepto | Costo estimado |
|----------|---------------|
| Whisper API (1h audio) | ~$0.36 USD (~$7 MXN) |
| Claude Sonnet (resumen de transcripción ~15,000 tokens) | ~$0.045 USD (~$0.9 MXN) |
| Supabase Storage (archivo temporal) | ~$0.001 USD |
| **Total por procesamiento** | **~$0.40 USD (~$8 MXN)** |

Con precio de venta de $25 MXN/hora, margen bruto ≈ 68%.

## Roadmap técnico

### Semana 5–6 (mayo 2026) — Setup inicial
- [ ] Crear repositorio en GitHub: `eduai-platform`
- [ ] Setup Next.js 14 + Tailwind + Supabase client
- [ ] Crear esquema de base de datos en Supabase
- [ ] Configurar Supabase Auth (email)
- [ ] Configurar Supabase Storage bucket `audio-files`

### Semana 7–8 (junio 2026) — Funcionalidad core
- [ ] Página de subida de archivo (drag & drop)
- [ ] API Route: subir archivo → Supabase Storage
- [ ] API Route: llamar Whisper → guardar transcripción
- [ ] API Route: llamar Claude → guardar resumen/puntos/preguntas
- [ ] Página de resultados con URL única

### Semana 9 (antes del 21 jun) — Demo funcional
- [ ] Generación de PDF descargable
- [ ] Deploy en Railway con dominio temporal
- [ ] Prueba completa con archivo real de 60 minutos
- [ ] Demo grabada para mostrar a potenciales usuarios/inversores

## Variables de entorno necesarias

```env
OPENAI_API_KEY=           # Para Whisper API
ANTHROPIC_API_KEY=        # Para Claude
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
```
