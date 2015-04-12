import sqlite3

database = sqlite3.connect("cinema.db")
cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS movies
              (id INTEGER PRIMARY KEY, name TEXT, rating REAL)''')
database.commit()

id1 = 1
name1 = "The Hunger Games: Catching Fire"
rating1 = 7.9
cursor.execute('''INSERT into movies(id, name, rating)
               VALUES(?, ?, ?)''', (id1, name1, rating1))
database.commit()

id2 = 2
name2 = "Wreck-it Ralph"
rating2 = 7.8
cursor.execute('''INSERT into movies(id, name, rating)
               VALUES(?, ?, ?)''', (id2, name2, rating2))
database.commit()

id3 = 3
name3 = "Her"
rating3 = 8.3
cursor.execute('''INSERT into movies(id, name, rating)
                VALUES(?, ?, ?)''', (id3, name3, rating3))
database.commit()
