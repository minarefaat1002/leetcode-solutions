# Write your MySQL query statement below
SELECT customer_id,COUNT(*) AS count_no_trans FROM Visits
WHERE visit_id NOT IN (
    SELECT V.visit_id FROM Visits V JOIN
    Transactions T ON V.visit_id = T.visit_id
) 
GROUP BY customer_id