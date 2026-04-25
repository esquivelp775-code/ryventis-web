-- =============================================
-- 003_triggers.sql
-- Triggers del sistema:
--   1. updated_at automático en tablas relevantes
--   2. Creación automática de profile al registrar usuario
-- =============================================


-- =============================================
-- Función: actualiza updated_at antes de cada UPDATE
-- =============================================
CREATE OR REPLACE FUNCTION public.update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar a menu_items
CREATE TRIGGER trg_menu_items_updated_at
  BEFORE UPDATE ON public.menu_items
  FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

-- Aplicar a restaurant_tables
CREATE TRIGGER trg_restaurant_tables_updated_at
  BEFORE UPDATE ON public.restaurant_tables
  FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

-- Aplicar a orders
CREATE TRIGGER trg_orders_updated_at
  BEFORE UPDATE ON public.orders
  FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();


-- =============================================
-- Función: crea un profile automáticamente cuando
-- un usuario se registra en auth.users.
--
-- El rol y full_name se pasan en raw_user_meta_data
-- al crear el usuario desde el dashboard o la API:
--
--   supabase.auth.admin.createUser({
--     email: '...',
--     password: '...',
--     user_metadata: { full_name: 'Ana López', role: 'cashier' }
--   })
-- =============================================
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, full_name, role)
  VALUES (
    NEW.id,
    -- full_name desde metadata, fallback al prefijo del email
    COALESCE(
      NEW.raw_user_meta_data->>'full_name',
      split_part(NEW.email, '@', 1)
    ),
    -- role desde metadata, fallback a 'cashier'
    COALESCE(
      (NEW.raw_user_meta_data->>'role')::public.user_role,
      'cashier'
    )
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger que ejecuta la función en cada INSERT en auth.users
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();
