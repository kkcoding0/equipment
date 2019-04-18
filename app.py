from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/machine')
def machine():
    return render_template('machine.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/log')
def log():
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug=True)
