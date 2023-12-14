-- Lists all shows in the hbtn_0d_tvshows database that have at least one linked genre
-- Retrieves specific columns from the tv_shows and tv_show_genres tables
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
