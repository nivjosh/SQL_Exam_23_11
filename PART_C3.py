#Q3
import sqlite3
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
movie_name = input("Enter movie name: ")
genre = input("Enter genre: ")
country = input("Enter country: ")
language = input("Enter language: ")
year = int(input("Enter release year: "))
revenue = float(input("Enter revenue: "))
cursor.execute("""
    INSERT INTO movies (movie_name, genre, country, language, year, revenue)
    VALUES (?, ?, ?, ?, ?, ?);
""", (movie_name, genre, country, language, year, revenue))

conn.commit()
conn.close()