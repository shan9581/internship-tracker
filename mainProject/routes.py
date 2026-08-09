from mainProject import app, db
from flask import render_template,  url_for, redirect
from mainProject.models import InternshipApplication
from mainProject.forms import ApplicationForm

@app.route("/")
def home():
    applications = InternshipApplication.query.all()
    return render_template('home.html', applications=applications)


@app.route("/application/new", methods = ['GET', 'POST'])
def new_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        
        #TODO user id is currently hardcoded to 1
        application =InternshipApplication(
user_id=1, company_name =form.company_name.data, role = form.role.data,pay = form.pay.data, url = form.url.data, notes = form.notes.data)
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_application.html', form=form)