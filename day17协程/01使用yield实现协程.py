# def test1():
#     return 1
#     print(3)          # 不能执行
#
# print(test1())          # 1

# def test2():
#     yield 2
#     yield 3
#     yield 4
#
# t2 = test2()
# print(next(t2))         # 2，next(变量)：获取yield后面的返回值用的
# print(next(t2))         # 3，next(变量)：获取yield后面的返回值用的
# print(next(t2))         # 4，next(变量)：获取yield后面的返回值用的

# 使用yield实现协程
# import time
# def task1():
#     while True:
#         print("----1----")
#         time.sleep(0.1)
#         yield              # 把当前函数执行状态挂起，方便下次回来执行事会继续之前的状态向下执行
#
# def task2():
#     while True:
#         print("----2----")
#         time.sleep(0.1)
#         yield
#
# t1 = task1()
# t2 = task2()
# while True:
#     next(t1)
#     next(t2)

# 使用yield实现的多任务，就是所谓的协程，协程是单线程下的并发












