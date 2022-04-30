# 1. 算术运算符
# 1.1 +，-，*，/
# print(1 + 1)
# print(1 - 1)
# print(2 * 2)
# print(4 / 2)        # 除法运算中会默认保留一位小数
#
# # 1.2  // : 整除， 取整数部分， % :取余，取余数部分
# print(9 // 4)       # 2
# print(9 % 4)        # 1
#
# print(8 // 3)       # 2
# print(8 % 3)        # 2
#
# # ** ：指数
# print(2 ** 4)           # 4个2= 16
# print(3 ** 3)           # 3个3= 27
# # 优先级：() > ** > *,/,%,// > +,-
# # 有小括号，先算小括号
# print(1 + 2 * 3)        # 7
# print((1 + 2) * 3)      # 9
#
# # 2.赋值运算符：= ，变量 = 值
# # 单个变量赋值，一对一
# num1 = 1
# print(num1)
#
# # 多个变量的赋值，多对多,等号左边的变量和右边的值都是从左至右依次对应, 等号左右两边的个数要相等
#
# name, age, num2 = "maiya", 20, 110
#
# print(name)
# print(age)
# print(num2)
#
# # 多个变量赋相同的值，多对一
# a = 10
# b = a
# b = a = 10      # 更简单
# print(a)
# print(b)
#
# # 3. 比较运算符, 结果都是属于布尔值，要么是False,要么是True
# # ==  :  判断是否相等            !=   :  判断是否不相等
# # >  :  判断是否大于              <    :  判断是否小于
# # >=  :  判断是否大于等于        <=  :  判断是否小于等于
# print(11 == 11)         # True
# print(11 != 11)           # False
#
# # 4. 逻辑运算符,结果都是属于布尔值，要么是False,要么是True
# a = 0
# b = 1
# c = 2
# # and :  True and False, 一假则假，都真才真
# print(表达式 and 表达式)
# print(a < b and c > b)          # True and True  = True
# print(a > b and c > b)          # False and True  = False
#
# # or  :  True or False,一真则真，都假才假
# print(a < b or c > b)           # True
# print(a > b or c > b)           # True
# print(a > b or c < b)           # False
#
# # not :  not True，取反意
# print(not a < b)            # False
# print(not False)            # True
#
# # 5.复合赋值运算符
# # += : 加法赋值运算符
# x = 10
# x += 2      # 等价于x = x + 2
# print(x)            # 12
#
# # *=: 乘法赋值运算符
# x = 3
# x *= 4          # x = x * 4
# print(x)






