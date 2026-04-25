# NFC MedID — Descripción del MVP

## Flujo del usuario (MVP)

```
1. Cliente compra tarjeta física (NFC + QR impreso)
2. Recibe link único para crear su perfil médico en línea
3. Llena el formulario con sus datos de emergencia
4. Perfil queda activo y vinculado al chip NFC y al QR
5. En emergencia: paramédico acerca celular a la tarjeta (o escanea QR)
6. Abre página web con datos médicos del portador en menos de 3 segundos
```

## Funcionalidades del MVP (alcance mínimo)

### Tarjeta física
- Chip NFC pasivo NTAG216 (capacidad 888 bytes, suficiente para URL)
- Código QR impreso al reverso (respaldo si el celular no tiene NFC)
- Tamaño CR80 (estándar tarjeta de crédito) — grosor 0.76mm
- Material: PVC o PET (evaluar costo vs durabilidad)
- Impresión: logo NFC MedID + instrucción "Acerca al celular en emergencia"

### Perfil digital (página web)
- URL única por tarjeta: `nfcmedid.mx/p/[ID_UNICO]`
- Campos del perfil de emergencia:
  - Nombre completo y foto (opcional)
  - Fecha de nacimiento y edad
  - Grupo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-)
  - Alergias conocidas (campo libre + checkboxes comunes: penicilina, aspirina, látex, mariscos, nuez)
  - Medicamentos actuales (nombre + dosis + frecuencia)
  - Condiciones crónicas (diabetes, hipertensión, epilepsia, marcapasos, etc.)
  - Contacto de emergencia 1 (nombre + teléfono + relación)
  - Contacto de emergencia 2
  - Médico de cabecera (nombre + teléfono)
  - Notas adicionales para paramédicos (campo libre)
- Página optimizada para lectura rápida en pantalla de celular
- Sin login requerido para ver el perfil (acceso público por URL)
- Botón de llamada directa al contacto de emergencia

### Panel de administración (básico)
- Login del portador con email + contraseña
- Editar y actualizar perfil en cualquier momento
- Ver historial de escaneos (fecha, hora, ubicación aproximada)

## Fuera del MVP (versión futura)

- App móvil nativa
- Integración con hospitales y servicios de emergencia
- Perfil médico completo (historial de cirugías, vacunas, resultados de laboratorio)
- Tarjeta para mascotas
- Multiidioma (inglés para turistas)
- Pago de renovación automática (Stripe / MercadoPago)

## Validación necesaria antes de construir

1. ¿Cuánto cuesta fabricar 10 tarjetas NFC para prueba? (investigar proveedor)
2. ¿El mercado pagará $350–$450 MXN? (probar con 5 ventas a conocidos)
3. ¿Qué dominio usar? (nfcmedid.mx disponible — verificar)
