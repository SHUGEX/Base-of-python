# 1. 导入模块threading模块
# import threading, time

# 定义全局变量
# list1 = []
#
# def add():
#     for i in range(3):
#         list1.append(i)
#         print(f"已添加{i}")
#
# def read():
#     print(f"读取到{list1}")
#
# # 不使用if __name__ == "__main__":这个语句
# # 2. 通过Thread()类创建线程对象
# add_thread = threading.Thread(target=add)
# read_thread = threading.Thread(target=read)
#
# # 3. 使用start()启动线程执行任务
# add_thread.start()
# read_thread.start()

# 结论：多线程之间都是会共享全局变量的

# 多线程共享全局变量时会存在数据不准确的问题(资源竞争的问题)
# 需求：定义两个函数﹐实现循环100万次﹐每循环一次给全局变量加1。

# 定义全局变量,num最终的结果是200万
# num = 0
#
# def add1():
#     for i in range(1000000):
#         # 注意：不可变数据类型在函数内部使用时需要声明
#         global num
#         num += 1
#     print(f"add1执行完成时num的值是{num}")
#
#
# def add2():
#     for i in range(1000000):
#         # 注意：不可变数据类型在函数内部使用时需要声明
#         global num
#         num += 1
#     print(f"add2执行完成时num的值是{num}")
#
# thread1 = threading.Thread(target=add1)
# thread2 = threading.Thread(target=add2)
#
# thread1.start()
# # thread1.join()          # thread1执行完了才会执行thread2
# thread2.start()
# # 1. 线程等待（join）让多任务变成了单任务，效率降低








