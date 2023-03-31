# Write your MySQL query statement below
SELECT name,bonus FROM Employee 
LEFT JOIN Bonus USING(empId)
HAVING (bonus < 1000 OR bonus IS NULL)