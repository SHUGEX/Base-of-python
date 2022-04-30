# 1. read(num):num表示字节，根据字节去读取数据
# file = open("test1.txt", "r")
# print(file.read(5))
# print(file.read())              # 不写参数表示读取所有的内容
# file.close()

# 2. readline():  一次读取一行内容,下一行的内容是在上一行内容已经读取到的前提之下
# file = open("test1.txt", "r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# 3. readlines():返回列表，列表中的一个数据是文件中的一行内容
# file = open("test1.txt", "r")
# print(file.readlines())
# file.close()

# seek(). 移动文件指针
# “语法”：文件对象.seek(偏移量，起始位置)
# “起始位置”：0,  文件开头
# 			  1,  当前位置
# 			  2,  文件结尾
# file = open("test2.txt", "r")
# file.seek(3, 0)             # 从文件开头向右偏移3个字节
# print(file.read())
# file.close()

# file = open("test2.txt", "a+")
# file.seek(0, 0)
# print(file.read())
# file.close()









