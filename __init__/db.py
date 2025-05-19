import sqlite3

def init_db():
    con = sqlite3.connect("demo.db")

    cursor = con.cursor()

    cursor.execute('''
        create table if not exists users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()

def get_connection():
    conn = sqlite3.connect('demo.db')
    conn.row_factory = sqlite3.Row
    return conn


