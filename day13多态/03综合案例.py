# “需求”：将小于房子剩余面积的家具摆放到房子中
"""
1. 房子类
属性：a. 房子总面积，b. 房子剩余面积， c. 房子地理位置， d. 家具列表
方法：容纳家具

2. 家具类
属性：a. 名称，b.家具面积
"""
# 定义房子类
# class Home(object):
#     def __init__(self, area, address):
#         # 房子总面积
#         self.area = area
#         # 房子剩余面积
#         self.free_area = area
#         # 房子地理位置
#         self.address = address
#         # 家具列表
#         self.list1 = []
#     # 定义房子添加家具方法
#     def add_Furniture(self, jiaju):            # self指的是changsha，jiaju指的是沙发
#         # 判断家具的面积 < 房子的剩余面积，如果成立可以添加家具，否则提示用户
#         if jiaju.area <= self.free_area:
#             # 添加家具
#             self.list1.append(jiaju.name)
#             self.free_area -= jiaju.area
#         else:
#             print(f"{jiaju.name}太大了，剩余面积不足，无法容纳！")
#     def __str__(self):                  # 为了把房子信息进行显示
#         return f"房子的地理位置在{self.address}, 总面积是{self.area},剩余面积{self.free_area}, 家具列表有{self.list1}"
#
# # 定义家具类
# class Furniture(object):
#     # 定义属性
#     def __init__(self, area, name):
#         # 家具面积
#         self.area = area
#         # 家具名称
#         self.name = name
#
#
# changsha = Home(200, "长沙")
# sofa = Furniture(3, "沙发")
# bed = Furniture(4, "双人床")
# ball = Furniture(300, "篮球场")
# changsha.add_Furniture(sofa)
# changsha.add_Furniture(bed)
# changsha.add_Furniture(ball)
# print(changsha)
#
#
#
#








