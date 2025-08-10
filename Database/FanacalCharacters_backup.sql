PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE educational_institutions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
INSERT INTO educational_institutions VALUES(0,'hogwarts');
INSERT INTO educational_institutions VALUES(1,'beauxbâtons');
INSERT INTO educational_institutions VALUES(2,'durmstrang');
INSERT INTO educational_institutions VALUES(3,'ilvermorny');
INSERT INTO educational_institutions VALUES(4,'koldovstoretz');
INSERT INTO educational_institutions VALUES(5,'uagadou');
INSERT INTO educational_institutions VALUES(6,'castelobruxo');
INSERT INTO educational_institutions VALUES(7,'mahoutokoro');
CREATE TABLE lineages (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);
INSERT INTO lineages VALUES(0,'black','originally');
INSERT INTO lineages VALUES(1,'gaunt','originally');
INSERT INTO lineages VALUES(2,'lestrange','originally');
INSERT INTO lineages VALUES(3,'malfoy','originally');
INSERT INTO lineages VALUES(4,'carrow','originally');
INSERT INTO lineages VALUES(5,'greengrass','originally');
INSERT INTO lineages VALUES(6,'ollivander','originally');
INSERT INTO lineages VALUES(7,'parkinson','originally');
INSERT INTO lineages VALUES(8,'gowin','advocated_by_Seika');
INSERT INTO lineages VALUES(9,'floures','advocated_by_Seika');
INSERT INTO lineages VALUES(10,'adel','advocated_by_Seika');
INSERT INTO lineages VALUES(11,'meredith','advocated_by_Seika');
INSERT INTO lineages VALUES(12,'封孫','advocated_by_Constantine');
INSERT INTO lineages VALUES(13,'Libau','advocated_by_Constantine');
CREATE TABLE houses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    institution_id INTEGER,
    FOREIGN KEY (institution_id) REFERENCES educational_institutions(id),
    UNIQUE (id, institution_id)
);
INSERT INTO houses VALUES(0,'gryffindor',0);
INSERT INTO houses VALUES(1,'slytherin',0);
INSERT INTO houses VALUES(2,'ravenclaw',0);
INSERT INTO houses VALUES(3,'hufflepuff',0);
INSERT INTO houses VALUES(4,'thunderbird',3);
INSERT INTO houses VALUES(5,'wampus',3);
INSERT INTO houses VALUES(6,'horned_serpent',3);
INSERT INTO houses VALUES(7,'pukwudgie',3);
CREATE TABLE characters (
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
    FOREIGN KEY (lineage_id) REFERENCES lineages(id),
    FOREIGN KEY (house_id, institution_id) REFERENCES houses(id, institution_id)
);
INSERT INTO characters VALUES(0,'Hortensia','Crimson','Gowin',NULL,0,1,8,'1955-6-26',NULL,'male','man','hetero','pure','made_by_Seika');
INSERT INTO characters VALUES(1,'Clover','Vermillion','Gowin',NULL,0,1,8,'1955-6-26',NULL,'male','man','hetero','pure','made_by_Seika');
INSERT INTO characters VALUES(2,'Galina','Yuhtlahm','Fungsyun',NULL,0,1,12,'1958-3-27',NULL,'female','women','hetero?','pure','made_by_Constantine');
INSERT INTO characters VALUES(3,'Angraecum',NULL,'Gowin',NULL,0,1,8,'1975-12-8',NULL,'female','women','hetero?','pure','made_by_Seika');
INSERT INTO characters VALUES(4,'Marry',NULL,'Gowin',NULL,0,1,8,'1971-11-29',NULL,'female','women','hetero?','pure','made_by_Seika');
INSERT INTO characters VALUES(5,'Gennad','Jaerius','Merspiegal',NULL,NULL,NULL,NULL,'1931-1-31',NULL,'male','man','gay','pure','made_by_Constantine');
INSERT INTO characters VALUES(6,'Eustace','Thetisius','Fitzarthur',NULL,0,1,13,'1956-6-16',NULL,'male','man','bi','pure','made_by_Constantine');
INSERT INTO characters VALUES(7,'Gideon',NULL,'Giesbelt',NULL,0,0,NULL,'1972-11-27',NULL,'male','man','hetero','half-pure','made_by_Constantine');
INSERT INTO characters VALUES(8,'Yksel','Adrian','Nicnessa',NULL,0,0,NULL,'1982-1-3',NULL,'male','man',NULL,'muggle-born/half-pure','made_by_Constantine');
INSERT INTO characters VALUES(9,'Elisha','Dexter','Lísbetdóttir',NULL,0,3,NULL,'1980-9-22',NULL,'male','man',NULL,'muggle-born','made_by_Constantine');
INSERT INTO characters VALUES(10,'Melchior-Mechthild','Marcellus','Murganatoht',NULL,0,2,NULL,'1989-10-30',NULL,'null','null','null','pure??','made_by_Constantine');
INSERT INTO characters VALUES(11,'Frances',NULL,'Oswetry',NULL,2,NULL,12,'1973-10-12',NULL,'female','woman','omni','half-pure','made_by_Constantine');
INSERT INTO characters VALUES(12,'Richarda','Uliela','Libau-Kursdolf',NULL,0,0,13,'1934-09-29',NULL,'female','woman',NULL,'half-pure','made_by_Constantine');
INSERT INTO characters VALUES(13,'Barnaba','Ramiela','Libau-Kursdolf',NULL,0,3,13,'1958-01-20',NULL,'female','woman','lesb','half-pure','made_by_Constantine');
INSERT INTO characters VALUES(14,'Hettia','Cassiela','Libau-Kursdolf',NULL,0,0,13,'1967-08-19',NULL,'female','woman',NULL,'half-pure','made_by_Constantine');
INSERT INTO characters VALUES(15,'Ascane','滄慧','Pressine',NULL,0,0,12,'1954-05-01',NULL,'male','man',NULL,'pure','made_by_Constantine');
INSERT INTO characters VALUES(16,'Rochadh','','Altmore',NULL,0,0,NULL,'2006-08-03',NULL,'male','?',NULL,'muggle-born','made_by_Constantine');
INSERT INTO characters VALUES(17,'Arthur','Klaus','Illyrger',NULL,0,0,NULL,'1933-07-01',NULL,'male','man','gay','muggle-born',NULL);
CREATE TABLE IF NOT EXISTS "enrollment" (
    id INTEGER PRIMARY KEY,
    character_id INTEGER NOT NULL,
    institution_id INTEGER NOT NULL,
    enrollment_year INTEGER NOT NULL,
    graduation_year INTEGER,
    notes TEXT,
    FOREIGN KEY (character_id) REFERENCES characters(id),
    FOREIGN KEY (institution_id) REFERENCES educational_institutions(id)
);
INSERT INTO enrollment VALUES(1,0,0,1966,1972,NULL);
INSERT INTO enrollment VALUES(2,1,0,1966,1972,NULL);
INSERT INTO enrollment VALUES(3,2,0,1969,1975,NULL);
INSERT INTO enrollment VALUES(4,3,0,1987,1993,NULL);
INSERT INTO enrollment VALUES(5,4,0,1983,1989,NULL);
INSERT INTO enrollment VALUES(6,6,0,1967,1973,NULL);
INSERT INTO enrollment VALUES(7,7,0,1984,1990,NULL);
INSERT INTO enrollment VALUES(8,8,0,1993,1999,NULL);
INSERT INTO enrollment VALUES(9,9,0,1992,1998,NULL);
INSERT INTO enrollment VALUES(10,10,0,2001,2007,NULL);
INSERT INTO enrollment VALUES(11,11,2,1985,1993,NULL);
INSERT INTO enrollment VALUES(12,12,0,1946,1953,NULL);
INSERT INTO enrollment VALUES(13,13,0,1969,1975,NULL);
INSERT INTO enrollment VALUES(14,14,0,1978,1984,NULL);
INSERT INTO enrollment VALUES(15,15,0,1965,1971,NULL);
INSERT INTO enrollment VALUES(16,16,0,2017,2023,NULL);
INSERT INTO enrollment VALUES(17,17,0,1944,1950,NULL);
CREATE TABLE relationship_types (
    id INTEGER PRIMARY KEY,
    type_name TEXT NOT NULL UNIQUE,
    is_bidirectional BOOLEAN NOT NULL
);
INSERT INTO relationship_types VALUES(1,'parent-child',0);
INSERT INTO relationship_types VALUES(2,'friends',1);
INSERT INTO relationship_types VALUES(3,'married',1);
INSERT INTO relationship_types VALUES(4,'crush',0);
INSERT INTO relationship_types VALUES(5,'sibling',1);
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
