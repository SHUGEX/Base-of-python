# 多态：一类事物的多种形态，一个抽象的类有多个子类，
# 注意：多态依赖于继承

# class Animal(object):
#     pass
#
#
# class Cat(Animal):
#     pass
#
#
# class Dog(Animal):
#     pass

# 多态性:不同的对象调用同一个方法，实现不同的效果
# class Animal(object):
#     pass
#
#
# class Cat(Animal):
#     def bark(self):
#         print("喵喵叫")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("汪汪叫")
#
#
# a = Cat()
# b = Dog()
#
#
# # a.bark()
# # b.bark()
#
# # 定义一个接口
# def func(obj):
#     obj.bark()
#
#
# func(a)
# func(b)