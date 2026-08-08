from mainProject import app
from flask import render_template
from mainProject.models import InternshipApplication


@app.route("/")
def home():
    applications = InternshipApplication.query.all()
    return render_template('home.html', applications=applications)