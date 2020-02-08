class Demand_mod():
    def __init__(self, demandInfo):
        # 需求名称、事件号
        self.demand_name = demandInfo[0][0]
        self.demand_code = demandInfo[0][1]
        # 业务域
        self.dcode = demandInfo[0][2]
        self.dname = demandInfo[0][3]
        # 申请人
        self.apply_userid = demandInfo[0][4]
        self.apply_username = demandInfo[0][5]
        # 模型名称
        self.model_name = demandInfo[0][6]
        # 状态编码、状态名称
        self.status_code = demandInfo[0][7]
        self.status_name = demandInfo[0][8]
        # 当前操作时间
        self.modify_time = demandInfo[0][9]
        # 开发人员
        self.dev_users = demandInfo[0][10]
        # 文档地址
        self.confluence = demandInfo[0][11]
        # 附加描述
        self.description = demandInfo[0][12]
        # 当前操作编码 1新增 2修改
        self.modfiy_code = demandInfo[0][13]

    def todict(self):
        return self.__dict__
