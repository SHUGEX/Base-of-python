# 需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能
# 1. 接收用户输入的文件名---》input()
# old_name = input("请输入您需要备份的文件名：")           # music.mp3
#
# # find()是从左至右,rfind()是从右至左
# index = old_name.rfind(".")             # index保存.对应的下标值
# # print(index)
# # 2. 规划备份好的文件的名字---》原文件名[备份].mp3 = 原文件名 + [备份] + 后缀
# new_name = old_name[:index] + "[备份]" + old_name[index:]
# # print(new_name)
#
# # 3. 打开原文件读取里面的内容，再打开备份文件写入原文件读取到的数据
# old_file = open(old_name, "rb")     # rb，wb, ab以二进制去读或者写，或者追加
# new_file = open(new_name, "wb")
# # 原文件读取内容,备份文件写入内容
# con = old_file.read()
# new_file.write(con)
#
# old_file.close()
# new_file.close()

# import os
#
# path = input("\033[1;36m请输入文件夹路径：\033[0m")  # 获取路径,引号内为引导用户输入内容的，可自行编辑，这里我用了改变颜色，具体格式为“\033[1;36m”需要改变颜色的字符串“\033[0m”
# path = path.replace("\\", "/")   # 将路径中的"\"替换为“/”,避免系统误认为转义字符
# files = os.listdir(path)
# print(files)                # 获取文件列表
# change = input("\033[1;36m请输入需要修改的文件后缀名以及插入内容如“png -备份”：\033[0m")  # 获取路径,引号内为引导用户输入内容的，可自行编辑，这里我用了改变颜色，具体格式为“\033[1;36m”需要改变颜色的字符串“\033[0m”
# suffix, add = change.split(" ")  # 拆分 获得目标文件后缀名和插入内容
# for old in files:
#     if old.rfind(f".{suffix}") != -1:    # 判断是否为目标文件后缀名
#         index = old.rfind(f".{suffix}")
#         new = old[:index] + add + old[index:]  # 插入内容
#         os.rename(path + old, path + new)
# files = os.listdir(path)      # 获取修改后的文件列表
# print(files)                  # 打印修改后的文件列表



# import os
#
# path = input("\033[1;36m请输入文件夹路径：\033[0m")  # 获取路径,引号内为引导用户输入内容的，可自行编辑，这里我用了改变颜色，具体格式为“\033[1;36m”需要改变颜色的字符串“\033[0m”
# path = path.replace("\\", "/")   # 将路径中的"\"替换为“/”,避免系统误认为转义字符
# files = os.listdir(path)
# print(files)                # 获取文件列表
# change = input("\033[1;36m请输入需要转移的文件后缀名以及转移路径如“png X:\photo\”：\033[0m")  # 获取路径,引号内为引导用户输入内容的，可自行编辑，这里我用了改变颜色，具体格式为“\033[1;36m”需要改变颜色的字符串“\033[0m”
# suffix, path2 = change.split(" ")  # 拆分 获得目标文件后缀名和插入内容
# path2 = path2.replace("\\", "/")   # 将路径中的"\"替换为“/”,避免系统误认为转义字符
# if not os.path.isdir(path2):  # 判断输入路径是否为有效路径，如果不是就创建出来一个
#     os.makedirs(path2)        # 这样只要你路径格式对了就一定能转移
# for old in files:
#     if old.rfind(f".{suffix}") != -1:      # 判断是否为目标文件后缀名
#         old_file = open(path + old, 'rb')  # 读方式打开旧文件
#         new = open(path2 + old, 'wb')      # 写方式打开新文件
#         new.write(old_file.read())         # 旧文件写入新文件
#         old_file.close()                   # 关闭旧文件
#         os.remove(path + old)              # 删除旧文件
#         new.close()                        # 关闭新文件
# files = os.listdir(path2)      # 获取移动后的文件列表
# print(files)

# import os
# path = input("\033[1;36m请输入需要创建的文件夹列表的路径：\033[0m")  # 获取路径,引号内为引导用户输入内容的，可自行编辑，这里我用了改变颜色，具体格式为“\033[1;36m”需要改变颜色的字符串“\033[0m”
# path = path.replace("\\", "/")   # 将路径中的"\"替换为“/”,避免系统误认为转义字符
# if not os.path.isdir(path):  # 判断输入路径是否为有效路径，
#     os.makedirs(path)        # 如果不是就创建出来一个
# count = int(input("\033[1;36m请输入需要创建的子文件夹个数：\033[0m")) # 获取路径,引号内为引导用户输入内容的，可自行编辑，这里我用了改变颜色，具体格式为“\033[1;36m”需要改变颜色的字符串“\033[0m”
# for i in range(count):
#     os.mkdir(path + "/" + f"子文件夹{i + 1}")  # 这里可以进一步循环嵌套







