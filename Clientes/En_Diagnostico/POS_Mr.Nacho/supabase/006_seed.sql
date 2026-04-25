-- =============================================
-- 006_seed.sql
-- Datos de ejemplo: categorías y menú completo
-- para el carrito de hamburguesas y hot dogs.
--
-- Ingredientes base por tipo de producto:
--   clasica:       groups: [verduras, aderezos]
--   especial:      groups: [verduras, aderezos], standalone: [champiñones, queso]
--   hawaiana:      groups: [verduras, aderezos], standalone: [piña, jamón, queso]
--   chori:         groups: [verduras, aderezos], standalone: [chorizo, queso]
--   tocino:        groups: [verduras, aderezos], standalone: [tocino, queso]
--   doble especial:groups: [verduras, aderezos], standalone: [champiñones, queso, piña, tocino]
--   vegetariano:   groups: [verduras, aderezos], standalone: [piña, champiñones, queso]
--   zincronizada:  groups: [aderezos],           standalone: [queso]
-- =============================================

-- Limpiar datos previos si existen.
-- ADVERTENCIA: Solo ejecutar en base de datos vacía sin órdenes activas.
--
-- Se incluyen las tres tablas en una sola instrucción TRUNCATE porque Postgres
-- bloquea TRUNCATE en tablas referenciadas por FK, incluso si están vacías.
-- El TRUNCATE multi-tabla maneja las FK entre estas tres tablas internamente.
-- order_items se incluye porque tiene FK → menu_items.
-- Si hubiera órdenes reales, sus order_items serían eliminados.
TRUNCATE public.order_items, public.menu_items, public.menu_categories;

-- ── Categorías ────────────────────────────────────────────────────────────────
INSERT INTO public.menu_categories (id, name, sort_order) VALUES
  ('11111111-0000-0000-0000-000000000001', 'Hamburguesas Chicas',  1),
  ('11111111-0000-0000-0000-000000000002', 'Hamburguesas Grandes', 2),
  ('11111111-0000-0000-0000-000000000003', 'Hot Dogs Chicos',      3),
  ('11111111-0000-0000-0000-000000000004', 'Hot Dogs Grandes',     4),
  ('11111111-0000-0000-0000-000000000005', 'Extras',               5);

-- ── Hamburguesas Chicas ───────────────────────────────────────────────────────
INSERT INTO public.menu_items (category_id, name, price, sort_order, base_ingredients) VALUES
(
  '11111111-0000-0000-0000-000000000001',
  'Hamburguesa Chica Clásica', 55, 1,
  '{"groups":["verduras","aderezos"],"standalone":[]}'
),
(
  '11111111-0000-0000-0000-000000000001',
  'Hamburguesa Chica Especial', 70, 2,
  '{"groups":["verduras","aderezos"],"standalone":["champiñones","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000001',
  'Hamburguesa Chica Hawaiana', 70, 3,
  '{"groups":["verduras","aderezos"],"standalone":["piña","jamón","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000001',
  'Chori Burger Chica', 80, 4,
  '{"groups":["verduras","aderezos"],"standalone":["chorizo","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000001',
  'Hamburguesa Chica de Tocino', 80, 5,
  '{"groups":["verduras","aderezos"],"standalone":["tocino","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000001',
  'Hamburguesa Doble Chica Especial', 110, 6,
  '{"groups":["verduras","aderezos"],"standalone":["champiñones","queso","piña","tocino"]}'
);

-- ── Hamburguesas Grandes ──────────────────────────────────────────────────────
INSERT INTO public.menu_items (category_id, name, price, sort_order, base_ingredients) VALUES
(
  '11111111-0000-0000-0000-000000000002',
  'Hamburguesa Clásica Grande', 65, 1,
  '{"groups":["verduras","aderezos"],"standalone":[]}'
),
(
  '11111111-0000-0000-0000-000000000002',
  'Hamburguesa Grande Especial', 80, 2,
  '{"groups":["verduras","aderezos"],"standalone":["champiñones","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000002',
  'Hamburguesa Grande Hawaiana', 80, 3,
  '{"groups":["verduras","aderezos"],"standalone":["piña","jamón","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000002',
  'Chori Burger Grande', 90, 4,
  '{"groups":["verduras","aderezos"],"standalone":["chorizo","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000002',
  'Hamburguesa Grande de Tocino', 90, 5,
  '{"groups":["verduras","aderezos"],"standalone":["tocino","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000002',
  'Hamburguesa Doble Grande Especial', 120, 6,
  '{"groups":["verduras","aderezos"],"standalone":["champiñones","queso","piña","tocino"]}'
);

-- ── Hot Dogs Chicos ───────────────────────────────────────────────────────────
INSERT INTO public.menu_items (category_id, name, price, sort_order, base_ingredients) VALUES
(
  '11111111-0000-0000-0000-000000000003',
  'Hot Dog Chico Clásico', 30, 1,
  '{"groups":["verduras","aderezos"],"standalone":[]}'
),
(
  '11111111-0000-0000-0000-000000000003',
  'Hot Dog Chico Especial', 50, 2,
  '{"groups":["verduras","aderezos"],"standalone":["champiñones","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000003',
  'Hot Dog Chico Hawaiano', 50, 3,
  '{"groups":["verduras","aderezos"],"standalone":["piña","jamón","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000003',
  'Hot Dog Chico Chori-jocho', 55, 4,
  '{"groups":["verduras","aderezos"],"standalone":["chorizo","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000003',
  'Hot Dog Chico de Tocino', 55, 5,
  '{"groups":["verduras","aderezos"],"standalone":["tocino","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000003',
  'Hot Dog Chico Vegetariano', 30, 6,
  '{"groups":["verduras","aderezos"],"standalone":["piña","champiñones","queso"]}'
);

-- ── Hot Dogs Grandes ──────────────────────────────────────────────────────────
INSERT INTO public.menu_items (category_id, name, price, sort_order, base_ingredients) VALUES
(
  '11111111-0000-0000-0000-000000000004',
  'Hot Dog Grande Clásico', 50, 1,
  '{"groups":["verduras","aderezos"],"standalone":[]}'
),
(
  '11111111-0000-0000-0000-000000000004',
  'Hot Dog Grande Especial', 60, 2,
  '{"groups":["verduras","aderezos"],"standalone":["champiñones","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000004',
  'Hot Dog Grande Hawaiano', 60, 3,
  '{"groups":["verduras","aderezos"],"standalone":["piña","jamón","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000004',
  'Hot Dog Grande Chori-jocho', 70, 4,
  '{"groups":["verduras","aderezos"],"standalone":["chorizo","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000004',
  'Hot Dog Grande de Tocino', 70, 5,
  '{"groups":["verduras","aderezos"],"standalone":["tocino","queso"]}'
),
(
  '11111111-0000-0000-0000-000000000004',
  'Hot Dog Grande Vegetariano', 50, 6,
  '{"groups":["verduras","aderezos"],"standalone":["piña","champiñones","queso"]}'
);

-- ── Extras ────────────────────────────────────────────────────────────────────
INSERT INTO public.menu_items (category_id, name, price, sort_order, base_ingredients) VALUES
(
  '11111111-0000-0000-0000-000000000005',
  'Zincronizada', 60, 1,
  '{"groups":["aderezos"],"standalone":["queso"]}'
);
