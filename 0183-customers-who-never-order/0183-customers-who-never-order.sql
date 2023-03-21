# Write your MySQL query statement below
# SELECT name AS Customers FROM Customers WHERE id NOT IN (SELECT customerId FROM Orders)
SELECT name AS customers FROM Customers 
LEFT JOIN Orders 
ON Customers.id = Orders.customerId
WHERE orders.id IS NULL