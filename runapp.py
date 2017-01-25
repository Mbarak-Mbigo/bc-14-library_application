from flask import Flask, request, render_template
app = Flask(__name__, template_folder='app/templates',static_folder='app/static')

@app.route('/')
def index():
    return render_template('signin.html')


if '__main__' == __name__:
	app.run()