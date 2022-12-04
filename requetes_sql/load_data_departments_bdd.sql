LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/departments.csv"
IGNORE INTO TABLE  departments
FIELDS TERMINATED BY ','
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(departments_id,department_name)