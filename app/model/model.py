# Model Module: handles all data creation and retrieval
class Model(object):
	"""docstring for Model"""
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg


class dbcon(object):
	#Handles connection to the database from the appliction
	#assumes database exists
	def __init__(self, host='localhost', db='appdb', username='appuser', password='mypassword'):
		self.host = host
		self.db = db
		self.username = username
		self.passwd = password

	def createconnection():
		pass