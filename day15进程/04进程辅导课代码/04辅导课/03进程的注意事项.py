# # 1.进程之间不共享全局变量
# import multiprocessing,time
# 
# list1 = []       # 可变的数据类型
# 
# def func():
#     for i in range(3):
#         list1.append(i)
#         print(f'添加了{i}')
#         print(list1)
# 
# 
# def read():
#     print(list1)
# 
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=func)
#     p2 = multiprocessing.Process(target=read)
#     p1.start()
#     p2.start()

