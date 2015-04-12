import sqlite3

database = sqlite3.connect("cinema.db")
cursor = database.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
              (id INTEGER PRIMARY KEY, username TEXT,
               projection_id INTEGER, row INTEGER, col INTEGER,
               FOREIGN KEY (projection_id) REFERENCES projections (id))''')
database.commit()

id1 = 1
username1 = "RadoRado"
projection1 = 1
row1 = 1
col1 = 2
cursor.execute('''INSERT into reservations(id, username, projection_id, row, col)
                VALUES(?, ?, ?, ?, ?)''', (id1, username1, projection1, row1, col1))
database.commit()
