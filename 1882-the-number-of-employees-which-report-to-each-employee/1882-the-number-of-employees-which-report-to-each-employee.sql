# Write your MySQL query statement below
select em.employee_id, em.name, count(em2.reports_to) as reports_count, round(avg(em2.age),0) as average_age
from Employees em inner join Employees em2 on em.employee_id = em2.reports_to 
group by employee_id 
order by em.employee_id 