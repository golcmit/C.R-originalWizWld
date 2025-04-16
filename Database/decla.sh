#!/bin/bash

DB_FILE="FanacalCharacters.db"

sqlite3 "$DB_FILE" <<'EOF'
PRAGMA foreign_keys = ON;
-- 学校テーブル
CREATE TABLE IF NOT EXISTS educational_institutions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
-- 寮テーブル
CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- 血族テーブル
CREATE TABLE IF NOT EXISTS lineages (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- キャラクターテーブル
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    current_last_name TEXT NOT NULL,
    birth_last_name TEXT,
    institution_id INTEGER,
    house_id INTEGER,
    lineage_id INTEGER,
    birth_date DATE NOT NULL,
    death_date DATE,
    sex TEXT,
    gender TEXT,
    sexual_orientation TEXT,
    blood_status TEXT,
    notes TEXT,
    FOREIGN KEY (institution_id) REFERENCES educational_institutions(id),
    FOREIGN KEY (house_id) REFERENCES houses(id),
    FOREIGN KEY (lineage_id) REFERENCES lineages(id)
);

-- キャラクター関係テーブル
CREATE TABLE IF NOT EXISTS relationships (
    id INTEGER PRIMARY KEY,
    from_character INTEGER NOT NULL,
    to_character INTEGER NOT NULL,
    relation_type TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (from_character) REFERENCES characters(id),
    FOREIGN KEY (to_character) REFERENCES characters(id)
);

-- ホグワーツ在籍情報
CREATE TABLE IF NOT EXISTS enrollment (
    id INTEGER PRIMARY KEY,
    character_id INTEGER NOT NULL,
    institution_id INTEGER NOT NULL,
    enrollment_year INTEGER NOT NULL,
    graduation_year INTEGER,
    notes TEXT,
    FOREIGN KEY (character_id) REFERENCES characters(id),
    FOREIGN KEY (institution_id) REFERENCES educational_institutions(id)
);

--初期値代入

--学校初期値
INSERT INTO educational_institutions (id, name) VALUES
    (0,'hogwarts'),
    (1,'beauxbâtons'),
    (2,'durmstrang'),
    (3,'ilvermorny'),
    (4,'koldovstoretz'),
    (5,'uagadou'),
    (6,'castelobruxo'),
    (7,'mahoutokoro');

--寮初期値
INSERT INTO houses (id, name) VALUES
    (0,'griffindor'),
    (1,'slytherin'),
    (2,'ravenclaw'),
    (3,'hufflepuff');

--血族初期値

INSERT INTO lineages (id, name,description) VALUES
    (0,'black','originally'),
    (1,'gaunt','originally'),
    (2,'lestrange','originally'),
    (3,'malfoy','originally'),
    (4,'carrow','originally'),
    (5,'greengrass','originally'),
    (6,'ollivander','originally'),
    (7,'parkinson','originally'),
    (8,'gowin','advocated_by_Seika');

EOF

echo "Database schema successfully created in $DB_FILE"
