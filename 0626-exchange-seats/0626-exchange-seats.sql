# Write your MySQL query statement below
SELECT * FROM(
SELECT IF(id != (SELECT MAX(id) FROM Seat), (id+1),id) AS id, (SELECT student FROM Seat WHERE id=S.id ) AS student FROM Seat S WHERE (id%2 = 1)
UNION 
SELECT(id-1),(SELECT student FROM Seat WHERE id = s.id) FROM Seat S WHERE (id%2=0)
) AS Alias ORDER BY id