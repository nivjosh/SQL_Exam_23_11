EXAM PART B 2 GROUP BY Queries:

Q1.
SELECT genre ,count(*)
FROM movies
GROUP BY genre

Q2.
SELECT year ,SUM(revenue)
FROM movies
GROUP BY year

Q3.
SELECT genre ,avg(revenue)
FROM movies
GROUP BY genre

Q4:
SELECT genre,language ,avg(revenue)
FROM movies
GROUP BY language ,genre

Q5:
SELECT language, count(*) AS movie_count
FROM movies
GROUP BY language
ORDER BY movie_count ASC
LIMIT 1

Q6 .
SELECT country, count(*) AS most_movies
FROM movies
GROUP BY country
ORDER BY most_movies DESC
LIMIT 1

Q7.
SELECT genre ,count(*) AS movie_count
FROM movies
GROUP BY genre
HAVING count(*)>2

Q8:
SELECT year ,sum(revenue) AS  total_revenue
FROM movies
GROUP BY revenue
HAVING sum(revenue)>1000


