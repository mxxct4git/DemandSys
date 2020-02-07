# 认证类模块蓝图
# 包括登录、注册功能

from flask import Blueprint, current_app, flash, request, redirect, render_template
from blueprints import DbLinks as db
from models.User import User_mod

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/log_bp")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        conn = db.getConn()
        sql = "select u.itcode, u.username, u.password, u.truename, " \
              "group_concat(udr.domain_code) as dcode, group_concat(d.name) as dname, " \
              "group_concat(udr.role_code) as rcode, group_concat(r.name) as rname " \
              "from (select * from t_user u where username = '" + username + "' and password = '" + password + "')u " \
                                                                                                               "left join t_user_domain_role udr on u.id = udr.user_id " \
                                                                                                               "left join t_domain d on udr.domain_code = d.code " \
                                                                                                               "left join t_role r on udr.role_code = r.code " \
                                                                                                               "group by u.itcode, u.username, u.password, u.truename"
        res = db.getSelRes(conn, sql)
        conn.close()
        if len(res) > 0:
            curUser = User_mod(res)
            # print(curUser.todict())
            # {'itcode': '10077110', 'username': 'zjh', 'password': '123', 'truename': '张嘉昊', 'dcode': '2,3,12', 'dname': '物联网,客服,GIS', 'rcode': '2,2,3', 'rname': '开发,开发,产品经理'}
            # print(curUser.truename)

            # 保存当前用户为全局变量
            current_app.curUser = curUser

            dcArr = curUser.dcode.split(",")
            dnArr = curUser.dname.split(",")
            rcArr = curUser.rcode.split(",")
            rnArr = curUser.rname.split(",")
            curDomainRole = []
            tmp = {}
            for i in range(0, len(dcArr)):
                tmp["dcode"] = dcArr[i]
                tmp["dname"] = dnArr[i]
                tmp["rcode"] = rcArr[i]
                tmp["rname"] = rnArr[i]
                curDomainRole.append(tmp.copy())
                tmp.clear()

            # 保存当前用户对应的业务域&角色信息为全局变量
            current_app.curDomainRole = curDomainRole

            print("登录成功")
            return render_template('index.html', curUser=curUser)
        else:
            print("登录失败")
            return render_template("login.html", warningContent="用户名或密码错误，请重新输入")

# 用户登出
# @log.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('你已退出登录')
#     return redirect(url_for('blog.index'))
#
#
# @log.route('/register', methods=['GET', 'POST'])
# def register():
#     form = Register_Form()
#     if form.validate_on_submit():
#         user = Users(name=form.name.data, pwd=form.pwd.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('注册成功')
#         return redirect(url_for('blog.index'))
#     return render_template('register.html', form=form)
