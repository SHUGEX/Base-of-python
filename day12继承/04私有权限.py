class Master(object):
    def __init__(self):
        # 共有权限
        # self.money = 200
        # 私有属性
        self.__money = 200

    def __info_print(self):
        print(1)
        return self.__money

    def info1(self):
        return self.__info_print()

class Prentice(Master):
    pass

tom = Prentice()
# a = tom.info_print()
# print(a)                        # 通过获取返回值拿到私有属性
# print(tom.money)            # 报错，权限限制
tom.info1()             # 1







