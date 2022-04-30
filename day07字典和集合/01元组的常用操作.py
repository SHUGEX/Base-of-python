# “元组的格式”:（数据1,数据2,数据3,数据4.….…）
# 1. 定义有数据的元组,检测数据类型：type(数据)
# t1 = ("maiya", "tom")
# print(type(t1))                 # tuple
# list1 = ["maiya", "tom"]
# print(type(list1))              # list

# 2. 定义有一个数据的元组,注意：需要在唯一的这个数据后面加上逗号
# t2 = (10)                   # int
# t3 = (10,)                   # tuple
# print(type(t3))

# 3. 元组的常用操作---->元组中的数据是不能修改，查找
# 查找：1. 按下标查找数据,序列名[下标]
# t1 = ("aa", "dd", "cc", "dd")
# # print(t1[2])            # cc
#
# # 2. 按函数查找:index()   count()   len()
# print(t1.index("dd"))               # 1,返回下标，不存在报错
# print(t1.count("dd"))                   # 2,返回出现的次数
# print(len(t1))                          # 4，返回序列中的数据的个数





