PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE enrollment_new (
    id INTEGER PRIMARY KEY,
    character_id INTEGER NOT NULL,
    institution_id INTEGER NOT NULL,
    enrollment_year INTEGER NOT NULL,
    graduation_year INTEGER,
    notes TEXT,
    FOREIGN KEY (character_id) REFERENCES characters(id),
    FOREIGN KEY (institution_id) REFERENCES educational_institutions(id)
);

INSERT INTO enrollment_new (id, character_id, institution_id, enrollment_year, graduation_year, notes)
SELECT id, character_id, institution_id, enrollment_year, graduation_year, notes FROM enrollment;

DROP TABLE enrollment;

ALTER TABLE enrollment_new RENAME TO enrollment;

COMMIT;
PRAGMA foreign_keys=ON;
