# Write your MySQL query statement below
SELECT r.contest_id, ROUND(100*COUNT(r.user_id)/(SELECT COUNT(*) FROM Users),2) as percentage
FROM Register r
INNER JOIN Users u
ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id