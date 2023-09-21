# Write your MySQL query statement below
select 
  customer_id, COUNT(if(transaction_id is null,1,null)) as count_no_trans
  from visits v
  left join transactions t
  on v.visit_id = t.visit_id
  group by customer_id
  having count_no_trans >0;