# Write your MySQL query statement below
SELECT 
 round(sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)/count(*)*100,2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);