# Write your MySQL query statement below
select accepter_id as id,count(*) as num from (select accepter_id from requestaccepted
union all
select requester_id from requestaccepted) as t
group by id
order by num desc limit 1;