-- listing all the cities in the database using join
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY id;
