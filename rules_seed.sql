-- Room Categories Table
CREATE TABLE room_categories (
    id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL
);

-- Room Types Table
CREATE TABLE room_types (
    id INTEGER PRIMARY KEY,
    category_id INTEGER NOT NULL,
    room_name TEXT NOT NULL,
    description TEXT,
    typical_floor TEXT,
    is_common BOOLEAN DEFAULT true,
    FOREIGN KEY (category_id) REFERENCES room_categories(id)
);

-- Insert Categories
INSERT INTO room_categories (id, category_name) VALUES
(1, 'Main Living Areas'),
(2, 'Personal Spaces'),
(3, 'Transitional Spaces'),
(4, 'Storage');

-- Insert Room Types
INSERT INTO room_types (category_id, room_name, description, typical_floor, is_common) VALUES
-- Main Living Areas
(1, 'Living Room', 'Primary family gathering space, also called sitting room or lounge', 'Ground', true),
(1, 'Dining Room', 'Formal eating area', 'Ground', true),
(1, 'Kitchen', 'Food preparation and informal dining area', 'Ground', true),
(1, 'Conservatory', 'Glass-walled extension used as additional living space', 'Ground', false),

-- Personal Spaces
(2, 'Master Bedroom', 'Primary bedroom, usually largest bedroom in house', 'First', true),
(2, 'Guest Bedroom', 'Bedroom for visitors', 'First', false),
(2, 'Family Bathroom', 'Main bathroom with full facilities', 'First', true),
(2, 'En-suite', 'Private bathroom connected to bedroom', 'First', false),
(2, 'Downstairs WC', 'Ground floor toilet facilities', 'Ground', false),
(2, 'Utility Room', 'Laundry and household storage area', 'Ground', false),

-- Transitional Spaces
(3, 'Hallway', 'Main entrance corridor', 'Ground', true),
(3, 'Landing', 'Upper floor corridor', 'First', true),
(3, 'Porch', 'Covered entrance area', 'Ground', false),
(3, 'Stairs', 'Internal staircase', 'Multiple', true),

-- Storage
(4, 'Airing Cupboard', 'Heated storage for linens and water heater', 'First', true),
(4, 'Box Room', 'Small bedroom often used for storage', 'First', false),
(4, 'Loft', 'Storage space in roof area', 'Top', true),
(4, 'Cellar', 'Underground storage room', 'Basement', false);