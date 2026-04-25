-- =============================================
-- 001_enums.sql
-- Tipos enumerados del sistema. Ejecutar primero.
-- =============================================

-- Roles de usuario
CREATE TYPE public.user_role AS ENUM (
  'cashier',   -- mesero / cajero
  'kitchen',   -- cocinero (solo KDS)
  'admin'      -- gerente / administrador
);

-- Estados de las mesas físicas
CREATE TYPE public.table_status AS ENUM (
  'available',       -- mesa libre
  'occupied',        -- mesa con orden activa
  'requesting_bill'  -- mesa pidió la cuenta
);

-- Estados del ciclo de vida de una orden
-- Flujo: pending → preparing → ready → closed
--        pending/preparing → cancelled
CREATE TYPE public.order_status AS ENUM (
  'pending',    -- enviada a cocina, sin acción aún
  'preparing',  -- cocina tomó la orden
  'ready',      -- cocina terminó, esperando al mesero
  'closed',     -- pagada y cerrada
  'cancelled'   -- cancelada (solo cashier/admin)
);
