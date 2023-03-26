# Write your MySQL query statement below
SELECT id,
"Root" AS type FROM Tree
WHERE P_id IS NULL
UNION 
SELECT id,"Inner" FROM Tree T
WHERE P_id IS NOT NULL AND (
EXISTS (
SELECT * FROM Tree WHERE P_id = T.id
)
)
UNION 
SELECT id,"Leaf" AS type FROM Tree T 
WHERE p_ID is not null AND (
NOT EXISTS (
SELECT * FROM Tree WHERE P_id = T.id
)
)