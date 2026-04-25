-- =============================================
-- 002_tables.sql
-- Tablas del sistema en orden de dependencia.
-- Requiere: 001_enums.sql ejecutado previamente.
-- =============================================


-- =============================================
-- profiles
-- Extiende auth.users con datos del negocio.
-- Se crea automáticamente vía trigger (ver 003).
-- =============================================
CREATE TABLE public.profiles (
  id          UUID        PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  full_name   TEXT        NOT NULL,
  role        public.user_role  NOT NULL DEFAULT 'cashier',
  is_active   BOOLEAN     NOT NULL DEFAULT true,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

COMMENT ON TABLE  public.profiles           IS 'Extiende auth.users con rol y estado de cuenta';
COMMENT ON COLUMN public.profiles.role      IS 'Determina qué pantallas y acciones están disponibles';
COMMENT ON COLUMN public.profiles.is_active IS 'false = acceso bloqueado sin eliminar el usuario';


-- =============================================
-- menu_categories
-- Agrupa los productos del menú.
-- Necesaria para la navegación del POS.
-- =============================================
CREATE TABLE public.menu_categories (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  name        TEXT        NOT NULL,
  sort_order  INTEGER     NOT NULL DEFAULT 0,
  is_active   BOOLEAN     NOT NULL DEFAULT true,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);


-- =============================================
-- menu_items
-- Productos individuales con precio.
-- =============================================
CREATE TABLE public.menu_items (
  id           UUID           PRIMARY KEY DEFAULT gen_random_uuid(),
  category_id  UUID           NOT NULL REFERENCES public.menu_categories(id) ON DELETE RESTRICT,
  name         TEXT           NOT NULL,
  description  TEXT,
  price        NUMERIC(10,2)  NOT NULL CHECK (price > 0),
  is_available BOOLEAN        NOT NULL DEFAULT true,
  sort_order   INTEGER        NOT NULL DEFAULT 0,
  created_at   TIMESTAMPTZ    NOT NULL DEFAULT now(),
  updated_at   TIMESTAMPTZ    NOT NULL DEFAULT now()
);

COMMENT ON COLUMN public.menu_items.price        IS 'Precio vigente. Los cambios NO afectan órdenes pasadas.';
COMMENT ON COLUMN public.menu_items.is_available IS 'false = oculto en POS, pero preservado en historial';


-- =============================================
-- restaurant_tables
-- Mesas físicas del local.
-- Nombrada así para evitar colisión con SQL "tables".
-- =============================================
CREATE TABLE public.restaurant_tables (
  id         UUID                 PRIMARY KEY DEFAULT gen_random_uuid(),
  number     INTEGER              NOT NULL UNIQUE CHECK (number > 0),
  name       TEXT,                -- alias opcional: "Terraza A", "Barra 1"
  capacity   INTEGER              NOT NULL DEFAULT 4 CHECK (capacity > 0),
  status     public.table_status  NOT NULL DEFAULT 'available',
  created_at TIMESTAMPTZ          NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ          NOT NULL DEFAULT now()
);

COMMENT ON COLUMN public.restaurant_tables.number IS 'Número visible de la mesa en el local';
COMMENT ON COLUMN public.restaurant_tables.name   IS 'Alias opcional para mostrar en pantalla';


-- =============================================
-- orders
-- Sesión completa de una mesa. Entidad central.
-- Una mesa puede tener solo una orden activa
-- (status distinto de closed/cancelled) a la vez.
-- =============================================
CREATE TABLE public.orders (
  id          UUID                  PRIMARY KEY DEFAULT gen_random_uuid(),
  table_id    UUID                  NOT NULL REFERENCES public.restaurant_tables(id) ON DELETE RESTRICT,
  cashier_id  UUID                  NOT NULL REFERENCES public.profiles(id) ON DELETE RESTRICT,
  status      public.order_status   NOT NULL DEFAULT 'pending',
  total       NUMERIC(10,2)         NOT NULL DEFAULT 0 CHECK (total >= 0),
  notes       TEXT,
  created_at  TIMESTAMPTZ           NOT NULL DEFAULT now(),
  updated_at  TIMESTAMPTZ           NOT NULL DEFAULT now(),
  closed_at   TIMESTAMPTZ           -- se setea al pasar a closed o cancelled
);

COMMENT ON COLUMN public.orders.total     IS 'Actualizado desde la app al agregar/quitar ítems';
COMMENT ON COLUMN public.orders.closed_at IS 'Timestamp de pago o cancelación';


-- =============================================
-- order_items
-- Ítems individuales dentro de una orden.
-- Almacena snapshot del precio al momento del pedido.
-- =============================================
CREATE TABLE public.order_items (
  id           UUID           PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id     UUID           NOT NULL REFERENCES public.orders(id) ON DELETE CASCADE,
  menu_item_id UUID           NOT NULL REFERENCES public.menu_items(id) ON DELETE RESTRICT,
  quantity     INTEGER        NOT NULL CHECK (quantity > 0),
  unit_price   NUMERIC(10,2)  NOT NULL CHECK (unit_price > 0),  -- snapshot al pedir
  subtotal     NUMERIC(10,2)  NOT NULL CHECK (subtotal > 0),    -- quantity × unit_price
  notes        TEXT,          -- instrucciones especiales: "sin cebolla", "término medio"
  created_at   TIMESTAMPTZ    NOT NULL DEFAULT now()
);

COMMENT ON COLUMN public.order_items.unit_price IS 'Copia del precio al momento del pedido. Inmutable.';
COMMENT ON COLUMN public.order_items.subtotal   IS 'quantity × unit_price. Calculado en la aplicación.';
