# Write your MySQL query statement below
select w.employee_id 
from Employees w
where salary < 30000 and w.manager_id NOT IN (
    select s.employee_id
    from Employees s
)
order by w.employee_id;