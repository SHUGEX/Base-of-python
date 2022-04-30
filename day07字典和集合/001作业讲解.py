# 1、将字符串 s = "alex"转换为元组。
# tuple():将数据类型转变为元组
# 元组的格式：(数据1,数据2.....)
# 列表的格式：[数据1,数据2.....]
# s = "alex"
# print(tuple(s))
# print(list(s))
# print(dict(s))      # 不能转变为字典
# print(set(s))       # 无序的

# 2、自定义一个列表，并遍历出列表中的元素。
# list1 = ["a", "b", "c", "d", "f"]
# # for 变量 in 序列：
# # 方法一
# for i in range(len(list1)):
#     print(list1[i])
#
# # 方法二
# for i in list1:
#     print(i,end=' ')
#
# print(len(list1))
# # 使用while循环
# i = 0       # 下标的初始值为0
# while i < len(list1):
#     print(list1[i])
#     i += 1
# # 3、 比较两个列表中的元素，找出不相同的元素并保存到列表L3中,已知下方列表L1和L2:
# L1 = ["Sun", "Mon","Tue", "Wed", "Thu", "Fri", "Sat"]
# L2 = ["Sun", "Mon", "Tue", "Tue", "Thu", "Sat", "AD"]
# L3 = []
# # 思路
# # 首先遍历L1里面的元素，判断每一个元素在不在L2，不在就添加到L3
# # 首先遍历L2里面的元素，判断每一个元素在不在L1，不在就添加到L3
# for i in L1:
#     # print(i)
#     if i not in L2:
#         L3.append(i)
#
# for i in L2:
#     if i not in L1:
#         L3.append(i)
# print(L3)







