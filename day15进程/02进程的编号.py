# import multiprocessing, time, os
#
# # 定义跳舞任务
# def dance(a, b, c):
#     print(a, b, c)
#     # print(f"第一个子进程的编号{os.getpid()}")
#     # print(f"process1父进程的编号{os.getppid()}")
#     print(multiprocessing.current_process())        # current_process()获取进程对象
#     for i in range(3):
#         print("跳舞中...")
#         time.sleep(0.5)
#
# # 定义唱歌任务
# def sing(name, age):
#     print(name, age)
#     # print(f"第二个子进程的编号{os.getpid()}")
#     # print(f"process2父进程的编号{os.getppid()}")
#     print(multiprocessing.current_process())        # current_process()获取进程对象
#     for i in range(3):
#         print("唱歌中...")
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':          # 防止主进程中一些代码被子进程创建时复制,或者访问
#     print(f"主进程的编号{os.getpid()}")
#     print(multiprocessing.current_process())            # 主进程对象是MainProcess
#     # 4.args∶以元组方式给执行任务传参
#     # 5.kwargs: 以字典方式给执行任务传参
#
#     process1 = multiprocessing.Process(target=dance, name="dance_process", args=(1, 2, 3))
#     process2 = multiprocessing.Process(target=sing, name="sing_process", kwargs={"name": "maiya", "age": 18})
#
#     process1.start()
#     process2.start()

















