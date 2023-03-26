# Write your MySQL query statement below
SELECT DISTINCT L1.num AS ConsecutiveNums FROM 
LOGS L1,
LOGS L2,
LOGS L3 
WHERE 
L2.id = L1.id-1 AND 
L3.id = L2.id-1 AND 
L1.num = L2.num AND
l2.num = L3.num