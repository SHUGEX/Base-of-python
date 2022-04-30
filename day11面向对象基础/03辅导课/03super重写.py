# 重写:在单继承的前提下,子类中定义一个和父类一样的方法
# class A(object):
#     def test(self):
#         print('赚钱')
#
#
# class B(A):
#     def test(self):
#         print('赚大钱')
#
#
# b = B()
# b.test()

# super:作用:对父类的方法进行扩展
# # 语法super().父类中的方法名
# class A(object):
#     def test(self):
#         print('赚钱')
#
#
# class B(A):
#     def test(self):
#         super().test()      # 调用父类中的方法
#         print('赚大钱')
#
#
# b = B()
# b.test()
# 注意:只能是单继承