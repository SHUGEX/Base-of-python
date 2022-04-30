# 一、单选题，一个2分，共10个，选错不得分（20分）
# 1.判断下列变量名哪些不符合规范：（  ）
# A.info_print1
# B._name
# C.true
# D. 3_password

# 2.在使用格式化输出”我的名字是tom,今年18岁，我的体重是75.5公斤，学号是001”，下列输出正确的是（ c ）
# A.print("我的名字是%s,今年%d岁了，体重%f公斤，学号是%03d" % (name, age, weight, stu_id))
# B.print("我的名字是%s,今年%d岁了，体重%.1f公斤，学号是%d" % (name, age, weight, stu_id))
# C.print("我的名字是%s,今年%d岁了，体重%.1f公斤，学号是%03d" % (name, age, weight, stu_id))
# D.print("我的名字是%s,今年%s岁了，体重%s公斤，学号是%s" % (name, age, weight, stu_id))
# %f:自动保留6位小数
# a = 75.5
# print("%s"%a)

# b = 1
# print('%03d'%b)


# 3.示例：list1=['pink', 'blue', 'yellow']，我们在使用列表时，以下哪个选项，会引起索引错误？（  d ）
# A． list1[-1]
# B． list1[-2]
# C． list1[0]
# D． list1[3]
# list1=['pink', 'blue', 'yellow']
# print(list1[2])

# 4.下面的代码会输出什么（ c ）
# s = "hello python"
# b = s.split("o")
# print(b)
# A. ['hell', '', ' pyth', 'n']
# B. ['hell', '', ' pyth', '', 'n']
# C. ['hell', ' pyth', 'n']
# D. ['hell', '', 'pyth', 'n']
#
# 5.以下说法正确的是：（ c ）
# A.while循环不可以和for循环嵌套使用
# B.if条件表达式后不一定要使用冒号
# C.如果只是控制循环次数, for i in range(20)和for i in range(20, 40)的作用是一样的
# D.continue可以用于单独的if判断中
# i = 1
# while i < 3:
#     print(f'我是while的值{i}')
#     i += 1
#     for j in range(2):
#         print(j)

# for i in range(20):
#     print(i)

# for i in range(20, 40):
#     print(i)


# 6. 代码list1 = [1, 2, [3, 4]],执行print(list1[2][1])的结果是（ d ）
# A. 1      B. 2        C. 3        D. 4
# list1 = [1, 2, [3, 4]]
# print(list1[2][1])
# a = list1[2]
# print(a)
# print(a[1])

#
# 7. 关于函数，下列说法中不正确的是：( d )
# A. 函数就是一段封装好的代码
# B. 函数能够实现代码的重用
# C. 函数可以有多个值返回
# D. 函数的位置参数可以随意传递，不用按照顺序传值
# def func(a,b):
#     return a,b
#
#
# print(func(2,1))
# print(type(func()))

# 8.关于面向对象的说法中，不正确的是( ad )
# A. __init__方法没有返回值
# B. __str__方法必须有返回值
# C. 对象是由类创建出来的，对象是类的实例
# D. 对象可以决定类的属性
class A(object):
    name1 = '张三'
    def __init__(self):
        self.name = '简单'


a = A()
print(A)
print(a.name1)
print(A.name1)

# 9. 关于 python 类继承，下列描述错误的是 （ b ）
# A．继承分为单继承和多继承。
# B．对于继承而来的父类方法，子类不可以重写。
# C．子类可以拥有多个父类，并且具有所有父类的属性和方法。
# D．子类除了拥有继承父类而来的属性和方法之外，还可以自定义子类自己的属性和方法。
class A(object):
    def test(self):
        print('父类的方法')


class B(A):
    def test(self):
        super().test()
        print('子类的方法')

    def test2(self):
        print('新的方法')

b = B()
b.test()
b.test2()


# 10.下列关于多线程共享数据描述错误的是? ( d )
# A. 多线程之间可以进行数据的共享
# B. 多线程程序可以通过全局变量实现数据的共享
# C. 多线程在使用全局变量共享数据时, 可能会出现问题
# D. 多线程可以使用线程异步解决共享数据时出现的问题

# 定义全局变量,num最终的结果是200万
import threading
num = 0

def add1():
    for i in range(1000000):
        # 注意：不可变数据类型在函数内部使用时需要声明
        global num
        num += 1
    print(f"add1执行完成时num的值是{num}")


def add2():
    for i in range(1000000):
        # 注意：不可变数据类型在函数内部使用时需要声明
        global num
        num += 1
    print(f"add2执行完成时num的值是{num}")

thread1 = threading.Thread(target=add1)
thread2 = threading.Thread(target=add2)

thread1.start()
# thread1.join()          # thread1执行完了才会执行thread2
thread2.start()





