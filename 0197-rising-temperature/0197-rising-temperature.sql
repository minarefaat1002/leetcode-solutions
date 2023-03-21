# Write your MySQL query statement below
SELECT id FROM Weather w1 WHERE w1.temperature > (SELECT temperature FROM Weather WHERE recordDate =w1.recordDate - interval 1 day)




# SELECT
#     weather.id AS 'Id'
# FROM
#     weather
#         JOIN
#     weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
#         AND weather.Temperature > w.Temperature