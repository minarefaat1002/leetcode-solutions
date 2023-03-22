# Write your MySQL query statement below
SELECT name FROM salesPerson s WHERE s.sales_id NOT IN(
SELECT sales_id FROM orders o WHERE o.com_id = (SELECT com_id FROM company WHERE name = "RED")
    )