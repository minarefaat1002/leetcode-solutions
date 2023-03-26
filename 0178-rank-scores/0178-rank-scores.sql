# Write your MySQL query statement below
# WINDOW FUNCTION 
SELECT score,DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"  FROM Scores