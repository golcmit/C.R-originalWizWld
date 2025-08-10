PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

-- Drop the old, badly defined table
DROP TABLE IF EXISTS relationships;

-- Create the new helper table for relationship types
CREATE TABLE relationship_types (
    id INTEGER PRIMARY KEY,
    type_name TEXT NOT NULL UNIQUE,
    is_bidirectional BOOLEAN NOT NULL
);

-- Populate it with the standard types
INSERT OR IGNORE INTO relationship_types (id, type_name, is_bidirectional) VALUES (1, 'parent-child', 0);
INSERT OR IGNORE INTO relationship_types (id, type_name, is_bidirectional) VALUES (2, 'friends', 1);
INSERT OR IGNORE INTO relationship_types (id, type_name, is_bidirectional) VALUES (3, 'married', 1);
INSERT OR IGNORE INTO relationship_types (id, type_name, is_bidirectional) VALUES (4, 'crush', 0);
INSERT OR IGNORE INTO relationship_types (id, type_name, is_bidirectional) VALUES (5, 'sibling', 1);

-- Create the new, correct relationships table
CREATE TABLE relationships (
    id INTEGER PRIMARY KEY,
    from_character INTEGER NOT NULL,
    to_character INTEGER NOT NULL,
    relationship_type_id INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (from_character) REFERENCES characters(id),
    FOREIGN KEY (to_character) REFERENCES characters(id),
    FOREIGN KEY (relationship_type_id) REFERENCES relationship_types(id)
);

COMMIT;
PRAGMA foreign_keys=ON;
