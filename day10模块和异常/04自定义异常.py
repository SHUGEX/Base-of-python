# 自定义异常是在正常的程序中引发错误
# 1.自定义异常语法：异常类型("异常的描述信息")
# 2.抛出异常语法：raise 异常类型("异常的描述信息")
# 需求：定义一个函数，判断输入的密码的长度，如果长度不足，就抛出异常（报错）
# def func1():
#     pwd = input("请输入密码：")           # 字符串
#     if len(pwd) >= 5:
#         return "密码输入成功"             # 退出函数并且返回提示信息
#     else:
#         # 自定义异常，然后抛出异常
#         error = Exception("长度不足，输入失败！")
#         raise error             # 引发报错
#         # print("麦芽")             # 注意：raise后面的代码是无法执行
#
# # print(func1())
#
# # 捕获异常
# try:
#     print(func1())
# except Exception as result:
#     print(result)
#


