# 为什么要捕获异常：让控制台不报错
# try:
#     尝试执行的代码
# except 错误类型:
#     出现错误的处理

# try:
#     a
# except Exception as e:
#     print(e)


# 抛出异常:为了让控制台报错
# raise 错误
# def test():
#     a = input('输入你的密码：')
#     if len(a) == 6:
#         print('符合条件')
#     else:
#         raise Exception('不符合条件')
#
#
# test()

# def test():
#     a = input('输入你的密码：')
#     if len(a) == 6:
#         print('符合条件')
#     else:
#         print('不符合条件')


# for i in range(5):
#     test()