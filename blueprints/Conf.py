import json

# loads()：将json数据转化成dict数据
# dumps()：将dict数据转化成json数据
# load()：读取json文件数据，转成dict数据
# dump()：将dict数据转化成json数据后写入json文件


def getDbConf():
    f = open("./config/dbconf.json", encoding="utf-8") # 设置以utf-8解码模式读取文件，encoding参数必须设置,否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    settings = json.load(f)

    host = settings[settings["env"]]["host"]
    port = settings[settings["env"]]["port"]
    user = settings[settings["env"]]["user"]
    password = settings[settings["env"]]["password"]
    db = settings[settings["env"]]["db"]
    charset = settings[settings["env"]]["charset"]
    return host, port, user, password, db, charset


