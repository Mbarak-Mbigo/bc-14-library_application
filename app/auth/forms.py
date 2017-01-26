# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User

class RegistrationForm(FlaskForm):
	# Form for user to create new account
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('Username', validators=[DataRequired()])
	firstName = StringField('First Name', validators=[DataRequired()])
	lastName = StringField('Last Name', validators=[DataRequired()])
	password = PasswordField('Password', validators= [
										DataRequired(),
										EqualTo('confirm_password')
										])
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Register')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
	"""Form for users to"""
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')