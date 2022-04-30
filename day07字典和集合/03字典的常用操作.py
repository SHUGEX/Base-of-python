# list1 = ["maiya", "女", 18]
# 单独取"女"数据怎么取？ 下标
# print(list1[1])                     # 女
# list1.insert(1, 100)            # 对列表中的数据进行修改
# print(list1)
# print(list1[1])

# 字典的数据是一个一个的键值对
# 1. 字典的格式:  {"name" : "Tom","age" : 20,"gender" : "男"}
# 定义有数据的字典：1.符号为大括号，2.数据为键值对形式出现，3.各个键值对之间用逗号隔开
# dict1 = {"name": "maiya", "age": 18}
# print(type(dict1))          # dict

# 2. 定义空字典
# dict2 = {}
# print(type(dict2))          # dict

# 3. 字典的常用操作
# dict2 = {"name": "maiya", "age": 18}
# 增加，写法:字典序列[key]=值, num 的值是110，key = 键， value = 值
# dict2["num"] = 110
# print(dict2)            # {'name': 'maiya', 'age': 18, 'num': 110},靠key添加一个键值对

# 修改，写法:字典序列[key]=值
# dict2["name"] = "tom"
# print(dict2)              # key不存在是添加，存在是修改

# dict3 = {"name": "maiya", "age": 18}
# 删除，del，clear
# dict3.clear()
# print(dict3)            # 清空字典

# 删除整个字典
# del dict3
# print(dict3)        # 报错
#
# # 删除一个键值对，靠key
# del dict3["age"]
# print(dict3)                # {'name': 'maiya'}
#
# dict4 = {"name": "maiya", "age": 18}
# # 查找
# # 1. 按key值查找
# print(dict4["age"])         # 通过键去获取值
#
# # 2. get(),获取Key对应的值
# print(dict4.get("name"))        # maiya,返回key对应的值
#
# # 3. keys():查找字典中所有的key,返回是列表，保存了所有的key
# print(dict4.keys())
#
# # 4. values():查找字典中所有的value,返回是列表，保存了所有的value
# print(dict4.values())
#
# # 5. items():查找字典中所有的键值对,返回是列表，保存了所有的键值对
# print(dict4.items())






