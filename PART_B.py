PART B 1 Writing SQL Queries:

CREATE TABLE televisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    catalog_number INTEGER NOT NULL UNIQUE,
    brand TEXT NOT NULL CHECK (brand IN ('Samsung', 'LG', 'Sony')),
    model TEXT NOT NULL,
    screen_size INTEGER NOT NULL CHECK (screen_size > 0),
    resolution TEXT NOT NULL CHECK (resolution IN ('4K', '8K', 'Full HD')),
    price REAL NOT NULL CHECK (price > 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    release_year INTEGER NOT NULL ,
    smart_tv TEXT NOT NULL DEFAULT 'Yes' CHECK (smart_tv IN ('Yes', 'No')),
    os TEXT DEFAULT NULL,
    panel_type TEXT NOT NULL CHECK (panel_type IN ('OLED', 'QLED', 'LED')),
    CHECK (
        (smart_tv = 'Yes' AND os IS NOT NULL) OR
        (smart_tv = 'No' AND os IS NULL)
    )
INSERT INTO televisions_2 (catalog_number, brand, model, screen_size, resolution, price, stock_quantity, release_year, smart_tv, os, panel_type)
VALUES ('SONY1', 'Sony', 'BLACK MAMBA', 85, '4K', 1200, 41, 2026, 'Yes', 'BBR', 'QLED');

INSERT INTO televisions_2 (catalog_number, brand, model, screen_size, resolution, price, stock_quantity, release_year, smart_tv, os, panel_type)
VALUES ('Samsung88', 'Samsung', 'GREEN B', 98, '8K', 1345, 2, 2024, 'Yes', 'RTY', 'LED');

INSERT INTO televisions_2 (catalog_number, brand, model, screen_size, resolution, price, stock_quantity, release_year, smart_tv, os, panel_type)
VALUES ('LG56', 'LG', 'WER4', 65, 'Full HD', 8000, 20, 2025, 'No', NULL, 'OLED');