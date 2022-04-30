# 字符串不可变
# a = 'asdasd'
# a.replace("a",'#')
# print(a)
#
# # 集合
# # {数据1，数据2，....}
# # 1.集合是无序的，里面的元素是唯一的
# # 2.可以用于元组或者列表去重
# # 3.集合不能有可变元素
# a = {}          # 定义字典
# print(type(a))
#
# # 定义集合
# a = set()       # 定义集合
# print(type(a))
#
# # 集合的无序性,去重
# a = set('123123')
# print(a)
#
# # 集合里面不能有可变的数据
# a = {1,2,3,4,'asd',(1,2,3)}
# # print(type(a))
# print(a)
#
#
# # 增加
# # add(数据):数据不能是序列
# a = {1,2}
# a.add(1)
# print(a)
#
# # update:添加序列
# a = {1,2}
# a.update('asda')       # 逐一的添加
# print(a)
#
# # 删除
# # remove
# a = {1, 2, 3, 4, 5}
# a.remove(2)     # 括号里面是数据
# print(a)
#
# # pop随机的删除一个数据,看起来默认的删除的是第一个
# a = {1, 2, 3, 4, 5}
# a.pop()
# print(a)
#
# # discard 删除
# a = {1, 2, 3, 4, 5}
# a.discard(4)
# print(a)
#
# # 查找
# # # in 和 not in
# a = {10, 2, 3, 4, 5}
# print(1 in a)
# print(10 in a)
#
# print(10 not in a)
#
