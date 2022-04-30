# 练习题
# 定义一个Point类为父类，在父类中分别有x,y,z,h四个属性，用来传入未知整数，
# 再定义一个Line类为子类，继承Point类，并在Line类中定义getPoint方法，
# getPoint方法用于计算x-y的绝对值和z-h的绝对值相乘的结果，
# 最后通过子类创建对象传入实参检测是否继承成功
# class Point(object):
#     def __init__(self,x,y,z,h):     # 初始化方法
#         self.x = x
#         self.y = y
#         self.z = z
#         self.h = h
#
#
# class Line(Point):
#     def getPoint(self):
#         # num = abs((self.x - self.y) * (self.z - self.h))
#         num = abs(self.x - self.y) * abs(self.z - self.h)
#         print(num)
#
#
# a = Line(1,2,3,4)          # 在实例化的时候就行传入
# a.getPoint()

# abs(变量或者是表达式（数）):返回绝对值
# print(abs(-5))
# print(abs(5))


# 需求：实现老王开车去北京
# 对象有：人
#         交通工具
#         地点
# 1.定义人的对象，初始化人的属性: 名字
# 2.定义人使用交通工具的方法：drive()
# 3.定义交通工具的对象，初始化交通工具的属性:名字
# 4.定义交通工具的启动方法：driving()
# 5.定义地点的对象，初始化地点的属性：地址名
# 6.创建实例化人对象，交通对象的对象，地点对象，实现人开车到达某个地
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#
#     def drive(self,a,b):    # a,b接收的是对象
#         a.driving()
#         print(f'{self.name}开{a.name}去{b.name}')
#
#
# class Car(object):
#     def __init__(self,name):
#         self.name = name
#
#     def driving(self):
#         print('启动')
#
# class Address(object):
#     def __init__(self,name):
#         self.name = name
#
#
# # 实现老王开车去北京
# p = Person('老王')
# tool = Car('bmw')
# address = Address('北京')
#
# p.drive(tool,address)