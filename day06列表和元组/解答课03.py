# while循环
# 语法
# 初始值
# while 条件(对初始值进行判断):
#     代码
#     改变初始值的大小

# 死循环
# a = 1
# while a < 3:
#     print(a)
#     a += 1          # 相当于a = a + 1
# print(123)
# 循环的运行方式:当程序遇到循环的时候,先执行完整个循环在往下执行下面的代码

# for循环
# 语法
# for 变量 in 字符序列:
#     代码
# a = 'asdfghjkl'
# for i in a:
#     print(i)
# print(123)

# range():取数器           range(开始位置,结束位置,步长)
# 开始位置的默认值为0
# 步长默认为1
# 结束位置取不到(前包后不包)
# print(range(5))
# for i in range(1, 5, 2):      # 步长指的是间隔的单位
#     print(i)


# 1.编写程序实现1-100以内的奇数累加和
# 思路:
# 1.通过循环输出1-100
# 2.取出奇数
# 3.对奇数进行累计和
# 方法一:取余
# a = 1
# num = 0
# while a <= 100:
#     # print(a)
#     if a % 2 == 1:      # 判断是否为奇数
#         # print(a)
#         num = num + a
#     a += 1
# print(num)

# 方法2:计数器设置为2
# a = 1
# num = 0
# while a <= 100:
#     # print(a)
#     num += a        # 放上面才是从1开始累加
#     a += 2
#     # num += a      # 放在下面是从3开始累加
# print(num)

# for循环
# num = 0
# for i in range(1,100,2):  # 步长设置为2，取出奇数
#     # print(i)
#     num += i
# print(num)

# 2. 使用循环实现输出 1 2 3 4 5 7 8 9 11 12
# 思路：
# 1.使用循环输出1，2，3，4，5，6，7，8，9，10，11，12
# 2.去掉6和10
# for i in range(1, 13):
#     # print(i)
#     if i == 6 or i == 10:
#         pass        # 占位符，作用：过，让代码继续往下执行
#     else:   # 其他的
#         print(i,end=' ')    # 末尾换行

# or :两边的条件一个为真就为真，都假才假



# 3. 已知用户名"maiya",密码是123，请实现效果：可重复输入用户名和密码，直到登陆成功。
# 输入错误提示登陆失败，并且设置程序只允许输入3次。
# 思路：
# 1.先写登录程序
#     1.1输入用户名和密码
#     1.2判断用户名和密码是否正确
# 2.把登录程序直接放在循环里
# name = input('请输入你的用户名：')
# pwd = int(input('请输入你的面密码：'))
# if name == 'maiya' and pwd == 123:
#     print('登陆成功')
# else:
#     print('登陆失败')

# a = 1
# while a <= 3:
#     # print(a)
#     name = input('请输入你的用户名：')
#     pwd = int(input('请输入你的面密码：'))
#     if name == 'maiya' and pwd == 123:
#         print('登陆成功')
#         break
#     else:
#         print('登陆失败')
#         print(f'还剩{3-a}次机会')
#     a += 1

# break：结束整个循环
# continue:结束这一次的循环，回到循环开始的地方

# 无限制的重复输入
# while True:
#     # print(a)
#     name = input('请输入你的用户名：')
#     pwd = int(input('请输入你的面密码：'))
#     if name == 'maiya' and pwd == 123:
#         print('登陆成功')
#         break
#     else:
#         print('登陆失败')



# 4.已知字符串fruits='苹果5个，香梨4个，西瓜3个，哈密瓜6个，桃子3个, 桔子7个'，
#    要求请编写程序使用for循环统计水果的总数。
# （提示：循环字符串 ，判断字符是否是数字，最后进行累加）
# 思路：
# 1. 使用循环依次取出所有字符
# 2.使用判断，判断字符是否为数字      isdigit()
# 3.是数字就转换类型进行累计和
# 4.打印累计和

# isdigit()的用法,判断字符是否为数字   注意：判断的字符串
# a = 'q'
# print(a.isdigit())

# fruits = '苹果5个，香梨4个，西瓜3个，哈密瓜6个，桃子3个, 桔子7个'
# num = 0
# for i in fruits:
#     # print(i)
#     if i.isdigit():
#         # print(type(i))
#         num += int(i)
# print(num)




