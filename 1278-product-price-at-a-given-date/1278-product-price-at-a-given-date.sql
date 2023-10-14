# Write your MySQL query statement below
select
    p0.product_id,
    CASE
        when min(p0.change_date) > DATE("2019-08-16") then 10
        else (
            select new_price
            from Products p1
            where p1.product_id=p0.product_id
            and p1.change_date <= DATE("2019-08-16")
            order by change_date desc
            limit 1
        )
    END as price
from
    Products p0
group by 
    p0.product_id