# Write your MySQL query statement below
(select u.name as results
from MovieRating mr
inner join Users u on u.user_id = mr.user_id
group by u.user_id
order by COUNT(rating) DESC, u.name
limit 1)

union all

(select m.title as results
from MovieRating mr
inner join Movies m on mr.movie_id = m.movie_id
where mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
group by m.movie_id
order by AVG(rating) DESC, m.title
limit 1) 