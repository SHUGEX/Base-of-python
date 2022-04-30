# str1 = "hello world and maiya and python"           # 空格算字符
# 1.   find(): 检测某个子串是否包含在这个字符串中
# 语法  : 字符串序列.find(子串，开始位置下标,结束位置下标),功能函数都是打点调用
# print(str1.find("and"))               # 12,有的话返回下标
# print(str1.find("and", 15, 30))         # 22，有了开始和结束，就是在限制查找的范围
# print(str1.find("ands"))              # -1,没有的话返回-1

# 2.   index(): 和find()调用方式和功能相同。
# print(str1.index("and"))         # 12
# print(str1.index("ands"))        # 找不到，一个报错

# 3.   count(): 返回某个子串在字符串中出现的次数。
# print(str1.count("and"))            # 2

# 4.   len(): 返回字符串中字符的个数, 语法：len(序列名)
# print(len(str1))            # 32, 总的字符个数










