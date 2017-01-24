#demo run before final structure
from flask import Flask
app = Flask(__name__)

@app.route('/')
def initialize():
	return "Root of M-Library Application"

if __name__ == '__main__':
	app.run()