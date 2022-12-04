LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/reviews.csv"
IGNORE INTO TABLE  reviews
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(reviews_id,reviews_clothes_id,age,title,review_text,rating,recommended_ind,positive_feedback_count)