# 不可变数据类型：数值，字符串，元组
# id(变量)：检测内存地址的id值
# num1 = 10
# num2 = num1
# print(id(num1))
# print(id(num2))           # 打印的两个id值是相同的
#
# # 修改num1的值，然后再去测试id值
# num1 = 20       # 修改num1的值
# print(id(num1))
# print(id(num2))          # 打印的两个id值是不相同的，因为修改num1值的时候，是不修改原内存地址
#
#
# # 可变数据：列表，字典，集合
# list1 = [10, 20]
# list2 = list1
# print(id(list1))
# print(id(list2))            # 打印的两个id值是相同的
#
# # 修改list1的值，然后再去测试id值
# list1.append(30)            # 增加一个数据其实就是在修改列表
# print(id(list1))
# print(id(list2))                # 打印的两个id值是相同的,因为修改list1值的时候，是修改原内存地址

# 总结：原内存地址可以被修改，那么就是可变类型，原内存地址不可以被修改，那么就是不可变类型









