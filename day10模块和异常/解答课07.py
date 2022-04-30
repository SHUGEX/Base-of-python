# 函数的作用：重复的使用，减少代码量
# 函数定义
# def 函数名():
#     函数体


# 函数的调用
# 函数名()


# def test():
#     print('我是函数')
#
#
# test()
# test()
# 注意：
# 1.函数必须要去调用,不调用不执行
# 2.函数被调用几次就执行几次
# 3.遇到函数调用就会直接去执行这个函数,函数执行完成之后会回到函数调用的地方,在往下执行下面的代码


# 2.带参的函数
# def test(参数(形参)):
#     函数体

# test(参数(实参))
# 形参是用来接收实参传递的数据的
# 实参是用来给形参传递数据的

# 函数的参数
# 1.位置参数:有几个形参就要有几个实参
# def test(a,b):
#     print(a,b)
#
#
# test(1,2)

# 2.默认参数:给形参设置默认值,一定要放在参数列表的最后
# def test(a,b=1):
#     print(a,b)
#
#
# test(1)

# 3.不定长参数(*args):参数以元组的形式保存
# def test(*args):
#     print(args)
#     print(type(args))
#
#
# test(1,2,3)


# 4.关键字参数(**kwargs)
# def test(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#
# test(name = 1)          # 键 = 值

# 1. 编写一个名为test1()的函数,它有一个名为number的参数，
# 如果参数是偶数,那么test1()就打印出number//2，
# 如果number是奇数,test1()就打印 3*number+1
# 1.定义函数
# def test1(number):
#     # 2.判断
#     if number % 2 == 0:
#         print(number//2)
#     else:
#         print(3*number+1)
#
#
# test1(12)


# 2. 写test2函数，接收n个数字，求这些参数数字的和
# 1.定义一个函数
# def test2(*args):
#     # 2.进行累加和
#     sum = 0
#     # print(args)
#     for i in args:
#         sum += i
#     print(sum)
#
# test2(1,2,3)


# def test2(*args):
#     print(sum(args))
#
#
# test2(1,2,3)

# 返回值return
# def test2(*args):
#     # 2.进行累加和
#     sum = 0
#     # print(args)
#     for i in args:
#         sum += i
#     return sum
#
#
# print(test2(1,2,3))

# 3. 写一个函数test3，判断用户传入的字符串长度是否大于5
# 1.定义函数
# str1 = input("请输入一个字符串")
# def test3(a):
#     # 2.判断
#     if len(a) <= 5:
#         print("字符串长度小于5")
#     else:
#         print("字符串长度大于5")
#
#
# test3(str1)


# 选择题
# 1. 关于函数，说法错误的是：()
# A. 使用函数的目的是为了在程序中减少代码量
# B. 函数的参数是使用了函数外部的数据，函数的返回值是为了把函数内部的数据返回出去
# C. 函数的返回值中，return可以退出函数
# D. 在函数中，print和return的使用是没有任何区别
# num1 = 1
# num2 = 2
# def test(a,b):
#     # print(a,b)
#     c = a + b
#     print(c)
#     return
#     return c
#     print('这是函数最后一行')
#
#
# print(test(num1,num2))
# return和循环里的break的用法一样


# 3. 关于Python的全局变量和局部变量，以下选项中描述错误的是：()
# A. 全局变量可以在多个函数中使用
# B. 全局变量的名字不能与局部变量的名字相同
# C. 为了区分全局变量和局部变量，往往起不同的名字
# D. 局部变量的值可以通过return返回给调用者
# 全局变量
# num = 1
# def test(a):
#     print(a)
#     print(num)
#
# test(num)

# 局部变量:只能在当前函数中使用
# a = 2
# def test2():
#     # global a        # 申明方式 global 变量名
#     a = 1
#     print(a)
#     return a
#
#
# test2()
# print(a)


# 4.下列说法错误的是：(c)
# A. 在模块和包中，包里面包括模块，模块里面包括类，函数，变量等
# B. 在异常中，Exception可以作为万能类捕获异常使用
# C. 在异常中，抛出异常就可以让控制台不报错
# D. 在异常中，raise的下方是不接任何代码的

# 有init文件的就是包

# 捕获异常
# try:
    # 可能出现错误的代码
# except:
#     备用的代码
# a = 1
# try:
#     a+'123'
# except Exception as e:
#     print(e)

# print(a)      # name 'a' is not defined
# print(a+'123')  # unsupported operand type(s) for +: 'int' and 'str'


# 抛出异常raise
# 代码没有出现错误，但是没有满足要求，主动的抛出异常
# def login():
#     a = input("输入密码")
#     if len(a) == 6:
#         print("符合条件")
#     else:
#         raise Exception("不符合条件")
#
# login()

