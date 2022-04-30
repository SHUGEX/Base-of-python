# # 1. 打开文件，open(文件名，打开模式)，w(当所打开的文件不存在时，会新建这个文件)
# file = open("test1.txt", "w")
#
# # 2. 对文件中数据进行读取，写入等操作,r-->read(读取)，w--->write(写入)
# file.write("aabbcc")
#
# # 3. 关闭文件, close()
# file.close()

# 文件的访问模式，r-->read(读取)，w--->write(写入), a--->append(追加)
# 1. r-->read(读取),注意：a. 如果打开文件不存在时，会报错，b. r模式下只能读取，不能去写入数据
# file = open("test2.txt", "r")       # 报错
# file.write("aaa")                   # 报错
# file.close()

# 2. w--->write(写入)，注意：a. 如果打开文件不存在时，会新建文件，b. w模式下只能写入，不能去读取数据
# file = open("test2.txt", "w")
# file.write("bbb")               # w模式之下写入数据时，会覆盖原有内容
# file.close()

# 3. a--->append(追加)，注意：a. 如果打开文件不存在时，会新建文件
# file = open("test3.txt", "a")
# file.write("bbb")               # 在原有的内容基础之上，追加新内容
# file.close()

# r+,w+,a+:也是访问模式表示又可以读又可以写












