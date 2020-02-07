class User_mod():
    def __init__(self, userInfo):
        self.itcode = userInfo[0][0]
        self.username = userInfo[0][1]
        self.password = userInfo[0][2]
        self.truename = userInfo[0][3]
        # 业务域
        # 0 表示管理员看的所有业务域，其他用户业务域从1开始
        self.dcode = userInfo[0][4]
        self.dname = userInfo[0][5]
        # 角色
        # 1 管理员 2 开发 3 产品经理 4 业务经理
        self.rcode = userInfo[0][6]
        self.rname = userInfo[0][7]

    def todict(self):
        return self.__dict__

    # 下面这4个方法是flask_login需要的4个验证方式
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id