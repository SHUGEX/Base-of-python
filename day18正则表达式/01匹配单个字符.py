# 1. 导入re模块
# import re
# 2. 使用findall方法进行匹配,findall(正则表达式, 字符串),返回的是列表数据类型
# a.  .  : 匹配任意1个字符
# list1 = re.findall(".", "%")
# print(list1)

# b.[]  : 匹配[ ]中列举的字符
# list2 = re.findall("[abcd]", "c")         # ['c']
# list2 = re.findall("[0-9]", "6")            # ['6']
# print(list2)

# c. \d : 匹配数字，即0-9
# list3 = re.findall("\d", "6")
# print(list3)

# d. \s  : 匹配空白，即空格
# list4 = re.findall("\s", " ")
# print(list4)

# e. \w: 匹配非特殊字符，即a-z，A-Z，0-9，_,汉字, \W匹配特殊字符
# list5 = re.findall("\W", "@")       # ['@']
# list5 = re.findall("\w", "我")       # ['我']
# print(list5)




