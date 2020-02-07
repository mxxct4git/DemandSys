class User_mod():
    def __init__(self):
        self.id = None
        self.itcode = None
        self.username = None
        self.password = None
        self.truename = None
        self.domain = None
        self.role = None
        self.permission = None

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