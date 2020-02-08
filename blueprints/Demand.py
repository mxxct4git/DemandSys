# 需求类模块蓝图
# 包括增改查功能
import json
import datetime

from flask import Blueprint, current_app, flash, request, redirect, render_template
from blueprints import DbLinks as db
from models.Demand import Demand_mod

demand_bp = Blueprint("demand_bp", __name__, url_prefix="/demand_bp")


@demand_bp.route('/add', methods=['GET', 'POST'])
def add():
    print("新建一个需求")
    print(request.form)
    # 拼接多个开发人员
    dev_users = "&".join(request.form.getlist("dev_userid"))
    conn = db.getConn()
    params = "'" + str(request.form["demand_name"]) + "', '" + str(request.form["demand_code"]) + "', '" + \
             str(request.form["domain_code"]) + "', '" + str(current_app.curUser.id) + "', '" + \
             str(request.form["model_name"]) + "', '" + str(request.form["status_code"]) + "', '" + \
             str(datetime.datetime.now())[:16] + "', '" + str(dev_users) + "', '" + \
             str(request.form["confluence"]) + "', '" + str(request.form["description"])  + "', " + "'1'"
    sql = "insert into t_demand(demand_name, demand_code, domain_code, apply_userid, model_name, status_code, modify_time, dev_users, confluence, description, modfiy_code) values(" + params +")"

    print(params)
    print(sql)

    db.insert(conn, sql)
    conn.close()
    return json.dumps({'msg': '新建需求成功'})
