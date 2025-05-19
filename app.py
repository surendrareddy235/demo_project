from flask import Flask
from __init__.db import get_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'



with app.app_context():
    get_conn()

@app.route('/')
def index():
    return 'Welcome to the Flask Auth App!'

if __name__ == '__main__':
    app.run(debug=True)
