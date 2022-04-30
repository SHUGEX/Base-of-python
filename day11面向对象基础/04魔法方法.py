# 1. __init__():初始化对象，设置初始化的值
# class Washer():
#     def __init__(self, width, height, name):           # self保存对象
# #         # 添加对象属性：对象名.属性名
#         self.width = width
#         self.height = height
#         self.name = name
# #
# #     # 定义方法，获取对象属性
#     def print_info(self):
#         print(f"{self.name}洗衣机的宽度是{self.width},高度是{self.height}")
# #
# # # 创建对象的位置给对象属性的属性值
# a = Washer(20, 40, "a")
# b = Washer(30, 50, "b")
# a.print_info()
# b.print_info()
#
# # 2. __str__():会改变对象的打印效果，都会有return
# class Wahser():
#     def __str__(self):
#         return "对类或者对象的说明"
#     def __init__(self):
#         self.name = "a"
#
# a = Wahser()
# print(a)            # 我是a洗衣机
#
# # 3. __del__() :释放内存，调用del之后，所有的属性和方法都会自动删除
# class Wahser():
#     def __init__(self):
#         self.name = "a"
#
#     def __del__(self):
#         print("对象内存已释放！")
#
#
# a = Wahser()
# print(a)
#











