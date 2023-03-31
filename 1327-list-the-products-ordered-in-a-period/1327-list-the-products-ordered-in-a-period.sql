# Write your MySQL query statement below
SELECT product_name,SUM(unit) AS unit FROM Products JOIN
Orders USING(product_id)
WHERE MONTH(order_date) = 2
GROUP BY product_id
HAVING unit>=100