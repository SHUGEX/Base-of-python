# 1. a=60;b=13;c=13，a>b（真） and b<c（假） 输出的结果是(False)
# and:都真才真，一假则假
# a = 60
# b = 13
# c = 13
# print(a>b and b<c)


# 2. 已知x=3，并且 id(x)的返回值为496103280，那么执行语句x+=6之后，判断表达式id(x)== 496103280的值为（False）
# id()：获取对象的内存地址
# x = 3
# print(id(x))
# x += 6
# print(id(x))
# x = 9
# print(id(x))
# -5到256整数内存地址是固定的
# list1 = []
# print(id(list1))
# list1.append(1)
# print(id(list1))


# 3. 己知x=3，那么执行语句x *= 6之后，x的值为（18）
# x = 3
# x *= 6      # x = x * 6
# print(x)

# 4. break语句用在循环语句中，是否可以跳出二重循环结构(不能)
# for i in range(3):
#     print(f'i的值为{i}')
#     for j in range(2):
#         print(j)
#         break
# break 结束循环：只对循环嵌套中的最近的一层起作用


# 5. 对于带有else子句的 for循环和 while循环，当循环因循环条件不成立.而自然结束时(会?不会?)执行else 中的代码。(会)
# i = 1
# while i < 3:
#     print(i)
#     i += 1
#     break
# else:
#     print('我是else')
# 循环中的else子句，可以看作一种奖励机制,只有当循环是因为条件不满足而退出的才会执行else子句


# 6. 假设列表对象aList的值为[3, 4, 5, 6, 7, 9, 11, 13, 15, 17]，那么切片aList[3 : 7]得到的值是([6, 7, 9, 11])
# list1 = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
# print(list1[3:7])

# 7. 任意长度的Python列表、元组和字符串中最后一个元素的下标为（-1,长度-1）
# 下标为负：最后一个元素的下标为-1，从右至左依次减小
# 下标为正：第一个元素的下标是0，从左往右依次增加
# list1 = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
# print(len(list1)-1)

# 8. Python语句 list1(range(1,10,3))执行结果为（[1, 4, 7]）,那么list2(range(6))[::2]执行结果为([0,2,4])
# print(list(range(1,10)))
# print(list(range(1,10,3)))
# print(list(range(6)))
# print(list(range(6))[::2])      #[0, 2, 4]


# 9. 已知x = {1 :2}，那么在执行语句x[2] = 3 之后，x的值为({1: 2, 2: 3})
# x = {1: 2}
# x[2] = 3        # 字典添加
# x[1] = 4        # 有则修改，无则添加
# print(x)

# 10. 表达式set([1, 1, 2, 3])的值为({1, 2, 3})
# x = {}
# print(type(x))
# x = set()
# print(type(x))
# 集合：里面的元素是唯一的，且无序
# print(set([1, 1, 2, 3]))

# 11. 如果函数中没有return语句或者return语句不带任何返回值，那么该函数的返回值为（None）
# 函数都是有返回值的
# def func():
#     print('我是函数')
#     # return 123
#     return
#
#
# print(func())
# 如果不使用return，解释器会默认的使用return返回None


# 12. 表达式sum(range(1, 10, 2))的值为()
# print(list(range(1, 10)))
# print(list(range(1, 10, 2)))
# # sum：用来计算累计和的
# print(sum(range(1, 10, 2)))

# 13．编写一个程序，判定用户输入的两个数a和 b，如果用户输入的第一个数大，则两数互换，如果相等或第一个数小，
# 那原样输出。
# 方法一
# a = int(input('输入第一个数'))
# b = int(input('输入第二个数'))
# print(a)
# print(b)
# if a > b:
#     a,b = b,a     # 序列赋值
#     print(a)
#     print(b)
# else:
#     print(a)
#     print(b)

# 方法二
# a = int(input('输入第一个数'))
# b = int(input('输入第二个数'))
# if a > b:
#     num = a
#     a = b
#     b = num
#     print(a)
#     print(b)
# else:
#     print(a)
#     print(b)