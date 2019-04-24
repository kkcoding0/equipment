from flask import Flask,request,session
from flask import render_template
from flask_bootstrap import Bootstrap
import pymysql
from flask import redirect,url_for
# from model import before_user

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'

from model import app
@app.route('/')
def index0():
    return render_template('index0.html')

@app.route('/index')
def index():
    # before_user()
    return render_template('index.html')

@app.route('/user')
def user():
    # before_user()
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='opcdata')
    cur = conn.cursor()
    sql = "SELECT * FROM user"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    print(u)
    return render_template('user.html', u=u)

@app.route('/user_form')
def user_form():
    # before_user()
    return render_template('user_form.html')

@app.route('/machine')
def machine_show():
    # before_user()
    return render_template('machine.html')

@app.route('/service')
def service():
    # before_user()
    return render_template('service.html')

@app.route('/log')
def log():
    # before_user()
    return render_template('log.html')

@app.route('/index/baidu')
def baidu():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)
