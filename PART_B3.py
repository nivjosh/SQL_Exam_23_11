JOIN Queries

Q1:
SELECT t.first_name, c.country_name
FROM tourists t
INNER JOIN countries c ON t.country_id = c.id

Q2:
SELECT t.*, tr.*
FROM tourists t
INNER JOIN tours tr ON t.tour_id = tr.id

Q3:
SELECT t.*, tr.*
FROM tourists t
LEFT JOIN tours tr ON t.tour_id = tr.id

Q4:
SELECT t.*, tr.*
FROM tourists t
FULL JOIN tours tr ON t.tour_id = tr.id

Q5:
SELECT t.*, tr.*
FROM tourists t
LEFT JOIN tours tr ON t.tour_id = tr.id
UNION
SELECT t.*, tr.*
FROM tours tr
LEFT JOIN tourists t ON tr.id = t.tour_id

