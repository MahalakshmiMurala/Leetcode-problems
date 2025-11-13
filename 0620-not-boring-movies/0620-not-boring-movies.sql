# Write your MySQL query statement below
select * from cinema where id%2=1 and description!='boring' order by rating desc;
-- SELECT *
-- FROM Cinema
-- WHERE id % 2 = 1
--   AND description != 'boring'
-- ORDER BY rating DESC;
