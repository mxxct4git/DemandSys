from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from blueprints.Auth import auth_bp

app = Flask(__name__)

# 注册"登录注册"模块蓝图
app.register_blueprint(auth_bp)

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
