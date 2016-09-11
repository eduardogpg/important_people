#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Eduardo Ismael García Pérez'
__contact__ = '@eduardo_gpg'

from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from flask import Markup

from flask_wtf.csrf import CsrfProtect

from config import DevelopmentConfig
from forms import LoginForm
from forms import CreateForm

from models import db as database
from models import User

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect()

def create_session(username, user_id):
	session['username'] = username
	session['id'] = user_id

def success_authentication(request, user):
	create_session(user.username, user.id)
	success_message = 'Bienvenido a la plataforma {}'.format(user.username)
	flash(success_message)
	return redirect(url_for('dashboard'))

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

@app.route('/user/new', methods = ['GET', 'POST'])
def user_new():
	create_form = CreateForm(request.form)
	if request.method == 'POST' and create_form.validate():
		username = create_form.username.data
		password = create_form.password.data
		email = create_form.email.data

		user = User(username, password, email)

		database.session.add(user)
		database.session.commit()
		return success_authentication(request,user)

	return render_template('user/new.html', form = create_form)

@app.route('/login', methods = ['GET','POST'])
def login():
	login_form = LoginForm(request.form)
	if request.method == 'POST' and login_form.validate():
		username = login_form.username.data
		password = login_form.password.data
		
		user = User.query.filter_by(username = username).first()
		if user is not None and user.verify_password(password):
			return success_authentication(request, user)
		else:
			error_message = 'Usuario o password incorrectos.'
			flash(error_message)

	return render_template('login.html', form = login_form)

@app.route('/logout', methods = ['GET'])
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/dashboard', methods = ['GET'])
def dashboard():
	username = session['username']
	is_authenticated = True
	return render_template('user/dashboard.html', username = username, is_authenticated = is_authenticated)

if __name__ == '__main__':
	csrf.init_app(app)
	database.init_app(app)

	with app.app_context():
		database.create_all()

	app.run()

