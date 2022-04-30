# 1. 导入模块threading模块
# import threading, time
#
# def dance():
#     for i in range(3):
#         print("跳舞中...")
#         time.sleep(0.1)             # 为了运行效果延迟一些，效果更明显
#
# def sing():
#     for i in range(3):
#         print("唱歌中...")
#         time.sleep(0.1)
#
# # 2. 通过Thread()类创建线程对象
# thread1 = threading.Thread(target=dance)            # thread1是子线程
# thread2 = threading.Thread(target=sing)
# # 3. 启动线程执行任务
# thread1.start()
# thread2.start()

# 子线程之间执行也是无序的，由cpu的调度去决定谁先执行的，主线程执行一定在子线程的前面
# 子进程之间执行也是无序的，由操作系统去决定谁先执行的，主进程的执行一定在子进程的前面

# 主进程是看不见，里面有一个主线程
# 1. 如果在主进程中手动创建了其他的进程，那么就是子进程
# 2. 如果在主进程中手动创建了其他的线程，那么就是子线程
# 当前代码中有1个进程， 有3个线程---1个主线程，2个子线程

# 多进程（2个及以上）和多线程（1个进程）的区别：
# 1. 多线程 执行效率高，系统资源占用少
# 2. 多进程要比多线程稳定些





