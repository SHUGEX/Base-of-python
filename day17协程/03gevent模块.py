# 使用gevent模块“步骤”：
# 	1.  导入gevent模块
# import gevent, time
#
# def eat():
#     print("吃麻辣小龙虾")
#     # time.sleep(0.1)         # 是延时操作，不能替换耗时操作
#     gevent.sleep(0.2)
#     print("吃烧烤")
# def play():
#     print("去橘子洲")
#     gevent.sleep(0.1)
#     print("去岳麓区")
#
# # 	2.  实例化协程对象，需要调用spawn函数
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
#
# # 	3.  调用join()函数,等待
# g1.join()           # 等待g1对象对应的任务执行
# g2.join()

# 使用gevent模块实现的协程是单线程下以并发的执行方式实现的多任务，执行效率更高

# 进程，线程，协程的对比和联系
# 1. 进程：当程序运行起来之后，所使用的资源才会产生进程，所以进程是操作系统分配资源的基本单位
#    多进程实现多任务---》并行的执行方式，有几个进程就会相对应去执行几个任务

# 2. 线程：是操作系统能够运行的最小单位，
#    多线程实现多任务---》并行的执行方式，在一个进程中有多个线程去执行多个任务
# 多进程 = 手机--》多个qq， 好处：稳定性更强
# 多线程 = 一个qq上去开启多个聊天窗口，好处：资源占用少

# 3. 协程：比线程占用更少的资源，如果线程实现交替执行任务，性能消耗很大
#    如果使用协程，就是自动切换任务，并不会去重新加载，所以通常都是用协程实现并发

# 总结：
# 1. 进程是资源分配的基本单位，线程是cpu调度的基本单位
# 2. 多进程切换任务需要的资源是最大的，效率很低
# 3. 多线程切换任务需要的资源一般，效率一般
# 4. 协程切换任务需要的资源很小的，效率高
# 5. 多进程，多线程根据cpu的核数不一样是可能是并行的，但是协程只能是单线程之下的并发

# date = input("输入年、月(以空格隔开)：")
# date = date.split(" ")
# year = int(date[0])
# month = int(date[1])
# leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
# if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
#     print("本月31天")
# elif month == 2:
#     if leap:
#         print("本月29天")
#     else:
#         print("本月28天")
# else:
#     print("本月30天")

# 猜年龄游戏：使用随机模块随机出1 - 18
# 范围内任意一个数字，用户在控制台输入任意数字，与随机数字比较大小，
# 小了，提示猜小了，大了，提示猜大了，如果猜对了，打印恭喜信息并退出，
# 允许用户最多尝试5次，5
# 次都没猜对的话直接退出程序。

# import random
# random_age = random.randint(1, 18)
# for i in range(5):
#     age = int(input("请输入1-18内任意数字："))
#     if age == random_age:
#         print("恭喜您猜对了！")
#         break
#     elif age > random_age:
#         print("猜大了")
#     elif age < random_age:
#         print("猜小了")

# 编写一个函数, 接收字符串参数, 返回一个元组,
# 元组的第一个值为大写字母的个数, 第二个值为小
# 写字母个数，已知字符串'HeLLo WrOlD, hELlO pYtHoN'
# import re
# str1 = input("请输入字符串：")
# list1 = (len(re.findall("[A-Z]", str1)), len(re.findall("[a-z]", str1)))
# print(list1)

# 定义一个表示学生信息的类Student要求如下：
# (1)类Student的成员属性：No表示学号；Name
# 表示姓名；Sex表示性别；Age表示年龄；Python：
# 表示python课程成绩。
# (2)类Student的方法成员：getNo（）：获得学号；getName（）：获得姓名；
# getSex（）：获得性别；getAge（）获得年龄；getPython（）：获得python课程成绩。
# (3)根据类Student的定义，创建三个该类的实例对象，输出每个学生的信息，计算并输出
# 这三个学生Python基础成绩的平均值，以及计算并输出他们python基础成绩的最大值和最小值


# class Student(object):
#
#     def getNo(self, No):
#         self.No = No
#
#     def getName(self, Name):
#         self.Name = Name
#
#     def getSex(self, Sex):
#         self.Sex =Sex
#
#     def getAge(self, Age):
#         self.Age = Age
#
#     def getPython(self, Python):
#         self.Python = Python
#
#     def __str__(self):
#         return f"学号:{self.No},姓名:{self.Name},性别:{self.Sex},年龄:{self.Age},python课程成绩:{self.Python}"

#
# student1 = Student()
# student2 = Student()
# student3 = Student()
# student1.getNo("001")
# student2.getNo("002")
# student3.getNo("003")
# student1.getName("Lisa")
# student2.getName("Jock")
# student3.getName("Tom")
# student1.getSex("女")
# student2.getSex("男")
# student3.getSex("男")
# student1.getAge(18)
# student2.getAge(22)
# student3.getAge(25)
# student1.getPython(92)
# student2.getPython(94)
# student3.getPython(91)
# print(student1)
# print(student2)
# print(student3)
# print(f"平均分:{(student1.Python + student2.Python + student3.Python)/3}")
# print(f"最高分:{max(student1.Python, student2.Python, student3.Python)}")
# print(f"最低分:{min(student1.Python, student2.Python, student3.Python)}")


#  s = ' 123.33sdhf3424.34fdg323.324',用正则知识计算字符串中所有数字的和。
# import re
# s = ' 123.33sdhf3424.34fdg323.324'
# num = re.findall("[\d]", s)
# sum1 = 0
# for i in range(len(num)):
#     sum1 += int(num[i])
# print(sum1)
# print(f"{sum(re.findall("[\d]", str1))}"




