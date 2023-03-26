# Write your MySQL query statement below
SELECT * FROM (
SELECT IF(S.id!=(SELECT MAX(id) FROM Seat),id+1,id) AS id,student FROM Seat S WHERE id%2 = 1
UNION 
SELECT id-1,student FROM Seat WHERE id%2 =0
) AS Alias ORDER BY id