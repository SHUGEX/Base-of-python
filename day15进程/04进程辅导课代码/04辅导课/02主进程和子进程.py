# 1.获取进程编号
# import multiprocessing,os,time

# # 唱歌
# def sing():
#     for i in range(5):
#         print(f'进程编号{os.getpid()}')
#         print(f'父进程编号{os.getppid()}')
#         print('---sing---')
#         time.sleep(0.5)
#
#
# # 跳舞
# def dance():
#
#     for i in range(5):
#         print(f'进程编号{os.getpid()}')
#         print(f'父进程编号{os.getppid()}')
#         print('---dance---')
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     print(f'主进程编号{os.getpid()}')
#     # 子进程
#     p1 = multiprocessing.Process(target=sing)
#     p2 = multiprocessing.Process(target=dance)
#     # 启动
#     p1.start()
#     p2.start()

# 2.进程等待：join():等待进程执行结束
# def sing():
#     for i in range(5):
#         print('---sing---')
#         time.sleep(0.5)
#
#
# # 跳舞
# def dance():
#     for i in range(5):
#         print('---dance---')
#         time.sleep(0.5)
#
#
#
# # 程序的入口
# if __name__ == '__main__':
#     # 创建子进程
#     p1 = multiprocessing.Process(target=sing)
#     p2 = multiprocessing.Process(target=dance)
#     # 启动
#     p1.start()
#     p1.join()       # 阻塞
#     p2.start()


# 结束子进程：terminate():不管任务是否完成，立即终止子进程

# def sing():
#     for i in range(5):
#         print('---sing---')
#         time.sleep(10)
#
#
# # 跳舞
# def dance():
#     for i in range(5):
#         print('---dance---')
#         time.sleep(0.5)
#
#
#
# # 程序的入口
# if __name__ == '__main__':
#     # 创建子进程
#     p1 = multiprocessing.Process(target=sing)
#     p2 = multiprocessing.Process(target=dance)
#     # 启动
#     p1.start()
#     time.sleep(1)
#     p1.terminate()
#     p2.start()
