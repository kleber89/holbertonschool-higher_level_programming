-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql) --

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
