# 1.函数都是有返回值的
# 使用return关键字来进行反回
# def test1():
#     a = 500
#     return a
#
#
# num = test1()
# print(num-10)


# def test1():
#     a = 500
#     # return a
#     return
#
#
# print(test1())      # None
# 1.函数无论如何都会给你一个结果（返回值）
# 2.不使用return，python解释器回默认的使用return
# 3.返回的是只，不是变量


# 2.函数的返回值是函数调用结束之后最后给调用者的结果
# def test():
#     a = 500
#     return a
#     print("这是最后一行")
#
#
# print(test())
# 结束函数：在函数种遇到return，函数就结束了，下面的代码不在执行

# 返回多个数据
# def test():
#     a = 500
#     b = 1
#     return a, b, 'jiandan'
#
#
# print(test())
# print(type(test()))
# return返回多个数据，是以元组的形式进行输出
