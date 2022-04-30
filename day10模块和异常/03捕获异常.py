# 1. 认识异常
# “实例”: 以r（读取）方式打开一个不存在的文件。
# open("test1.py", "r")               # 报错，test1.py文件不存在
# “语法”:
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码（备用代码）
# try:
#     open("test1.py", "r")
# except:
#     open("test1.py", "w")           # w模时当文件不存在会创建文件

# 2. 捕获异常
# “语法”:
# try:
#     可能发生错误的代码
# except 异常类型:
#     如果捕获到了异常会去执行的代码

# 2.1 通过异常类型进行捕获
# num = 1
# print(num)          # 异常类型：NameError

# try:
#     print(num)
# except NameError:
#     print("有错误！")

# 2.2 通过万能异常类进行捕获, Exception
# try:
#     print(num)
# except Exception:
#     print("有错误！")

# 2.3 捕获报错信息
# try:
#     print(num)
# except Exception as result:
#     print(result)                    # name 'num' is not defined






