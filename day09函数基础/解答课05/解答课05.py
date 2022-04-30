# 1、 编写程序输出已知元组内7的倍数的数据和个位是7的数据，
# 已知元组b=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
# 思路：
# 1.循环遍历取出元组里的数据
# 2.进行判断（7的倍数的数据和个位是7的数据）
# 3.保存到一个列表里
# 4.输出保存的数据

# 创建一个空的列表
# a = []
# b=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
# for i in b:
#     print(i)
#     # 判断7的倍数
#     if i % 7 == 0:
#         # print(i)
#         a.append(i)     # 把元素添加到列表中
#     # 判断个位是7的数据
#     elif i % 10 == 7:
#         a.append(i)
# print(a)
#
# a = []
# b=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
# for i in b:
#     # print(i)
#     # 判断7的倍数
#     if i % 7 == 0 or i % 10 == 7:
#         a.append(i)
# print(a)
#
# while循环
# a = []
# b=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)
# i = 0
# while i < len(b):
#     # print(i)
#     if b[i] % 7 == 0 or b[i] % 10 == 7:
#         a.append(b[i])
#     i += 1
# print(a)
#
#
# # 2、创建字典dict1,然后存储名字、年龄、身高；并且依次的打印输出所有的key值和value值。
# # 1.定义一个字典存储名字、年龄、身高
# dict1 = {'name': '简单', 'age': 18, 'height': 180}
# # 通过key获取value
# # 通过循环遍历自字典
# for i in dict1:
#     # print(i)
#     print(i,dict1[i])
#
#
# # print(dict1.keys())   dict_keys(['name', 'age', 'height'])
# # print(dict1.items())    dict_items([('name', '简单'), ('age', 18), ('height', 180)])
#
# # 拆包（对序列进行拆包）
# # 再进行拆包时，有几个元素就要几个变量来接受，不能多也不能少
# a = 'qwre'
# a = [1,2,3,4]
# b,c,d,e = a
# print(b)
# print(c)
# print(d)
# print(e)
#
# for key,value in dict1.items():
#     print(key,value)
#
#
# # 3、自定义一个空字典，通过添加键值对的方式，实现字典key的值是1，2, 3, 4，5，value的值都是key值的2次方
# # 自定义一个空字典
# a = {}
# # 循环输出key的值  1-5
# for i in range(1,6):
#     # print(i)
#     # 通过key来进行添加键值对
#     a[i] = i ** 2
# print(a)
#
# a = {}
# i = 1
# while i <= 5:
#     # print(i)
#     a[str(i)] = i ** 2
#     i += 1
# print(a)
#
