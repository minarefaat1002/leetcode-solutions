# Write your MySQL query statement below
UPDATE salary
SET sex = CASE WHEN sex LIKE 'm' THEN 'f' else 'm' end
/*

UPDATE salary
SET
    sex = CASE sex
        WHEN 'm' THEN 'f'
        ELSE 'm'
    END;
*/