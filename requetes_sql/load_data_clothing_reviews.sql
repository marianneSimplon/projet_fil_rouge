LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Womens Clothing E-Commerce Reviews.csv"
IGNORE INTO TABLE  clothing_reviews
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(@unamed,Clothing_ID,Age,Title,Review_Text,Rating,Recommended_IND,Positive_Feedback_Count,Division_Name,Department_Name,Class_Name)