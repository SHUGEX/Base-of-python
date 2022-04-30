# 面向对象的两个组成部分：类和对象
# 类：通过class定义的，组成部分：属性和方法(所有的对象所共有的)
# 属性： 分为类属性（共有的）和对象属性（私有的）
# 方法： 直接在类里面定义的方法就是对象方法（实例方法）
# 类方法：用装饰器@classmethod来标识其为类方法
# 静态方法：通过装饰器@staticmethod来标识其为静态方法

# 对象：通过类创建出来的
# 定义狗类
# class Dog(object):
#     tooth = 10              # 定义类属性
#     @classmethod            # 装饰器，添加其他的功能：让对象方法变成类方法
#     def info_print(cls):
#         print(1)
#
#     @classmethod
#     def info_print1(cls):       # cls表示类本身
#         # 在方法里面去使用类本身去调用方法时，可以直接使用cls
#         print(cls.tooth)
#
# wangcai = Dog()
# wangcai.info_print()            # 类方法
# Dog.info_print()
# Dog.info_print1()               # 10,用类调用类属性得到的属性值

# 结论：类方法是可以被类和对象一起访问的,而对象方法可以被对象访问，但是不能被类访问

# 静态方法：取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
# class Dog(object):
#     @staticmethod
#     def info_print():           # 小括号中没有self,也没有cls
#         print("这是一个静态方法！")
#
# wangcai = Dog()
# wangcai.info_print()
# Dog.info_print()                # 结论：静态方法是可以被类和对象一起访问的






