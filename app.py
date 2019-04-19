from flask import Flask,request,session
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'

from model import app
@app.route('/')
def index0():
    return render_template('index0.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/machine')
def machine_show():
    return render_template('machine.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/log')
def log():
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug=True)
