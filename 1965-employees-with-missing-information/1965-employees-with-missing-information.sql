# Write your MySQL query statement below
SELECT employee_id FROM (
SELECT employee_id FROM Employees
LEFT JOIN Salaries USING(employee_id)
WHERE salary IS NULL
UNION
SELECT employee_id FROM Employees
RIGHT JOIN Salaries USING(employee_id)
WHERE name IS NULL
    ) AS alias
ORDER BY employee_id ASC