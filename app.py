from flask import Flask,request,session
from flask import render_template
from flask_bootstrap import Bootstrap
import time

from app import *
import json
import pymysql
from flask import request
import traceback
from flask import flash,session

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '123456'

# from model import app
@app.route('/machin',methods=['GET','POST'])
def machine_data():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='opcdata', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM rtdata"
    cur.execute(sql)
    u = cur.fetchmany(20)
    conn.close()
    jsondata = []
    for i in u:
        tem = {}
        tem['user_id'] = i[0]
        tem['tag_id'] = i[1]
        tem['tag_value'] = i[2]
        tem['tag_type'] = i[3]
        tem['tag_quality'] = i[4]
        tem['value_time'] = i[5]
        jsondata.append(tem)
    # print(jsondata)
    return json.dumps(jsondata)
    # return render_template('index.html',u=u)
    # return render_template('machine.html')

@app.route('/yonghuming',methods=['GET','POST'])
def yonghuming():
   jsondata = []
   tem = {}
   tem['username'] = session.get('username')
   jsondata.append(tem)
   return json.dumps(jsondata)

@app.route('/log0',endpoint='log0')
def log():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "select * from user where username=" + repr(request.args.get('username')) + " and password=" + repr(request.args.get('password'))
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(request.args.get('password'))
        if len(results) == 1:
            # flash('登录成功')
            username = request.args.get('username')
            session['username'] = username
            return render_template('index.html')
        else:
            flash('用户名或密码不正确')
            return render_template('index0.html')
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()

@app.route('/regist',endpoint='regist')
def regist():
    db = pymysql.connect("localhost", "root", "123456", "opcdata")
    cursor = db.cursor()
    sql = "insert into user(username,password,email,phone,cre_time) values" +\
          '('+repr(request.args.get('username'))+','+\
          repr(request.args.get('password'))+','+\
          repr(request.args.get('email'))+','+\
          repr(request.args.get('phone'))+','+\
          repr(str(time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time()))))+')'
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        return render_template('index0.html')
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
        flash('注册失败，该用户已存在')
        return render_template('index0.html')
    # 关闭数据库连接
    db.close()

# @app.route('/userinfo')
# def userinfo():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='opcdata')
#     cur = conn.cursor()
#     sql = "SELECT * FROM user"
#     cur.execute(sql)
#     u = cur.fetchall()
#     conn.close()
#     print(u)
#     return render_template('user.html',u=u)

# @app.before_request
# def before_user():
#     if 'username' in session:
#         return render_template('index.html')
#     else:
#         return render_template('index0.html')







@app.route('/')
def index0():
    return render_template('index0.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='opcdata')
    cur = conn.cursor()
    sql = "SELECT * FROM user"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    print(u)
    return render_template('user.html',u=u)

@app.route('/user_form')
def user_form():
    return render_template('user_form.html')

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
