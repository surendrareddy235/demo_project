import sqlite3

con = sqlite3.connect("demo.db")

cursor = con.cursor()

cursor.execute('''
    create table users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
con.commit()
con.close()


