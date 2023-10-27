# Write your MySQL query statement below
select visited_on, amount, average_amount
from (select visited_on , sum(total)
 over(order by visited_on rows between 6 preceding and current row ) as amount,
round(avg(total)over(order by visited_on rows between 6 preceding and current row ),2)as average_amount,
row_number() over(order by visited_on) as rnk
from (select visited_on, sum(amount) as total from Customer group by visited_on)x)y
where rnk>6