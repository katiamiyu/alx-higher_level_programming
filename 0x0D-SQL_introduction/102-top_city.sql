-- selecting top 3 cities with highest temp between month 7 to 8
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
