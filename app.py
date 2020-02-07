from flask import Flask, current_app, render_template, redirect, request
from blueprints.Auth import auth_bp

app = Flask(__name__)

# 注册认证类模块蓝图，包括登录、注册功能
app.register_blueprint(auth_bp)

@app.route('/')
# @app.route('/toLog')
def toLog():
    return render_template("login.html")


# 针对iframe方式来跳转
# 根据传递的参数不同，跳转到对应的页面
@app.route('/iframe/<name>', methods=['GET'])
def iframeRouter(name):
    return render_template(name, curUser=current_app.curUser, curDomainRole=current_app.curDomainRole)


if __name__ == '__main__':
    app.run(debug=True)
