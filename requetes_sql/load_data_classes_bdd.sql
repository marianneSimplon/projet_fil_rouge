LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/classes.csv"
IGNORE INTO TABLE  classes
FIELDS TERMINATED BY ','
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(classes_id,class_name)