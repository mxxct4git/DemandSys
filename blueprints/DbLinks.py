from blueprints import Conf
import pymysql


def getConn():
    host, port, user, password, db, charset = Conf.getDbConf()
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
    return conn

def getSelRes(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    res = cur.fetchall()
    return res