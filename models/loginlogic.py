import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from flask import flash








def loginlogic(email,password):
    con = sqlite3.connect("demo.db")

    cursor = con.cursor()

    cursor.execute("select * from users where email=?" ,(email,))
    user =cursor.fetchone()
    con.close()
