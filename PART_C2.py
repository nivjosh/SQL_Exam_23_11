#Q2
import sqlite3
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
search_name = input("Enter movie name: ")
cursor.execute("SELECT * FROM movies WHERE movie_name LIKE ", (f"%{search_name}%",))
results = cursor.fetchall()
for movie in results:
    print(movie)

conn.close()