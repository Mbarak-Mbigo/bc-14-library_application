# Model Module: handles all data creation and retrieval
from flask.ext.sqlalchemy import SQLAlchemy
class Model(object):
	"""docstring for Model"""
	def __init__(self):
		super(Model, self).__init__()
		self.conn=None


class dbcon(object):
	#Handles connection to the database from the appliction
	#assumes database exists
	def __init__(self, host='localhost', db='testdb', username='dbuser', password='pwduser'):
		self.host = 'host='+host
		self.db = 'dbname='+db
		self.username = 'user='+username
		self.passwd = 'password'+password

	def createconnection():
		pass
		
		