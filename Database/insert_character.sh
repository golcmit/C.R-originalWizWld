#!/bin/bash


DB_FILE="FanacalCharacters.db"

sqlite3 "$DB_FILE" <<'EOF'
INSERT INTO characters (id,first_name,middle_name,current_last_name,institution_id,house_id,lineage_id,birth_date,sex,gender,sexual_orientation,blood_status,notes)VALUES
    (0,'Hortensia','Crimson','Gowin',0,1,8,1955-6-26,'male','man','hetero','pure','made_by_Seika'),
    (1,'Clover','Vermillion','Gowin',0,1,8,1955-6-26,'male','man','hetero','pure','made_by_Seika');

EOF
echo 'SUCCESS!!!!!!!!!!!!!!'