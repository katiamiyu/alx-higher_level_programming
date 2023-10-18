-- displays all genre in database and shows link to each genre
SELECT tv_genres.name AS genre, COUNT(tv_shows.title) AS number_of_shows 
FROM `tv_genres` INNER JOIN `tv_show_genres` 
ON tv_genres.id = tv_show_genres.genre_id INNER JOIN `tv_shows` 
ON tv_show_genres.show_id = tv_shows.id 
GROUP BY tv_genres.name 
ORDER BY number_of_shows DESC;
