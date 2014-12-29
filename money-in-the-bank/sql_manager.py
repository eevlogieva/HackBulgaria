#import requests
import hashlib
import sqlite3
from datetime import datetime, timedelta
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT
                wrong_passes INTEGER DEFAULT 0
                fifth_wrong_pass DATETIME)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_hash_pass = hash_password(new_pass)
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_hash_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    hashed_pass = hash_password(password)
    insert_sql = "INSERT into clients(username, password) VALUES (?, ?)"
    cursor.execute(insert_sql, (username, hashed_pass))
    conn.commit()


def login(username, password):
    select_sql = "SELECT wrong_passes FROM clients WHERE username = ?"
    cursor.execute(select_sql, (username,))
    num_wrong_passes = cursor.fetchone()
    if num_wrong_passes == 5:
        update_sql = "UPDATE clients SET fifth_wrong_pass = ? WHERE username = ?"
        cursor.execute(update_sql, (datetime.now(), username))
        conn.commit()
        num_wrong_passes = 0
        return False
    select_time = "SELECT fifth_wrong_pass FROM clients WHERE username = ?"
    cursor.execute(select_time, (username,))
    fifth_time = cursor.fetchone()
    if num_wrong_passes == 0 and (datetime.now() - fifth_time) < timedelta(minutes=5):
        return False
    else:
        hashed_pass = hash_password(password)
        select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
        cursor.execute(select_query, (username, hashed_pass))
        user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        num_wrong_passes += 1
        update_sql = "UPDATE clients SET wrong_passes = ? WHERE username = ?"
        cursor.execute(update_sql, (num_wrong_passes, username))
        conn.commit()
        return False


def hash_password(password):
    hashed_pass = hashlib.sha1(password.encode('utf-8'))
    return hashed_pass.hexdigest()
