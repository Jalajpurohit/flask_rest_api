from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/N04399/Desktop/projects/flask_rest_api/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
