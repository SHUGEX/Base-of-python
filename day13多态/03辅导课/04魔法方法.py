# 特点:不需要调用,会自动的执行
# class A(object):
#     def __init__(self):     # 初始化方法
#         print('123')
#
#
# a = A()

# __init__:初始化方法
# class A(object):
#     def __init__(self):     # 初始化方法
#         self.name = '张三'
#
#     def test(self):
#         self.name = "李四"
#         return self.name
#
#
# a = A()
# print(a.name)
# print(a.test())

# __del__:析构方法
# 做资源回收的
# class A(object):
#     def __init__(self):     # 初始化方法
#         self.name = '张三'
#
#     def __del__(self):
#         print('我是del方法')
#
#
# a = A()
# del a
# print(123)
# 当一个对象被删除或者是被销毁的时候,python的解释器会默认的使用__del__
