0. Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
1. Write a script that creates the MySQL server user user_0d_1.
2. Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
3. Write a script that creates the table force_name on your MySQL server.
4. Write a script that creates the table id_not_null on your MySQL server.
5. Write a script that creates the table unique_id on your MySQL server.
6. Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server. states description:
id INT unique, auto generated, can’t be null and is a primary key
name VARCHAR(256) can’t be null
If the database hbtn_0d_usa already exists, your script should not fail
If the table states already exists, your script should not fail
7. Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
8. Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
9. Write a script that lists all cities contained in the database hbtn_0d_usa.
10. Import the database dump from hbtn_0d_tvshows to your MySQL server: download

Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
11. mport the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)

Write a script that lists all shows contained in the database hbtn_0d_tvshows.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
If a show doesn’t have a genre, display NULL
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
12. Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)

Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
You can use only one SELECT statement
The database name will be passed as an argument of the mysql command
13. Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
14. Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
15. Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
16. Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
17. Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
19. Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
20. Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
