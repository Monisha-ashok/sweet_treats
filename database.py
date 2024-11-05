import sqlite3
from contextlib import contextmanager

DB_NAME = 'sweet_treats.db'

@contextmanager
def db_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn.cursor()
        conn.commit()
    finally:
        conn.close()

def setup_database():
    with db_connection() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SpecialtyTreats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                treat_name TEXT NOT NULL,
                availability TEXT NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                amount INTEGER NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CustomerRequests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                treat_name TEXT NOT NULL,
                requester TEXT NOT NULL,
                dietary_restrictions TEXT
            )
        ''')

setup_database()

# Specialty Treat Functions
def create_treat(treat_name, availability):
    with db_connection() as cursor:
        cursor.execute("INSERT INTO SpecialtyTreats (treat_name, availability) VALUES (?, ?)", (treat_name, availability))

def retrieve_treats():
    with db_connection() as cursor:
        cursor.execute("SELECT * FROM SpecialtyTreats")
        return cursor.fetchall()

def remove_treat(treat_id):
    with db_connection() as cursor:
        cursor.execute("DELETE FROM SpecialtyTreats WHERE id = ?", (treat_id,))

# Stock Management Functions
def add_stock_item(item_name, amount):
    with db_connection() as cursor:
        cursor.execute("INSERT INTO Stock (item_name, amount) VALUES (?, ?)", (item_name, amount))

def get_stock():
    with db_connection() as cursor:
        cursor.execute("SELECT * FROM Stock")
        return cursor.fetchall()

def modify_stock(item_id, new_amount):
    with db_connection() as cursor:
        cursor.execute("UPDATE Stock SET amount = ? WHERE id = ?", (new_amount, item_id))

def remove_stock_item(item_id):
    with db_connection() as cursor:
        cursor.execute("DELETE FROM Stock WHERE id = ?", (item_id,))

# Customer Request Functions
def log_request(treat_name, requester, dietary_restrictions):
    with db_connection() as cursor:
        cursor.execute("INSERT INTO CustomerRequests (treat_name, requester, dietary_restrictions) VALUES (?, ?, ?)", 
                       (treat_name, requester, dietary_restrictions))

def fetch_requests():
    with db_connection() as cursor:
        cursor.execute("SELECT * FROM CustomerRequests")
        return cursor.fetchall()

