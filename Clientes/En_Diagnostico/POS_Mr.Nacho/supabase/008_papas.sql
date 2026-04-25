-- Agrega la categoría "Papas" y sus productos al catálogo.
-- Seguro ejecutar varias veces (idempotente).

DO $$
DECLARE
  cat_id uuid;
BEGIN
  -- Buscar o crear la categoría Papas
  SELECT id INTO cat_id
  FROM public.menu_categories
  WHERE name = 'Papas'
  LIMIT 1;

  IF cat_id IS NULL THEN
    INSERT INTO public.menu_categories (name, sort_order, is_active)
    VALUES ('Papas', 10, true)
    RETURNING id INTO cat_id;
  END IF;

  -- Insertar Papas a la francesa si no existe
  IF NOT EXISTS (
    SELECT 1 FROM public.menu_items WHERE name = 'Papas a la francesa'
  ) THEN
    INSERT INTO public.menu_items
      (category_id, name, price, is_available, sort_order, base_ingredients)
    VALUES
      (cat_id, 'Papas a la francesa', 40, true, 1,
       '{"groups": [], "standalone": []}'::jsonb);
  END IF;

  -- Insertar Papas gajo si no existe
  IF NOT EXISTS (
    SELECT 1 FROM public.menu_items WHERE name = 'Papas gajo'
  ) THEN
    INSERT INTO public.menu_items
      (category_id, name, price, is_available, sort_order, base_ingredients)
    VALUES
      (cat_id, 'Papas gajo', 45, true, 2,
       '{"groups": [], "standalone": []}'::jsonb);
  END IF;
END;
$$;
