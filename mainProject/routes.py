from mainProject import app, db, bcrypt
from flask import render_template,  url_for, redirect, request, flash, abort
from mainProject.models import InternshipApplication, User
from mainProject.forms import ApplicationForm, RegisterForm, LoginForm
from flask_login import current_user,login_user,logout_user, login_required


@app.route("/")
def home():
    if current_user.is_authenticated:
        applications = InternshipApplication.query.filter_by(user_id=current_user.id).all()
    else:
        applications = []
    return render_template('home.html', applications=applications)

#creating a new application route
@app.route("/application/new", methods = ['GET', 'POST'])
@login_required
def new_application():
    form = ApplicationForm()
    if form.validate_on_submit():

       
        application =InternshipApplication(
user_id=current_user.id, company_name =form.company_name.data, role = form.role.data,pay = form.pay.data, url = form.url.data, notes = form.notes.data)
        db.session.add(application)
        db.session.commit()
        flash('Application Added!','success')
        return redirect(url_for('home'))
    return render_template('new_application.html', form=form, legend = "New Application")


#detail route, viewing the details of an applicaiton
@app.route("/application/<int:application_id>")
@login_required
def application(application_id):
    application = InternshipApplication.query.get_or_404(application_id)
    if application.user_id != current_user.id:
        abort(403)
    return render_template('application.html',application=application)


#update an application route
@app.route("/application/<int:application_id>/update", methods = ['GET', 'POST'])
@login_required
def update_application(application_id):
    application = InternshipApplication.query.get_or_404(application_id)
    if application.user_id != current_user.id:
        abort(403)
    form = ApplicationForm()
    if form.validate_on_submit():
        application.company_name =form.company_name.data
        application.role = form.role.data
        application.pay = form.pay.data
        application.url = form.url.data
        application.notes = form.notes.data
        db.session.commit()
        flash('Application Updated!','success')
        return redirect(url_for('home'))
    
    elif request.method == 'GET':
        form.company_name.data = application.company_name
        form.role.data = application.role
        form.pay.data = application.pay
        form.url.data=application.url
        form.notes.data = application.notes

    return render_template('new_application.html', form=form, legend = "Update Application")


@app.route("/application/<int:application_id>/delete", methods = ['POST'])
@login_required
def delete_application(application_id):
    
    application = InternshipApplication.query.get_or_404(application_id)
    if application.user_id != current_user.id:
        abort(403)
    db.session.delete(application)
    db.session.commit()
    
    flash('Application Deleted!!','success')
    return redirect(url_for('home'))


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()


    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,password=hashed_password )
        db.session.add(user)
        db.session.commit()
        flash('Account created!!','success')
        return redirect(url_for('login'))

    
    return render_template('register.html', title = 'Register', form = form)



@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()


    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash('Login Successful!!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password','danger')


    
    return render_template('login.html', title = 'Login', form = form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))