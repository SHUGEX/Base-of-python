# 模块：内置模块（比如random是python已经写好的模块）和第三方模块（手动安装的）
# import random           # 查看内置模块--》长按ctrl + 鼠标的光标左键点击
# 所以所谓的模块其实就是一个普通的py文件

# 导入模块的方式
# 1.import 模块名
# 语法:
# import 模块名
# import 模块名1，模块名2....
# 模块名.功能名()
# math模块中有sqrt()-->开平方，fabs()---》绝对值，fmod()--->余数
# import math, random

# 使用函数：模块名.函数名()
# print(math.sqrt(9))                 # 3.0
# print(random.randint(1, 9))

# 2.from 模块名 import 功能名
# 语法:from 模块名 import 功能1，功能2，功能3
# from math import sqrt
# from math import sqrt, fabs, fmod
# #
# # # 使用函数：函数名()
# print(sqrt(9))              # 3.0
# print(fabs(-9))             # 9.0
# print(fmod(10, 3))          # 1.0
#
# # 3.语法:from 模块名 import *,导入一整个模块
# from time import *
#
# # 使用函数：函数名()
# print(1)
# sleep(2)                     # sleep可以暂停，小括号中给秒数，给多少秒，睡多少秒
# print(2)














