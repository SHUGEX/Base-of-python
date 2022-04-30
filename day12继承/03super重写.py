# # 1. 定义师父类和学校类，定义属性和方法
# class Master(object):           # 父类
#     def __init__(self):
#         self.jishu = "师父的摊煎饼果子配方"
#
#     def make_cake(self):
#         print(f"使用{self.jishu}摊煎饼果子")
#
# class School(object):           # 父类
#     def __init__(self):
#         self.jishu = "学校的摊煎饼果子配方"
#
#     def make_cake(self):
#         print(f"使用{self.jishu}摊煎饼果子")
#
# # 2. 定义徒弟类，子类
# class Prentice(Master, School):
#     # 定义自己的属性和方法
#     def __init__(self):
#         self.jishu = "自创的摊煎饼果子配方"
#     def make_cake(self):
#         print(f"使用{self.jishu}摊煎饼果子")
#
#
# # 3. 实例化对象，需要徒弟继承师父和学校的技术
# tom = Prentice()
# print(tom.jishu)
# tom.make_cake()         # 继承到的是自创的，同名的情况之下，使用的是自己的属性和方法

# super()重写
# 1. 定义师父类和学校类，定义属性和方法
class Master(object):  # 父类
    def __init__(self):
        self.jishu = "师父的摊煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.jishu}摊煎饼果子")


class School(Master):  # 父类
    def __init__(self):
        self.jishu = "学校的摊煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.jishu}摊煎饼果子")
        # 用super()重写语法：super().方法名()
        super().__init__()          # 父类的属性
        super().make_cake()         # 父类的方法


# 2. 定义徒弟类，子类
class Prentice(School):
    # 定义自己的属性和方法
    def __init__(self):
        self.jishu = "自创的摊煎饼果子配方"

    def make_cake(self):
        print(f"使用{self.jishu}摊煎饼果子")

    # 在子类中调用父类的同名属性和方法，用super()重写语法：super().方法名()
    def info_print(self):
        super().__init__()          # 获取父类中的属性值
        super().make_cake()


# 3. 实例化对象，需要徒弟继承师父和学校的技术
tom = Prentice()
print(tom.jishu)
tom.make_cake()  # 继承到的是自创的，同名的情况之下，使用的是自己的属性和方法
tom.info_print()

# 通过__mro__可以去查看类之间的继承关系
# print(Prentice.__mro__)

# 总结：super重写指的是在子类中调用和父类同名的方法的，同名时只能调用子类的属性和方法
# 只适用于单继承
