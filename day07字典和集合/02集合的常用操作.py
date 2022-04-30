# 1. 集合格式：{数据1,数据2,数据3,数据4,......}
# 存储有数据的集合
# s1 = {10, 20, 30, 40}
# print(type(s1))         # set

# # 2. 定义空集合,注意：只能使用set()
# list1 = []          # 定义空列表
# s2 = {}             # 不是空集合，而是空字典
# s2 = set()            # 定义空集合
# print(type(s2))         # set
# s3 = set("12345")
# print(s3)           # {'2', '4', '1', '5', '3'}

# # 3. 集合的特点：无序和去重
# s4 = {10, 20, 30, 40}
# print(s4)               # {40, 10, 20, 30},集合是无序，不支持下标操作
# print(s4[1])          # 报错
#
# s5 = {10, 20, 10, 40, 20}
# print(s5)                   # {40, 10, 20},集合中的数值不重复，去重

# 4.集合的常用操作
# 1. 集合的增加数据
# 1.1 add(数据):数据不能是序列，是序列就会报错(不包括字符串)
# s1 = {10, 20}
# s1.add(30)
# s1.add([12, 13])            # 报错
# print(s1)

# 1.2 update(序列)
# s1.update(30)           # 报错，单个数据不能添加
# s1.update([12, 13])           # {10, 13, 20, 12}，序列的话是逐一添加
# print(s1)

# s2 = {10, 20, 30, 40}
# # 2. 删除，remove，discard,pop
# s2.remove(30)
# print(s2)               # {40, 10, 20},删除指定的数据
# s2.remove(30)           # 删除不存在的数据会报错
# print(s2)

# s2.discard(30)
# print(s2)           # {40, 10, 20}
# s2.discard(30)
# print(s2)                           # 删除不存在的数据不会报错

# del_num = s2.pop()                # 返回被删除的数据
# print(del_num)              # 40, 随机删除，因为集合的无序特点，其实默认删除集合中的第一个数据
# print(s2)
#
# s3 = {10, 20, 30, 40}
# # 查找：in 和not in
# print(30 in s3)         # True






