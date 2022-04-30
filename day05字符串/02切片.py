# 切片语法：序列名[开始位置下标:结束位置下标:步长],类似于range(开始，结束，步长)
# str1 = "abcdefg"
# print(str1[2:5:1])          # cde，步长是1，注意：切片也是前包后不包
# print(str1[2:5:2])          # ce，步长是2，间隔1个字母取字符
#
# str2 = "0123456789"
# # 拿出字符串的一部分--->234
# print(str2[2:5])            # 234,步长不写，默认是1
# print(str2[:5])                 # 01234,开始位置不写，默认从下标为0选取
# print(str2[2:])                 # 23456789,结束位置不写，默认选取到最后字符
# print(str2[:])                 # 0123456789,开始和结束位置不写，默认选取所有
#
# # 步长为负数
# print(str2[::-1])           # 9876543210,当步长是负数，就会倒序选取字符
# print(str2[::-2])           # 97531,当步长是负数，就会倒序选取字符

# 总结：步长表示间隔，正数步长是正序，负数步长是逆序
# 切片有两个选取方向：1.开始到结束（从左到右），2.步长是负数（从右至左），方向冲突，没有执行效果















