-- =============================================
-- 004_rls.sql
-- Row Level Security para todos los roles.
--
-- Lógica de Supabase RLS:
--   - Las políticas del mismo tipo (SELECT, INSERT...)
--     se combinan con OR (cualquiera que pase, da acceso).
--   - USING  = filtro en lectura (qué filas puede ver)
--   - WITH CHECK = filtro en escritura (qué filas puede crear/editar)
--
-- NOTA MVP: La restricción de qué CAMPOS puede editar cada
-- rol (ej: kitchen solo puede editar status, no total)
-- se implementa en la capa de aplicación. RLS opera a nivel
-- de fila, no de columna. Documentado aquí para no olvidarlo.
-- =============================================


-- =============================================
-- Helper: retorna el rol del usuario autenticado actual.
-- SECURITY DEFINER = corre como superuser para poder
-- leer profiles aunque tenga RLS habilitado.
-- STABLE = Postgres puede cachear el resultado por query.
-- =============================================
CREATE OR REPLACE FUNCTION public.get_user_role()
RETURNS public.user_role AS $$
  SELECT role
  FROM public.profiles
  WHERE id = auth.uid() AND is_active = true;
$$ LANGUAGE sql SECURITY DEFINER STABLE;


-- =============================================
-- Habilitar RLS en todas las tablas
-- =============================================
ALTER TABLE public.profiles          ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.menu_categories   ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.menu_items        ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.restaurant_tables ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orders            ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.order_items       ENABLE ROW LEVEL SECURITY;


-- =============================================
-- PROFILES
-- Admin: todo. Resto: solo su propio perfil.
-- =============================================

CREATE POLICY "profiles: own select"
  ON public.profiles FOR SELECT TO authenticated
  USING (id = auth.uid());

CREATE POLICY "profiles: admin all"
  ON public.profiles FOR ALL TO authenticated
  USING (public.get_user_role() = 'admin');


-- =============================================
-- MENU CATEGORIES
-- Admin: todo. Staff: solo categorías activas (SELECT).
-- =============================================

CREATE POLICY "menu_categories: staff read active"
  ON public.menu_categories FOR SELECT TO authenticated
  USING (
    is_active = true
    AND public.get_user_role() IN ('cashier', 'kitchen')
  );

CREATE POLICY "menu_categories: admin all"
  ON public.menu_categories FOR ALL TO authenticated
  USING (public.get_user_role() = 'admin');


-- =============================================
-- MENU ITEMS
-- Admin: todo. Cashier/Kitchen: solo ítems disponibles.
-- =============================================

CREATE POLICY "menu_items: staff read available"
  ON public.menu_items FOR SELECT TO authenticated
  USING (
    is_available = true
    AND public.get_user_role() IN ('cashier', 'kitchen')
  );

CREATE POLICY "menu_items: admin all"
  ON public.menu_items FOR ALL TO authenticated
  USING (public.get_user_role() = 'admin');


-- =============================================
-- RESTAURANT TABLES
-- Admin: todo.
-- Cashier: SELECT todas + UPDATE status.
-- Kitchen: SELECT (para mostrar número en KDS).
-- =============================================

CREATE POLICY "restaurant_tables: all staff read"
  ON public.restaurant_tables FOR SELECT TO authenticated
  USING (public.get_user_role() IN ('cashier', 'kitchen', 'admin'));

-- Cashier actualiza status de la mesa (occupied, requesting_bill, available)
-- La app valida que solo cambie el campo status.
CREATE POLICY "restaurant_tables: cashier update"
  ON public.restaurant_tables FOR UPDATE TO authenticated
  USING     (public.get_user_role() IN ('cashier', 'admin'))
  WITH CHECK (public.get_user_role() IN ('cashier', 'admin'));

CREATE POLICY "restaurant_tables: admin insert delete"
  ON public.restaurant_tables FOR INSERT TO authenticated
  WITH CHECK (public.get_user_role() = 'admin');

CREATE POLICY "restaurant_tables: admin delete"
  ON public.restaurant_tables FOR DELETE TO authenticated
  USING (public.get_user_role() = 'admin');


-- =============================================
-- ORDERS
-- Admin: todo.
-- Cashier: SELECT todas + INSERT + UPDATE (cerrar/cancelar/notas).
-- Kitchen: SELECT solo activas (pending/preparing/ready) + UPDATE status.
--
-- RESTRICCIÓN DE CAMPO (en app, no en RLS):
--   Kitchen solo puede cambiar status a: preparing, ready.
--   Cashier solo puede cambiar status a: closed, cancelled.
--
-- LIMITACIÓN CONOCIDA (MVP):
--   La policy "orders: cashier update" no restringe qué columnas puede modificar
--   un cashier. RLS opera a nivel de fila, no de columna. Un cashier autenticado
--   podría modificar total, cashier_id u otros campos vía API directa.
--   Mitigación en MVP: la app solo envía los campos permitidos.
--   Solución definitiva (post-MVP): trigger de validación de columnas o
--   mover mutaciones sensibles a Edge Functions con validación explícita.
-- =============================================

CREATE POLICY "orders: cashier select"
  ON public.orders FOR SELECT TO authenticated
  USING (public.get_user_role() = 'cashier');

CREATE POLICY "orders: cashier insert"
  ON public.orders FOR INSERT TO authenticated
  WITH CHECK (
    public.get_user_role() = 'cashier'
    AND cashier_id = auth.uid()
  );

CREATE POLICY "orders: cashier update"
  ON public.orders FOR UPDATE TO authenticated
  USING     (public.get_user_role() = 'cashier')
  WITH CHECK (public.get_user_role() = 'cashier');

-- Kitchen ve solo órdenes que necesitan atención
CREATE POLICY "orders: kitchen select active"
  ON public.orders FOR SELECT TO authenticated
  USING (
    public.get_user_role() = 'kitchen'
    AND status IN ('pending', 'preparing', 'ready')
  );

-- Kitchen solo puede avanzar el estado (pending→preparing, preparing→ready)
-- No puede volver atrás ni cerrar/cancelar.
CREATE POLICY "orders: kitchen update status"
  ON public.orders FOR UPDATE TO authenticated
  USING (
    public.get_user_role() = 'kitchen'
    AND status IN ('pending', 'preparing')         -- solo puede editar estas
  )
  WITH CHECK (
    public.get_user_role() = 'kitchen'
    AND status IN ('preparing', 'ready')           -- solo puede dejar en estas
  );

CREATE POLICY "orders: admin all"
  ON public.orders FOR ALL TO authenticated
  USING (public.get_user_role() = 'admin');


-- =============================================
-- ORDER ITEMS
-- Admin: todo.
-- Cashier: SELECT + INSERT.
-- Kitchen: SELECT (para mostrar ítems en KDS).
--
-- DELETE solo desde la app y solo en órdenes pending
-- (se valida en la lógica de aplicación).
-- =============================================

CREATE POLICY "order_items: cashier select"
  ON public.order_items FOR SELECT TO authenticated
  USING (public.get_user_role() = 'cashier');

CREATE POLICY "order_items: cashier insert"
  ON public.order_items FOR INSERT TO authenticated
  WITH CHECK (public.get_user_role() = 'cashier');

CREATE POLICY "order_items: kitchen select"
  ON public.order_items FOR SELECT TO authenticated
  USING (public.get_user_role() = 'kitchen');

CREATE POLICY "order_items: admin all"
  ON public.order_items FOR ALL TO authenticated
  USING (public.get_user_role() = 'admin');
