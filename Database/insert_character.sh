#!/bin/bash


DB_FILE="FanacalCharacters.db"

sqlite3 "$DB_FILE" <<'EOF'
INSERT INTO characters (id,first_name,middle_name,current_last_name,institution_id,house_id,lineage_id,birth_date,sex,gender,sexual_orientation,blood_status,notes)VALUES
    (3,'Angraecum',,'Gowin',0,1,8,'1975-12-8','female','woman','hetero?','pure','made_by_Seika'),
    (4,'Framces',,'Fungsyun',2,,12,'1973-10-12','female','demi-girl?','omni','harf-pure','made_by_Constantine'),
    (5,'',,'Gowin',0,1,8,)
EOF
echo 'SUCCESS!!!!!!!!!!!!!!'