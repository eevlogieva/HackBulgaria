import sqlite3

database = sqlite3.connect("cinema.db")
cursor = database.cursor()

cursor.execute('''PRAGMA foreign_key = ON''')

cursor.execute('''CREATE TABLE IF NOT EXISTS projections
              (id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT,
              date1 DATE, time1 TIME, FOREIGN KEY (movie_id) REFERENCES movies (id))''')
database.commit()

id1 = 1
movie_id1 = 1
type1 = "3D"
date1 = "2014-04-01"
time1 = "19:10"
cursor.execute('''INSERT into projections (id, movie_id, type, date1, time1)
               VALUES(?, ?, ?, ?, ?)''', (id1, movie_id1, type1, date1, time1))
database.commit()

id2 = 2
movie_id2 = 1
type2 = "2D"
date2 = "2014-04-01"
time2 = "19:00"
cursor.execute('''INSERT into projections (id, movie_id, type, date1, time1)
               VALUES(?, ?, ?, ?, ?)''', (id2, movie_id2, type2, date2, time2))
database.commit()

id3 = 3
movie_id3 = 1
type3 = "4DX"
date3 = "2014-04-02"
time3 = "21:00"
cursor.execute('''INSERT into projections (id, movie_id, type, date1, time1)
               VALUES(?, ?, ?, ?, ?)''', (id3, movie_id3, type3, date3, time3))
database.commit()

id4 = 4
movie_id4 = 3
type4 = "2D"
date4 = "2014-04-05"
time4 = "20:20"
cursor.execute('''INSERT into projections (id, movie_id, type, date1, time1)
               VALUES(?, ?, ?, ?, ?)''', (id4, movie_id4, type4, date4, time4))
database.commit()

id5 = 5
movie_id5 = 2
type5 = "3D"
date5 = "2014-04-02"
time5 = "22:00"
cursor.execute('''INSERT into projections (id, movie_id, type, date1, time1)
               VALUES(?, ?, ?, ?, ?)''', (id5, movie_id5, type5, date5, time5))
database.commit()

id6 = 6
movie_id6 = 2
type6 = "2D"
date6 = "2014-04-02"
time6 = "19:30"
cursor.execute('''INSERT into projections (id, movie_id, type, date1, time1)
               VALUES(?, ?, ?, ?, ?)''', (id6, movie_id6, type6, date6, time6))
database.commit()
