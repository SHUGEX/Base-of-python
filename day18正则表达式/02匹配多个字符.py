# import re
# list1 = re.findall(".", "123")
# print(list1)

# 1. * : 作用在前一个字符，使前一个字符匹配的次数是0次或者无限次
# list2 = re.findall(".*", "10")
# list2 = re.findall("[a-z]*", "abc123abc")
# list2 = re.findall("yes*", "yesssss")
# list2 = re.findall("yes*", "ye")                # ['ye']
# print(list2)

# 2. +  : 作用在前一个字符，使前一个字符出现1次或者无限次
# list3 = re.findall("yes+", "ye")            # [], s至少要出现一次
# print(list3)

# 3. ? : 匹配前一个字符出现1次或者0次﹐即要么有1次﹐要么没有
# list4 = re.findall("https?", "http")            # ['http']
# print(list4)

# 4. {m} : 匹配前一个字符出现m次
# list5 = re.findall("yes{2}", "yess")            # ['yess']
# list5 = re.findall("yes{2}", "yes")            # []
# print(list5)

# 5. {m,n} : 匹配前一个字符出现从m到n次,m是最小次数，n是最多次数
# list6 = re.findall("yes{2,5}", "yess")              # ['yess']
# list6 = re.findall("yes{2,5}", "yessssss")              # ['yesssss']
# print(list6)

# list7 = re.findall(".{2,5}", "4aC*")            # ['4aC*']
# print(list7)







