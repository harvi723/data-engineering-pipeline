-- Average marks by department
SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

-- Top students
SELECT *
FROM students
ORDER BY marks DESC;

-- Count grades
SELECT grade, COUNT(*) AS cnt
FROM students
GROUP BY grade;
