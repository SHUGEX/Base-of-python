import re
# 1.  ^  : 匹配字符串开头
# list1 = re.findall("^\d.*", "1abcd")            # ['1abcd']
# print(list1)

# 2.  $  : 匹配字符串结尾
# list2 = re.findall(".*\d$", "abcd4")            # ['abcd4']
# print(list2)

# list2 = re.findall("^\d.*\d$", "3abcd4")            # ['3abcd4']
# print(list2)

# 3. [^指定字符]：除了指定字符以外都匹配
# list3 = re.findall("[^17]", "7")            # [],7是指定字符，所以是空列表
# print(list3)

# 4. |  : 匹配左右任意一个表达式
# list4 = re.findall("1|4|7", "7")            # ['7']
# list4 = re.findall("\d|4|7", "5")            # ['5']
# print(list4)






