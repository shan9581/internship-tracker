from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Email, EqualTo, ValidationError
from mainProject.models import User


class ApplicationForm(FlaskForm):
    company_name = StringField('Company', validators=[DataRequired(), Length(max=100)])
    role = StringField('Role', validators=[Optional(),Length(max=100)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=500)])
    url = StringField('URL', validators=[Optional(), Length(max=1000)])
    pay = StringField('Pay', validators=[Optional(), Length(max=100)])


    submit = SubmitField('Submit')



class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=100), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(max=20, min=3)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100, min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=100,min=2), EqualTo('password')])

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another')

    def validate_email(self,email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose another')
    
        
    submit = SubmitField('Submit')   


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=100), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)])
    remember = BooleanField('Remember Me', validators = [Optional()])
    
    submit = SubmitField('Submit')   
