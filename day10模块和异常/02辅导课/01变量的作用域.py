# 全局变量：作用范围整个程序
# a = 1
#
#
# def test1():
#     print(a)
#
#
# test1()
# print(a)

# 局部变量：在函数里面定义的变量，只在当前函数里面起作用
# def test2():
#     a = 1       # 局部变量
#     print(a)
#
#
# test2()
# print(a)
# def test3():
#     print(a)
#
#
# test3()

# 3.将局部变量声明为迁居变量（global）
# 语法：global 变量名


# def test2():
#     global a,b
#     a = 1       # 局部变量
#     b = 2
#     print(a)
#
#
# test2()
# print(a,b)
