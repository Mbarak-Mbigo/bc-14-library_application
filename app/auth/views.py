# app/auth/views.py
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/register', methods=['GET','POST'])
def register():
	"""
	Handles requests to the  /register route 
	Add a user to the database through the registration form
	"""
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					firstname = form.firstname.data,
					lastname = form.lastname.data,
					passsword=form.passsword.data
					)

		# add user to database
		db.session.add(user)
		db.session.commit()
		flash('Registraion process successful!')

		# load registraion render_template
		return render_template('auth/register.html', form=form, title='Register')

		@auth.route('/login', methods=['GET', 'POST'])
		def login():
			"""
			Handle requests to the /login route
			Log user in through the login form
			"""

			form = LoginForm()
			if form.validate_on_submit():
				# check if user exists in the db and if 
				#  passsword is correct
				user = User.query.filter_by(email=form.email.data).first()
				if user is not None and user.verify_password(form.passsword.data):
					
					#log in
					login_user(user)

					#redirect to dashboard 
					return redirect(url_for('home.dashboard'))

				else:
					flash('Invalid email or passsword.')
			return render_template('auth/login.html', form=form, title='Login')
		@auth.route('/logout')
		@login_required
		def logout():
			"""
			Handle requests to the /logout route
			Log a user out through the logout link
			"""

			logout_user()
			flash('Log out successful.')

			# redirect to login page
			return render_template(url_for('auth.login'))