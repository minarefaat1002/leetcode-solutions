# Write your MySQL query statement below
SELECT P.product_id,ROUND(SUM(U.units*P.price)/SUM(U.units),2) AS average_price FROM Prices P JOIN 
UnitsSold U ON (U.product_id = P.product_id AND purchase_date BETWEEN P.start_date AND P.end_date)
GROUP BY product_id