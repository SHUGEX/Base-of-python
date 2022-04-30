# 2、人的体力
# 要求：
# 定义人（Person）类
# 在类中默认体力（power）100
# 当进行学习操作时（study）体力在默认体力的基础上减30
# 当进行吃饭操作时（eat）体力在默认体力的基础上加20
# 当进行练习操作时（training）体力在默认体力的基础上减25
# 当进行睡觉操作时（sleep）体力在默认体力的基础上加50

# class Person(object):
#     def __init__(self):     # 初始化方法，对象的属性   不需要调用，会自动执行
#         self.power = 100
#         # print(123)
#
#     def study(self):        # 对象的方法
#         if self.power > 30:
#             self.power -= 30
#             print('学习消耗30')
#             # print(self.power)
#
#     def training(self):
#         if self.power > 25:
#             self.power -= 25
#             print("练习消耗25")
#
#     def est(self):
#         self.power += 20
#         print("吃饭恢复20")
#
#     def sleep(self):
#         self.power += 50
#         print("睡觉恢复50")
#
#     def __str__(self):
#         if self.power > 100:
#             self.power = 100
#         return f"体力是{self.power}"      # 返回的一定是字符串







# p = Person()
# # p.study()
# # p.est()
# print(p)
# print(p.power)










