# Write your MySQL query statement below
SELECT stock_name,
SUM(IF(operation='sell',price,-price)) AS capital_gain_loss FROM Stocks 
GROUP BY stock_name