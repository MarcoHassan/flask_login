# general flask functionalities for rendering and interacting with front-end
from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm

from flask_login import current_user, login_user, login_required, logout_user
from flask import render_template, url_for, redirect, flash

pID = None

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('test'))
    form = LoginForm() ## leverages the loginform specified in the other module
    if form.validate_on_submit():        
        user = User.query.filter_by(username=form.username.data).first()
        global pID
        pID = form.patientID.data
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('test'))
    
    return render_template('hel_temp.html', title='Sign In', form=form)

# App logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register_nice.html', title='Register', form=form)

# Endpoints
@app.route('/api/home', methods=['GET'])
@login_required
def example():    
    return 'hello world' + ' registered pID: ' + pID

@app.route('/api/test', methods=['GET'])
@login_required
def test():
    return 'hello world test'
