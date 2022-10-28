CREATE DATABASE IF NOT EXISTS sentiment_analysis;
USE sentiment_analysis;

CREATE TABLE IF NOT EXISTS clothing_reviews (
id_clothing_reviews INT AUTO_INCREMENT,
Clothing_ID INT,
Age INT,
Title VARCHAR(200),
Review_Text TEXT,
Rating INT,
Recommended_IND TINYINT(1),
Positive_Feedback_Count INT,
Division_Name VARCHAR(50),
Department_Name VARCHAR(50),
Class_Name VARCHAR(50),
PRIMARY KEY (id_clothing_reviews)
);