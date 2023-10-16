# Write your MySQL query statement below
select 'Low Salary' AS category, COUNT(*) as accounts_count 
from Accounts
where income < 20000
union
select 'Average Salary' AS category, COUNT(*) as accounts_count 
from Accounts
where income >= 20000 AND income <= 50000
union
select 'High Salary' AS category, COUNT(*) as accounts_count 
from Accounts
where income > 50000
group by category