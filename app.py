from flask import Flask, render_template, redirect, request
from blueprints.Auth import auth_bp

app = Flask(__name__)

# 注册"登录注册"模块蓝图
app.register_blueprint(auth_bp)

@app.route('/')
# @app.route('/toLog')
def toLog():
    return render_template("login.html")


# 针对iframe方式来跳转
# 根据传递的参数不同，跳转到对应的页面
@app.route('/iframe/<name>', methods=['GET'])
def iframeRouter(name):
    return render_template(name)


if __name__ == '__main__':
    app.run(debug=True)
