import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if '__main__' == __name__:
	app.run()


