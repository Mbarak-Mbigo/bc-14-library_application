# app/models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
	"""Create a Users table"""
	__tablename__ = 'users'

	userId = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	firstName = db.Column(db.String(60), index=True)
	lastName = db.Column(db.String(60), index=True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	isAdmin = db.Column(db.Boolean, default=False)
	fines = db.relationship('Fine', backref='User', lazy='dynamic')

	@property
	def password(self):
		# Prevent password from being accessed
		raise AttributeError('Password is not a readable attribute.')

	@password.setter
	def password(self, password):
		# Set password to be hashed
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		# check if password matches actual password4
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User: {}>'.format(self.username)

	# set up user_loader
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	class Role(db.Model):
		"""Create a role table"""
		
		__tablename__ = 'roles'

		id = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(60), unique=True)
		description = db.Column(db.String(200))
		users = db.relationship('User', backref='role', lazy='dynamic')

		def __repr__(self):
			return 'Role: {}'.format(self.name)

class Book(object):
	"""Create table Book"""
	__tablename__ = 'books'

	bookId = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(60))
	bkTitle = db.Column(db.String(30), unique=True)
	isbn = db.Column(db.String(20), unique=True)
	authors = db.Column(db.String(60))
	acquireddate = db.Column(db.DateTime)
	quantity = db.Column(db.Integer, default=1)
	isAvailable = db.Column(db.Boolean, default=True)
	isBorrowed = db.Column(db.Boolean, default=False)
	currentBorrower = db.Column(db.Integer, default=None)
	
		

	class Fine(db.Model):
		"""Create table Fine"""

		__tablename__ = 'fines'

		fineId = db.Column(db.Integer, primary_key=True)
		fineAmount = db.Column(db.Float)
		isPaid = db.Column(db.Boolean, default=False)
		user_id = db.Column(db.Integer, db.ForeignKey('users.userId'))




		
			
			

		
		
