CREATE DATABASE IF NOT EXISTS sentiment_analysis_bdd;
USE sentiment_analysis_bdd;

CREATE TABLE IF NOT EXISTS divisions (
divisions_id INT AUTO_INCREMENT,
division_name VARCHAR(50),
PRIMARY KEY (divisions_id)
);

CREATE TABLE IF NOT EXISTS departments (
departments_id INT AUTO_INCREMENT,
department_name VARCHAR(50),
PRIMARY KEY (departments_id)
);

CREATE TABLE IF NOT EXISTS classes (
classes_id INT AUTO_INCREMENT,
class_name VARCHAR(50),
PRIMARY KEY (classes_id)
);

CREATE TABLE IF NOT EXISTS clothes (
clothes_id INT AUTO_INCREMENT,
clothes_divisions_id INT,
clothes_departments_id INT,
clothes_classes_id INT,
PRIMARY KEY (clothes_id),
FOREIGN KEY (clothes_divisions_id) REFERENCES divisions(divisions_id),
FOREIGN KEY (clothes_departments_id) REFERENCES departments(departments_id),
FOREIGN KEY (clothes_classes_id) REFERENCES classes(classes_id)
);

CREATE TABLE IF NOT EXISTS reviews (
reviews_id INT AUTO_INCREMENT,
reviews_clothes_id INT,
age INT,
title VARCHAR(200),
review_text TEXT,
rating INT,
recommended_ind TINYINT(1),
positive_feedback_count INT,
PRIMARY KEY (reviews_id),
FOREIGN KEY (reviews_clothes_id) REFERENCES clothes(clothes_id)
);
