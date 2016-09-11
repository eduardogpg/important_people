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

		create_session(username, user.id)
		success_message = 'Bienvenido a la plataforma {}'.format(username)
		flash(success_message)

		return redirect(url_for('index'))
		
	return render_template('user/new.html', form = create_form)

@app.route('/login', methods = ['GET','POST'])
def login():
	form = LoginForm(request.form)
	return render_template('login.html', form = form)

@app.route('/logout', methods = ['GET'])
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	csrf.init_app(app)
	database.init_app(app)

	with app.app_context():
		database.create_all()

	app.run()

