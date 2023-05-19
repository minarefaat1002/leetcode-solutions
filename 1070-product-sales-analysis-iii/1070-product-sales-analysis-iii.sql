# Write your MySQL query statement below
SELECT product_id,year AS first_year,quantity AS quantity,price FROM (
SELECT product_id,year,quantity,price,DENSE_RANK() OVER(PARTITION BY product_id ORDER BY year) AS dr FROM Sales
    ) AS alias
    WHERE dr = 1