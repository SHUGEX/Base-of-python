# 1、“需求”：批量修改文件名，既可添加指定字符串，又能删除指定字符串，添加前缀python_。
# import os   # 导入模块

# 文件批量重命名的前提：重命名的代码文件和被重命名的文件必须在同级文件之下
# listdir(路径):返回一个列表,数据是字符串型的
# file = os.listdir(r'')
# print(file)

# choose = input("请选择：1.添加，2.删除")
# # input('请输入添加或者是删除的内容')
# # 添加
# if choose == '1':
#     for i in file:
#         # print(i)
#         # 添加前缀python_  :使用字符串的拼接
#         new_name = "python_" + i
#         #重命名：os.rename(旧的文件名，新的文件名)
#         os.rename(i,new_name)
#
# # 删除
# if choose == '2':
#     for i in file:
#         # 删除前缀python_:使用切片获取python_后面字符作为文件名
#         a = len('python_')      # _的下标是：长度-1
#         new_name = i[a:]
#         os.rename(i, new_name)





