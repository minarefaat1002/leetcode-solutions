# Write your MySQL query statement below
SELECT id FROM Weather w1 WHERE w1.temperature > (SELECT temperature FROM Weather WHERE recordDate =w1.recordDate - interval 1 day)