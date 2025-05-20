from __init__.db import get_connection

def signup(email, password):
    con = get_connection()
    cursor = con.cursor()

    cursor.execute("select * from users where email= ?", (email,))
    existing = cursor.fetchone()
    if existing:
        con.close()
        return "email already existing"
    
    cursor.execute("insert into users (email,password) values(?,?)", (email, password))
    con.commit()
    con.close()
    return "signup successful"
    
    
