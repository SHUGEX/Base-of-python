# 格式：{key1:value1，key2:value2.....}
# 数据以键值对的形式出现的

# 增加        通过key进行添加
# dict1 = {'name':'简单','age' : 18}
# dict1['sex'] = 'man'
# print(dict1)
#
# # # 修改        通过key进行修改
# dict1 = {'name':'简单','age' : 18}
# dict1['name'] = 'maiya'
# print(dict1)
# # 增加和修改的方法是有一样的，key没有就是添加，有就是修改
#
# # 删除
# # del
# # 删除整个字典
# dict1 = {'name':'简单','age' : 18}
# del dict1
# print(dict1)
#
# # 删除一个键
# del dict1['name']
# print(dict1)
#
# # 查找
# # 1.按key进行查找
# dict1 = {'name':'简单','age' : 18}
# print(dict1['name'])
#
# # # get按key进行查找
#
# dict1 = {'name':'简单','age' : 18}
# print(dict1.get('name'))
#
# # 如果出现连两个相同的key，查找会输出最后定义的那个值
# dict1 = {'name':'简单','age' : 18,'name':'jiandan'}
# print(dict1.get('name'))

