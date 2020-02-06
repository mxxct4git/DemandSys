from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from blueprints.Auth import auth_bp

app = Flask(__name__)

# 注册"登录注册"模块蓝图
app.register_blueprint(auth_bp)

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost：3306/demands"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/charts')
def charts():
    return render_template("charts.html")


if __name__ == '__main__':
    app.run(debug=True)
