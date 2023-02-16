# Write your MySQL query statement below
/*
IF(condition, value_if_true, value_if_false)
select 
    employee_id,
    if(employee_id%2!=0 and name NOT LIKE 'M%',salary,0) as bonus 
from Employees 
order by employee_id
*/
/*
        -- select entries with odd  employee id and name not start with M
            select employee_id , salary as bonus 
            from employees 
            where employee_id%2 <>0 and name not like 'M%'
            
        -- join both selection 
            union
            
        -- select remaining entries from table 
            select employee_id , 0 as bonus
            from employees
            where employee_id%2 = 0 or name like 'M%'
            order by employee_id;
*/
/*
select employee_id , 
   case when employee_id%2 <>0 and name not like 'M%' then salary 
   else 0
   end 
   as bonus
   from employees
   order by employee_id;
   */
SELECT employee_id,
CASE WHEN employee_id%2 != 0 and name NOT LIKE 'M%' THEN salary
else 0
end
as bonus 
FROM employees
order by employee_id