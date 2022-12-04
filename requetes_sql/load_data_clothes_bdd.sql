LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clothes.csv"
IGNORE INTO TABLE  clothes
FIELDS TERMINATED BY ','
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(clothes_id,clothes_divisions_id,clothes_departments_id,clothes_classes_id)