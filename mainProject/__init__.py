#imports
#flask and SQLAlchemy
#flask hangles HTML, gives templates, allows jinja2 (python in html)
from flask import Flask
#sqlalchemy is a database toolkit, allows tables as python classes, and querying
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from flask_migrate import Migrate



#this line creates application object that everything is built around, name is the project name "mainProject" in this file
#its saying the app is flask based and points to the name
app = Flask(__name__)

#app has settings called config
#SQLALCHEMY_DATABASE_URI is a setting and we are setting its value
#sqlite:///site.db tells it that it is a sqlite database located in a file named internships.db
database_url = os.environ.get('DATABASE_URL', 'sqlite:///internships.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

#makes key that flask uses to sign data
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tempkey')

#db is an object that can talk to the database
#db.Model allows a class to become a table
#db.Column adds a column to a table
db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#this line is for sending people to the login page when they are logged out and accesing a page that needs login
login_manager.login_view = 'login'


#routes import must be at bottom to avoid a circular import
from mainProject import routes