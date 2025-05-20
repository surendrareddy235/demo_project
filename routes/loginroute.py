from flask import Flask,request,redirect,render_template,flash
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from flask import Blueprint
demo = Blueprint('demo',__name__)

app=Flask(__name__)
app.secret_key='secret'

@demo.route('/login',methods=['POST','GET'])
def login(email,password):
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        hashed_password=generate_password_hash(password)
        user=(email,password)
        if user and check_password_hash(user[2], password):  # Assuming password is in column 3
            flash('Login successful!')
        else:
            flash('Invalid credentials, please try again')
    return render_template('login.html')


