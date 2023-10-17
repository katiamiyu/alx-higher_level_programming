-- list all non null records in table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
