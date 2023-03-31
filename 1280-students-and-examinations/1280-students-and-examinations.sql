# Write your MySQL query statement below
SELECT 
    student_id, 
    student_name, 
    subject_name, 
    COUNT(E.subject_name) AS attended_exams
FROM 
    Students 
    CROSS JOIN Subjects
    LEFT JOIN Examinations E USING (student_id, subject_name)
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name;