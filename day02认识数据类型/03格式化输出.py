# %s --->字符串，%d---> 整型， %f --->浮点型
# 1. 需求：输出"今年我的年龄是x岁"
# age = 18
# print("今年我的年龄是%d岁" % age)

# 2. 我的名字是x
# name = "maiya"
# print("我的名字是%s" % name)

# 3. 我的体重是x公斤
# weight = 45.5
# print("我的体重是%f公斤" % weight)         # 默认保留6位小数
# print("我的体重是%.1f公斤" % weight)       # 保留1位小数


# 需求：我的名字是x,年龄是x岁，体重是x公斤
# 格式化符号输出，更加精确
# print("我的名字是%s,年龄是%d岁，体重是%.1f公斤" % (name, age, weight))
# print("我的名字是%s,年龄是%d岁，体重是%.1f公斤" % (age, name, weight))       # 错误，变量顺序不能乱

# # f格式化输出----》语法：f”{变量}”,更加高效，简洁
# print(f"我的名字是{name},年龄是{age}岁，体重是{weight}公斤")








