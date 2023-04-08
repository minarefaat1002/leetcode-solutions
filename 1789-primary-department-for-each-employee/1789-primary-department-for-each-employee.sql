# Write your MySQL query statement below
SELECT employee_id, IF(COUNT(*) > 1, SUM(IF(primary_flag="Y",department_id,0)) , SUM(department_id)) AS department_id  FROM Employee
GROUP BY employee_id