#demo run before final structure
import os
rom flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from app.model.model import Model

#model object
appmodel = Model()

app = Flask(__name__)

@app.route('/')
def initialize():
	return render_template('signin.html')

if __name__ == '__main__':
	app.run(port=8000)
