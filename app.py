from flask import Flask
from __init__.db import get_connection, init_db
from routes.signuproute import demo

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(demo)


with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
