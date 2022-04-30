# import multiprocessing, time
# “Queue类(队列)”：
# 	1.  q.put():  放入数据(入队)
# 	2.  q.get():  取出数据(出队)
# 	3.  q.empty(): 如果队列为空，返回True
# 	4.  q.qsize(): 返回当前队列包含的消息数量
# 	5.  q.full(): 如果队列满了，返回True

# q = multiprocessing.Queue(3)
# q.put("maiya")
# q.put("jiandan")
# print(q.full())             # False
# q.put("susu")
# print(q.full())             # True
# # q.put("bingbing")
# print(q.qsize())            # 3
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.qsize())            # 0
# print(q.empty())            # True

# list1 = ["maiya", "susu", "jiandan"]
#
# def add(q1):
#     for i in list1:
#         q1.put(i)
#         print(f"{i}已经添加")
#         time.sleep(0.5)
#
# def read(q2):
#     while True:
#         if q2.empty() == True:
#             break
#         print(f"读取的数据是：{q2.get()}")
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     process1 = multiprocessing.Process(target=add, args=(q,))
#     process2 = multiprocessing.Process(target=read, args=(q,))
#
#     process1.start()
#     process1.join()
#     process2.start()


















