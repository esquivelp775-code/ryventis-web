# NFC MedID — Stack Tecnológico

## Hardware (tarjeta física)

| Componente | Opción A | Opción B | Decisión |
|------------|----------|----------|---------|
| Chip NFC | NTAG216 (888 bytes) | NTAG215 (504 bytes) | **NTAG216** — más capacidad |
| Formato | CR80 PVC 0.76mm | PET flexible | PVC por durabilidad |
| QR | Impreso al reverso | Sticker adicional | Impreso (más limpio) |
| Proveedor MX candidato | NFC México (CDMX) | Alibaba (importación) | Investigar en semana 1 |

## Backend (plataforma web)

| Capa | Tecnología | Razón |
|------|-----------|-------|
| Base de datos | **Supabase (PostgreSQL)** | Ya en el stack de Ryventis, row-level security nativo, gratis hasta 500MB |
| Autenticación | **Supabase Auth** | Email/password + magic link, sin costo adicional |
| API | **Supabase Edge Functions** (Deno) | Serverless, sin servidor dedicado |
| Hosting web | **Netlify** | Ya en el stack, plan gratis suficiente para MVP |
| Framework | **Next.js 14 (App Router)** | SSR para SEO + pages estáticas para perfil público |

## Frontend (perfil público de emergencia)

- Next.js con Tailwind CSS
- Diseño móvil-primero (la mayoría de escaneos serán desde celular)
- Sin JavaScript requerido para ver el perfil (SSR puro) — máxima compatibilidad
- Contraste alto para lectura rápida bajo estrés
- Carga < 1 segundo en 3G (emergencias = cualquier condición de red)

## Programación del chip NFC

- URL programada en el chip: `https://nfcmedid.mx/p/[ID]`
- Herramienta de escritura: NFC Tools (app gratuita iOS/Android) o escritura masiva vía lector USB ACR122U
- El ID del perfil se genera en Supabase al crear la cuenta, luego se programa en el chip físico antes de enviar

## Dominio y hosting

- Dominio candidato: `nfcmedid.mx` (verificar disponibilidad — NIC México ~$250 MXN/año)
- SSL: automático vía Netlify
- CDN: incluido en Netlify

## Costos estimados de operación (MVP, primeros 12 meses)

| Concepto | Costo |
|----------|-------|
| Supabase (plan gratis) | $0 |
| Netlify (plan gratis) | $0 |
| Dominio nfcmedid.mx | ~$250 MXN/año |
| 10 tarjetas NFC prototipo | ~$500–$1,500 MXN (estimar con proveedor) |
| **Total inicial** | **~$750–$1,750 MXN** |

## Pendientes técnicos

- [ ] Verificar disponibilidad de dominio nfcmedid.mx
- [ ] Cotizar fabricación de 10 tarjetas NTAG216 con impresión personalizada
- [ ] Definir esquema de base de datos (tabla `profiles`, tabla `scans`)
- [ ] Wireframe de la página de perfil de emergencia
