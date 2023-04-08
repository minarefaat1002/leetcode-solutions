# Write your MySQL query statement below
SELECT machine_id,
ROUND((SUM(IF(A.activity_type="end",timestamp,0)) - SUM(IF(A.activity_type="start",timestamp,0)))/(COUNT(DISTINCT process_id)),3) processing_time 
FROM Activity A
GROUP BY machine_id