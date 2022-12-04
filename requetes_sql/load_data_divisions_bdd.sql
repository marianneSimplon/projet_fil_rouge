LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/divisions.csv"
IGNORE INTO TABLE  divisions
FIELDS TERMINATED BY ','
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(divisions_id,division_name)