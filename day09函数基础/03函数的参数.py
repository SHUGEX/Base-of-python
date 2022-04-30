# 序列名.count(数据)，需要给进去一个数据，才能返回这个数据出现的次数给我们
# 1. 位置参数: 调用函数时根据函数定义的参数位置来传递参数
# 需求：定义一个函数，函数有3个参数name,age,gender
# def user_info(name, age, gender):
#     print(f"您的名字是{name}，年龄是{age},性别是{gender}")
# # #
# # # # 调用函数
# user_info("maiya", 18, "女")         # 需要放实参，个数和位置需要和形参一一对应,否则报错
# #
# # # 2.关键字参数: 函数调用时通过"键”=“值”形式加以指定。可以让函数更加清晰、容易使用。
# def user_info(name, age, gender):
#     print(f"您的名字是{name}，年龄是{age},性别是{gender}")
# #
# # # 调用函数
# user_info(name="maiya", 18, "女")            # 报错，因为位置参数要写在关键字前面
# user_info("maiya", 18, gender="女")
# #
# # # 3. 缺省参数: 也叫默认参数，为参数提供默认值，调用函数时可不传该默认参数的值
# def user_info(name, age, gender="女"):
#     print(f"您的名字是{name}，年龄是{age},性别是{gender}")
#
# user_info("maiya", 18)                            # 没有第三个实参，会直接使用默认值
# user_info("maiya", 18, gender="男")                  # 有第三个实参，会修改默认值
#
# # 4. 不定长参数︰ 也叫可变参数，用于不确定会传递多少个参数的时候，
# # 可用来包裹位置参数,返回的就是元组类型
# def user_info(*args):
#     print(args)             # (1, 3, 4)
# #
# #
# user_info(1)
# user_info(1, 3, 4)
# user_info()
#
# # # 包裹关键字参数来进行参数传递,返回的是字典类型
# def user_info(**kwargs):
#     print(kwargs)
#
# user_info(name="maiya")
# user_info(name="maiya", age=18)
# user_info()
#
#
#








