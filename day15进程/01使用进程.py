# import time
# def test1():
#     for i in range(4):
#         print("hello")
#         time.sleep(0.5)
#
# def test2():
#     for i in range(4):
#         print("world")
#         time.sleep(0.5)
#
# # test1()
# # test2()
# # 使用进程实现多任务的步骤
# # 1.  导入进程包：import multiprocessing
# import multiprocessing
# if __name__ == '__main__':
#     # 2.  调用Process类创建实例对象
#     process1 = multiprocessing.Process(target=test1)            # process1进程对象
#     process2 = multiprocessing.Process(target=test2)            # process2进程对象
#     # 3. 启动进程:  start()启动子进程实例(创建子进程)
#     process1.start()
#     process2.start()

# 进程对象执行的任务是无序的，由操作系统管的
# 主进程：一个程序正在执行的时候，默认存在的
# 子进程：手动创建的进程，能看间的就是子进程


