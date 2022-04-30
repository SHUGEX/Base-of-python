# a. 编写程序实现1-100以内的奇数累加和
# s = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         print(i)
#         s += i
# print(s)
#
#
# # b. 使用循环实现输出 1 2 3 4 5 7 8 9 11 12（注意：可以使用退出循环的方式使数字6和10不取）
#
# for j in range(1,13):
#     if j == 6 or j == 10:
#         continue
#     print(j, end=' ')
#
# # c. 已知用户名"maiya",密码是123，请实现效果：可重复输入用户名和密码，直到登陆成功。
# # 以上练习题使用while循环和for循环其中一种实现即可
# name = 'maiya'
# code = '123'
# e_name = input('用户名：')
# e_code = input('密码：')
# while e_name != name or e_code != code:
#     if e_name != name:
#         e_name = input('用户名：')
#     elif e_name == name:
#         e_code = input('密码：')
#     else:
#         print('error')
# print('success')
