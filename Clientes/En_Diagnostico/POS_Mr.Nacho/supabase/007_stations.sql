-- =============================================
-- 007_stations.sql
-- Agrega estaciones de cocina y el estado 'delivered' a las órdenes.
--
-- Cambios:
--   1. Nuevo enum kitchen_station: station_1, station_2
--   2. Nuevo valor 'delivered' en order_status (después de 'ready')
--   3. Columna kitchen_station en orders (NOT NULL, DEFAULT 'station_1')
--
-- Idempotencia:
--   - CREATE TYPE usa DO/EXCEPTION para no fallar si ya existe
--   - ALTER TYPE ADD VALUE usa IF NOT EXISTS
--   - ALTER TABLE ADD COLUMN usa IF NOT EXISTS
-- =============================================

-- 1. Crear enum kitchen_station
DO $$ BEGIN
  CREATE TYPE public.kitchen_station AS ENUM ('station_1', 'station_2');
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

-- 2. Agregar 'delivered' al enum order_status (Postgres 9.3+ IF NOT EXISTS)
-- Supabase usa PG 15+, soportado sin restricciones dentro de transacciones.
ALTER TYPE public.order_status ADD VALUE IF NOT EXISTS 'delivered' AFTER 'ready';

-- 3. Agregar columna kitchen_station a orders
--    DEFAULT 'station_1' para no romper órdenes existentes.
ALTER TABLE public.orders
  ADD COLUMN IF NOT EXISTS kitchen_station public.kitchen_station NOT NULL DEFAULT 'station_1';
