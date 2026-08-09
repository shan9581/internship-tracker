from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional 

class ApplicationForm(FlaskForm):
    company_name = StringField('Company', validators=[DataRequired(), Length(max=100)])
    role = StringField('Role', validators=[Optional(),Length(max=100)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=500)])
    url = StringField('URL', validators=[Optional(), Length(max=1000)])
    pay = StringField('Pay', validators=[Optional(), Length(max=100)])


    submit = SubmitField('Submit')