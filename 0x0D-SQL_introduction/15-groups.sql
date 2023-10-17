-- count score from table and group it by score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
