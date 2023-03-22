# Write your MySQL query statement below
# SELECT product_id, product_name
# FROM Sales 
# JOIN Product 
# Using(product_id)
# GROUP BY product_id
# HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31' 


select product_id,product_name
from product p join sales s 
using(product_id)
group by product_id
having COUNT(IF(sale_date<'2019-01-01', 1, NULL))=0
and COUNT(IF(sale_date>'2019-03-31', 1, NULL))=0


# select product_id,product_name
# from product p join sales s 
# using(product_id)
# group by product_id
# having sum(sale_date<"2019-01-01")=0
# and sum(sale_date>"2019-03-31")=0