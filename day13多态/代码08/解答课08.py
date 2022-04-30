# 类和对象
# 类是一个抽象的概念，一个大的概念
# 对象是具体的,实实在在存在的
# 总结:类是对象的抽象,对象是类的具体化
# 定义类
# class 类名(object):     # 类名符合大驼峰式命名
#     属性,方法


# 创建对象:通过类来创建对象
# 对象名 = 类名()


# 1. 定义一个Person类，使用Person类，
# 创建一个tom对象后，在类外面添加company属性，值是"阿里巴巴"；
# 创建一个jerry对象，添加company属性，值是"万达集团"
# 定义一个类
# class Person(object):
#     pass                # 占位
#
#
# # tom对象
# tom = Person()
# # 给对象添加属性: 对象名.属性名 = 属性值
# tom.company = '阿里巴巴'
# # 获取属性:对象名.属性名
# print(tom.company)
#
# # jerry对象
# jerry = Person()
# jerry.company = '万达集团'
# print(jerry.company)

# 2. 定义一个水果类，然后通过水果类，
# 然后分别创建苹果对象、橘子对象、西瓜对象，并在类外面分别添加上颜色属性，
# 最后在类里面通过方法获取颜色属性（注意：每个对象获取的颜色属性都是不同的）
# class Fruits(object):
#     def test(self):         # 用来接收对象的
#         print(f'苹果的颜色是{self.color}')
#
#
# a = Fruits()
# a.color = 'red'
# # 调用类里面的方法
# a.test()


# class Fruits(object):
#     def test(self,name):  # 用来接收对象的
#         print(f'{name}的颜色是{self.color}')
#
#
# a = Fruits()
# a.color = 'red'
# # 调用类里面的方法
# a.test('苹果')
#
# b = Fruits()
# b.color = '黄色'
# # 调用类里面的方法
# b.test('橘子')
#
#
# c = Fruits()
# c.color = '绿色'
# # 调用类里面的方法
# c.test('西瓜')


# 3. 定义一个汽车类，并在类中定义一个move方法，
# 然后分别创建BMW_X9、AUDI_A9对象，
# 并在类里面添加颜色、马力、型号等属性，
# 然后通过调用move方法方法分别打印出属性值、（使用__init__方法完成属性赋值）
# # 定义类
# class Car(object):
#     def __init__(self,name, color, mali, type):     # 初始化方法
#         self.name = name
#         self.color = color
#         self.mali = mali
#         self.type = type
#
#     def move(self):
#         print(f'汽车是{self.name}颜色是{self.color},马力是{self.mali},类型是{self.type}')
#
#
# BMW_X9 = Car('baoma','黑色','100','720')
# BMW_X9.move()

# AUDI_A9 = Car('白色','200','a4')
# AUDI_A9.move()






