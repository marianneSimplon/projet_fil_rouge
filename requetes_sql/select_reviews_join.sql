SELECT reviews_id,reviews_clothes_id,age,title,review_text,rating,recommended_ind,positive_feedback_count,division_name,department_name,class_name
FROM reviews
LEFT JOIN clothes ON reviews.reviews_clothes_id = clothes.clothes_id
LEFT JOIN divisions ON clothes.clothes_divisions_id = divisions.divisions_id
LEFT JOIN departments ON clothes.clothes_departments_id = departments.departments_id
LEFT JOIN classes ON clothes.clothes_classes_id = classes.classes_id