from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app config

UPLOAD_FOLDER = './app/static/Profilepics'
app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
