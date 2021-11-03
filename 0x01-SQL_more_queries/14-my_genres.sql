-- List genres for 'Dexter'
-- Dexter could be any id
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter"

