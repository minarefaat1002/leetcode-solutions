# Write your MySQL query statement below
SELECT id,
"Root" AS type FROM Tree
WHERE P_id IS NULL
UNION 
SELECT id,"Inner" AS type FROM Tree T
WHERE (T.P_id IS NOT NULL) AND (T.id IN (
SELECT P_id FROM Tree
))
UNION 
SELECT id,"Leaf" AS type FROM Tree T
WHERE (T.P_id IS NOT NULL) AND (T.id NOT IN (
SELECT IFNULL(P_id,0) FROM Tree
))
