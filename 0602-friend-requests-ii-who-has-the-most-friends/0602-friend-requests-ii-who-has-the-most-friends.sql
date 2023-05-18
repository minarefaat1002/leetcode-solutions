# Write your MySQL query statement below

SELECT id,SUM(num) AS num FROM
(
SELECT requester_id AS id, COUNT(*) AS num FROM RequestAccepted 
GROUP BY requester_id 
UNION ALL
SELECT accepter_id AS id,COUNT(*) AS num FROM RequestAccepted 
GROUP BY accepter_id
    ) AS alias
    GROUP BY id 
    ORDER BY SUM(num) DESC
    LIMIT 1
    
    /*
    # Write your MySQL query statement below

select requester_id as id,
       (select count(*) from RequestAccepted
            where id=requester_id or id=accepter_id) as num
from RequestAccepted
group by requester_id
order by num desc limit 1
    */