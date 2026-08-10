from mainProject import app, db
from flask import render_template,  url_for, redirect, request
from mainProject.models import InternshipApplication
from mainProject.forms import ApplicationForm

@app.route("/")
def home():
    applications = InternshipApplication.query.all()
    return render_template('home.html', applications=applications)

#creating a new application route
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
    return render_template('new_application.html', form=form, legend = "New Application")


#detail route, viewing the details of an applicaiton
@app.route("/application/<int:application_id>")
def application(application_id):
    application = InternshipApplication.query.get_or_404(application_id)
    return render_template('application.html',application=application)


#update an application route
@app.route("/application/<int:application_id>/update", methods = ['GET', 'POST'])
def update_application(application_id):
    application = InternshipApplication.query.get_or_404(application_id)

    form = ApplicationForm()
    if form.validate_on_submit():
        application.company_name =form.company_name.data
        application.role = form.role.data
        application.pay = form.pay.data
        application.url = form.url.data
        application.notes = form.notes.data
        db.session.commit()
        return redirect(url_for('home'))
    
    elif request.method == 'GET':
        form.company_name.data = application.company_name
        form.role.data = application.role
        form.pay.data = application.pay
        form.url.data=application.url
        form.notes.data = application.notes

    return render_template('new_application.html', form=form, legend = "Update Application")


    