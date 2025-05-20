from flask import render_template, request, redirect, url_for
from models.signuplogic import signup
from flask import Blueprint

demo = Blueprint("demo", __name__)

@demo.route('/')
def showsignup():
    return render_template('signup.html')

@demo.route("/signupform", methods=["POST"])
def showsignupform():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        result = signup(email,password)
        if result == 'signup successful':
            return render_template('login.html')
        else:
            return result
