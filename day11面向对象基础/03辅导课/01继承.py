
# 单继承：
# 一个子类继承一个父类，拥有父类的属性方法
# 格式：class 类名(父类名)
# class A(object):
#     money = 200
#
#     def test(self):
#         print('赚钱的方法')
#
#
# class B(A):
#     pass
#
#
# b = B()
# print(b.money)
# b.test()
# #
#
# 多继承：
# 一个子类继承多个父类，拥有所有父类的属性方法
# 格式：class 类名(父类1，父类2...)
# 简单的多继承：父类中的方法不同名
# class F(object):
#     money = 100
#
#     def test(self):
#         print('赚钱养家')
#
#
# class M(object):
#     money2 = 200
#
#     def test2(self):
#         print('貌美如花')
#
#
# class S(F,M):
#     pass
#
#
# son = S()
# print(son.money)
# print(son.money2)
# son.test()
# son.test2()
# #
#
# class F(object):
#     money = 100
#
#     def test(self):
#         print('赚钱养家')
#
#
# class M(object):
#     money = 200
#
#     def test(self):
#         print('貌美如花')
#
#
# class S(M,F):
#     pass
#     def test(self):
#         print('我是son')
#
#
# son = S()
# print(son.money)
# son.test()
# # 父类中的属性和方法出现同名的情况,谁先继承就调用谁的方法和属性
# print(S.__mro__)









