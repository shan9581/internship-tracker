#imports
#flask and SQLAlchemy
#flask hangles HTML, gives templates, allows jinja2 (python in html)
from flask import Flask
#sqlalchemy is a database toolkit, allows tables as python classes, and querying
from flask_sqlalchemy import SQLAlchemy


#this line creates application object that everything is built around, name is the project name "mainProject" in this file
#its saying the app is flask based and points to the name
app = Flask(__name__)

#app has settings called config
#SQLALCHEMY_DATABASE_URI is a setting and we are setting its value
#sqlite:///site.db tells it that it is a sqlite database located in a file named internships.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


#db is an object that can talk to the database
#db.Model allows a class to become a table
#db.Column adds a column to a table
db = SQLAlchemy(app)