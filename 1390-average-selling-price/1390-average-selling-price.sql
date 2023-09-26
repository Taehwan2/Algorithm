SELECT p.product_id, IFNULL(ROUND(SUM(price * units) / SUM(units), 2),0) AS average_price
FROM Prices AS p
left JOIN UnitsSold AS u ON p.product_id = u.product_id
WHERE u.purchase_date BETWEEN p.start_date AND p.end_date  or u.purchase_date is NULL

GROUP BY p.product_id;