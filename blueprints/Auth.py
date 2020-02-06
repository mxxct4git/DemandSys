from flask import Blueprint, flash, request, redirect, render_template

auth_bp = Blueprint("auth_bp",__name__,url_prefix="/log_bp")

@auth_bp.route('/mylogin', methods=['GET', 'POST'])
def mylogin():
    if request.method == 'POST':
        print("登录用户名")
        print(request.form["username"])
        print(request.form["password"])
        return render_template('index.html')
    return render_template("test.html")
    # form = Login_Form()
    # if form.validate_on_submit():
    #     user = Users.query.filter_by(name=form.name.data).first()
    #     if user is not None and user.pwd == form.pwd.data:
    #         login_user(user)
    #         flash('登录成功')
    #         return render_template('ok.html', name=form.name.data)
    #     else:
    #         flash('用户或密码错误')
    #         return render_template('login.html', form=form)


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
