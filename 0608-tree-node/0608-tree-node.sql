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

# NOT IN didn't work due to null

# Previously I had

# SELECT id,
#     CASE
#         WHEN p_id IS null THEN 'Root'
#         WHEN id NOT IN (SELECT p_id FROM tree) THEN 'Leaf'
#         ELSE 'Inner'
#     END AS Type
# FROM tree
# Error.
# Because for example

# 3 NOT IN (null, 1, 2)
# returns null and hence not identified as 'Leaf'.

# Take out null and it works fine:

# SELECT id,
#     CASE
#         WHEN p_id IS null THEN 'Root'
#         WHEN id NOT IN (SELECT p_id FROM tree WHERE p_id IS NOT null) THEN 'Leaf'
#         ELSE 'Inner'
#     END AS Type
# FROM tree






# The problem is caused by NOT IN . NOT IN returns 0 records when compared against an unknown value.
# Since NULL is an unknown, a NOT IN query containing a NULL or NULLs in the list of possible values will always return 0 records since there is no way to be sure that the NULL value is not the value being tested.