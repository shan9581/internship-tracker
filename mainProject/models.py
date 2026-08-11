from datetime import datetime
from mainProject import db, login_manager
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False, unique=True)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False, unique=True)
    applied_internships = db.relationship('InternshipApplication', backref='applicant', lazy = True)

#turns an id back into a user
@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))



#defines what an internship will contain when added, a row in the database
class InternshipApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100),nullable=True)
    date_applied = db.Column(db.DateTime,nullable=True, default = datetime.utcnow)
    pay = db.Column(db.String(100),nullable=True)
    status = db.Column(db.String(100),nullable=True, default = 'applied')
    notes = db.Column(db.String(500),nullable=True)
    url = db.Column(db.String(1000),nullable=True)    

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)