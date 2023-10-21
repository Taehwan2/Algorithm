# Write your MySQL query statement below
delete
from person
where id not in (
    select min(id) 
    from (select * from person) as p2
    group by email
)