# # 1. + ：将序列中的数据合并，支持字符串，列表，元组，不支持集合，字典
# str1 = "123"
# str2 = "345"
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# dict1 = {"age": 18}
# dict2 = {"id": 110}
# print(str1+str2)            # 123345
# print(set1 + set2)              # 报错，集合不支持合并，黄色的方块，要么是警告，要么会报错
# print(dict1 + dict2)          # 报错
#
# # 2. * ：将序列中的数据复制,支持字符串，列表，元组，不支持集合，字典
# str1 = "123"
# list1 = [1, 2, 3]
# set1 = {1, 2, 3}
# print(str1 * 4)                 # 123123123123
# print(list1 * 2)                # [1, 2, 3, 1, 2, 3]
# print(set1 * 4)                     # 报错
#
# # 3. sum(序列):返回序列中数据的和
# list1 = [1, 3, 5, 7]            # 16
# set1 = {1, 2}
# str1 = "123"
# print(sum(str1))            # 报错，字符串是不能相加
# print(sum(list1))
# print(sum(set1))
#
# str2 = "abc"
# # 4. max():返回序列中最大值和min()最小值
# print(max(list1))           # 7
# print(min(list1))           # 1
#
# print(max(str2))            # c
# print(min(str2))            # a,a-z中,a是最小的，z是最大的

# 5. enumerate(序列，起始下标)：枚举函数，用来改变下标的默认起始值，一般搭配for循环使用
str1 = "maiya"
for i in enumerate(str1, start=2):
    print(i)                # 返回的是一个元组，元组的第一个数据是修改之后的下标，第二个数据是相对应的数据
    print(str1[2])        # i











