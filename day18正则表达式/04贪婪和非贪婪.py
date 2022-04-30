# import re
# list1 = re.findall("ab*c", "abbbbbc")           # ['abbbbbc']
# print(list1)

# 有多少字符就取多少字符的匹配就是所谓的贪婪匹配

# 非贪婪匹配：越少越好，尽可能拿最少的字符
# list2 = re.findall("ab{2,5}", "abbbb")          # ['abbbb'],贪婪模式
# list2 = re.findall("ab{2,5}?", "abbbb")            # ['abb'], 非贪婪模式，需要用?
# print(list2)

# list3 = re.findall("ab*", "abbbb")              # ['abbbb']
# list3 = re.findall("ab*?", "abbbb")              # ['a'],取最少次0次
# list3 = re.findall("ab+?", "abbbb")              # ['ab'],取最少次1次
# print(list3)

# 原生字符串
# \n换行，\t空格，\转义,一个\转义后面的字符，两个\就是取消转义
# print("hello\\nworld")                    # hello\nworld
# print("C:\\Users\\86132\\Desktop\\project\\day18正则表达式\\04贪婪和非贪婪.py")
# print(r"C:\Users\86132\Desktop\project\day18正则表达式\04贪婪和非贪婪.py")
# print(r"hello\tworld")                      # 通过r可以取消掉\带来的转义效果


# 基础测试，分数，60分及以上安排爬虫课
# 不及格---》根据自身情况安排补习班，，有针对性的去补习，安排爬虫班
# 缺失一块知识点---》1. 自己根据录播自学，学完整个课程去参加测试
                    # 2. 根据自身学习进度情况重新进入新的班级，跟着直播学完整个课程去参加测试







