-- =============================================
-- 005_schema_update.sql
-- Adapta el schema para el flujo de carrito ambulante:
--   - Sin mesas, con nombre de cliente y tipo de servicio
--   - Modificaciones de producto en order_items (JSONB)
--   - Ingredientes base por producto en menu_items (JSONB)
-- =============================================

-- Nuevo enum para tipo de servicio
-- Bloque idempotente: no falla si el tipo ya existe (re-ejecución segura).
-- PostgreSQL no soporta CREATE TYPE IF NOT EXISTS, por eso se usa DO $$.
DO $$ BEGIN
  CREATE TYPE public.service_type AS ENUM ('comer_aqui', 'para_llevar');
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

-- ── orders ────────────────────────────────────────────────────────────────────

-- Hacer table_id nullable (el carrito no usa mesas)
ALTER TABLE public.orders
  ALTER COLUMN table_id DROP NOT NULL;

-- Agregar nombre del cliente (identificador visible principal)
ALTER TABLE public.orders
  ADD COLUMN IF NOT EXISTS customer_name TEXT NOT NULL DEFAULT '';

-- Agregar tipo de servicio
ALTER TABLE public.orders
  ADD COLUMN IF NOT EXISTS service_type public.service_type NOT NULL DEFAULT 'para_llevar';

COMMENT ON COLUMN public.orders.customer_name IS 'Identificador visible de la orden en KDS e historial';
COMMENT ON COLUMN public.orders.service_type  IS 'comer_aqui o para_llevar';

-- ── order_items ───────────────────────────────────────────────────────────────

-- Modificaciones seleccionadas por el cajero en el modal de personalización
-- Estructura: {
--   removed_groups: string[],     -- ['verduras', 'aderezos']
--   removed_subitems: string[],   -- ['cebolla', 'jitomate']
--   removed_standalone: string[], -- ['queso']
--   extras: [{id, name, price, subchoice?}],
--   notes: string
-- }
ALTER TABLE public.order_items
  ADD COLUMN IF NOT EXISTS modifications JSONB NOT NULL DEFAULT '{}';

COMMENT ON COLUMN public.order_items.modifications IS 'Personalización del ítem: ingredientes removidos y extras';

-- ── menu_items ────────────────────────────────────────────────────────────────

-- Ingredientes base del producto, usados para renderizar el modal
-- Estructura: {
--   groups: string[],      -- grupos removibles: ['verduras', 'aderezos']
--   standalone: string[]   -- ítems individuales: ['queso', 'champiñones']
-- }
ALTER TABLE public.menu_items
  ADD COLUMN IF NOT EXISTS base_ingredients JSONB NOT NULL DEFAULT '{"groups":[],"standalone":[]}';

COMMENT ON COLUMN public.menu_items.base_ingredients IS 'Ingredientes customizables del producto para el modal de personalización';
