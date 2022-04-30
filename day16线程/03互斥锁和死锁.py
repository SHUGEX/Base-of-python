# import threading
# # 定义全局变量,num最终的结果是200万
# num = 0
#
# # 1. 创建互斥锁
# lock = threading.Lock()
#
# def add1():
#     # 2. 上锁：acquire()
#     lock.acquire()
#     for i in range(1000000):
#         # 注意：不可变数据类型在函数内部使用时需要声明
#         global num
#         num += 1
#     print(f"add1执行完成时num的值是{num}")
#     # 3. 释放锁：release()
#     lock.release()
#
# def add2():
#     lock.acquire()
#     for i in range(1000000):
#         # 注意：不可变数据类型在函数内部使用时需要声明
#         global num
#         num += 1
#     print(f"add2执行完成时num的值是{num}")
#     lock.release()
#
# thread1 = threading.Thread(target=add1)
# thread2 = threading.Thread(target=add2)
#
# thread1.start()
# # thread1.join()          # thread1执行完了才会执行thread2
# thread2.start()
# 1. 线程等待（join）让多任务变成了单任务，效率降低
# 2. 互斥锁：谁抢到锁谁就去执行锁中间的代码，由多任务变成了单任务，但是执行效率要比join高一点
# 注意：如果上锁了不释放锁，那么就会出现死锁的情况，所以一定要及时去释放锁















