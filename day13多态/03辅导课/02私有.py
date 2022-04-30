# class A(object):
#     __money = 100
#
#     def __test(self):
#         print('我是私有方法')
#
#     def test2(self):
#         print(self.__money)
#         self.__test()
#
#
# a = A()
# # print(a.__money)
# # a.__test()
# a.test2()


# 有继承关系的私有
# class A(object):
#     __money = 100
#
#     def __test(self):
#         print('我是私有方法')
#
#     def test2(self):
#         print(self.__money)
#         self.__test()
#
#
# class B(A):
#     pass
#
# b = B()
# # print(b.__money)
# # b.__test()
# b.test2()
# 私有属性不能被继承