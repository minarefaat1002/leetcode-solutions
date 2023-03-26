# Write your MySQL query statement below
SELECT buyer_id,join_date,COUNT(order_id) AS orders_in_2019 FROM 
(
SELECT user_id AS buyer_id,join_date,order_id FROM Users LEFT JOIN
Orders 
ON (buyer_id = user_id AND YEAR(order_date) = 2019)
) AS Alias
GROUP BY buyer_id