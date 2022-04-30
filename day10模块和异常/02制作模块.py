# “需求”:
# 1．新建一个Python文件，命名为module1.py，并定义testA函数，testA函数完成2个数字的加法运算。
# 2. 调用模块
# 导入module1模块
# import module1

# 使用模块中的testA函数,模块名.函数名()
# print(module1.testA(4, 5))              # 9

# 自定义的模块名不要和已经有的内置模块名冲突
# 导入模块时有搜索顺序，自己的目录的模块 > 内置模块

# all列表的作用：控制模块中的函数是否可以被其他的文件所导入
# 注意点：在from xxx import * 导入方式时，all列表才能生效
# from module1 import *
#
# print(testA(1, 3))          # 4
# testB()                     # 报错，因为all列表中没有testB

# 导入包：import 包名.模块名
# 使用包：包名.模块名.函数名()








