# Write your MySQL query statement below
SELECT Department.name AS 'Department',
Employee.name AS 'Employee',Salary
FROM Employee JOIN
Department ON Employee.DepartmentId = Department.Id
WHERE 
(Employee.DepartmentId,Salary) IN (
SELECT DepartmentId,Max(Salary) FROM Employee
GROUP BY DepartmentId
)
