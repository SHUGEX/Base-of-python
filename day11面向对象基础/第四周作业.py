# 1. 定义一个Person类，使用Person类，创建一个tom对象后，在类外面添加company属性，值是"阿里巴巴"；
# 创建一个jerry对象，添加company属性，值是"万达集团"


# class Person():
#     pass
#
#
# tom = Person()
# tom.company = "阿里巴巴"
# jerry = Person()
# jerry.company = "万达集团"
# 2. 定义一个水果类，然后通过水果类，然后分别创建苹果对象、橘子对象、西瓜对象，并在类外面分别添加上颜色属性，
# 最后在类里面通过方法获取颜色属性（注意：每个对象获取的颜色属性都是不同的）


# class Fruit():
#     pass
#
#
# apple = Fruit()
# apple.color = 'red'
# orange = Fruit()
# orange.color = "yellow"
# watermelon = Fruit()
# watermelon.color = "green"
# print(apple.color)
# print(orange.color)
# print(watermelon.color)
# # 3. 定义一个汽车类，并在类中定义一个move方法，然后分别创建BMW_X9、AUDI_A9对象，
# # 并在类里面添加颜色、马力、型号等属性，然后通过调用move方法方法分别打印出属性值、（使用__init__方法完成属性赋值）
# class Car():
#     def __init__(self, color, horsepower, model):
#         self.color = color
#         self.horsepower = horsepower
#         self.model = model
#
#     def move(self):
#         print(f"颜色{self.color}、马力{self.horsepower}、型号{self.model}")
#
#
# BMW_X9 = Car("write", "10", 'a')
# AUDI_A9 = Car("blue", "8", 'b')
#
#
# BMW_X9.move()
# AUDI_A9.move()