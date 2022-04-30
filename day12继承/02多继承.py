# 多继承的第一种情况（简单,C继承的A和B当中的方法是不同名）
# class A(object):
#     def test1(self):
#         print("test1")
#
# class B(object):
#     def test2(self):
#         print("test2")
#
# class C(A,B):          # C(A,B)表示C这个类继承了A和B两个类
#     pass
#
# c = C()
# c.test1()
# c.test2()

# 复杂：所继承的父类中有同名的方法
# 1. 定义师父类和学校类，定义属性和方法
class Master(object):
    def __init__(self):
        self.jishu = "师父的摊煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.jishu}摊煎饼果子")

class School(object):
    def __init__(self):
        self.jishu = "学校的摊煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.jishu}摊煎饼果子")

# 2. 定义徒弟类
class Prentice(Master, School):         # 父类名有优先继承，谁在第一个就优先继承
    pass

# 3. 实例化对象，需要徒弟继承师父和学校的技术
tom = Prentice()
print(tom.jishu)
tom.make_cake()         # 继承到的是师父的









