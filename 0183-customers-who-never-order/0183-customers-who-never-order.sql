# Write your MySQL query statement below
SELECT name as customers FROM customers WHERE id NOT IN (SELECT customerId FROM orders)
