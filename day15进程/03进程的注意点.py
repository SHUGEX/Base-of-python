# 1.  进程之间不共享全局变量
# import multiprocessing, time

# list1 = []          # 全局变量是可变类型
#
# # 定义添加函数
# def add():
#     for i in range(3):
#         list1.append(i)
#         print(f"已添加{i}")
#         time.sleep(0.2)
#
# # 定义读取函数
# def read():
#     print(f"读取：{list1}")
#
# if __name__ == '__main__':
#     process1 = multiprocessing.Process(target=add)
#     process2 = multiprocessing.Process(target=read)
#
#     process1.start()
#     process1.join()         # join(): 主进程等待子进程执行结束
#     process2.start()        # 进程之间是不共享数据的

# # 2.  主进程退出子进程正在执行也会直接销毁
# def test1():
#     while True:
#         print("子进程正在执行任务中...")
#         time.sleep(0.2)
#
# if __name__ == '__main__':
#     process1 = multiprocessing.Process(target=test1)
#     process1.daemon = True      # 2. 设置process1成为守护主进程
#     process1.start()
#     time.sleep(1)
#     # process1.terminate()            # 1. terminate(): 不管任务是否完成，立即终止子进程
#     print("hello world")            # 主进程结束了

# 多任务用一个子进程和主进程去控制实现






