# 1. 查找，查找列表中的数据，index(数据),find在列表中不能使用,count()和len()都是可以在列表中用的
namelist = ["maiya", 18, False]
print(namelist.index(18))           # 1，返回下标
print(namelist.index(17))           # 报错

# 按下标查找
# print(namelist[2])          # False

# 2. 判断,判断数据是否在列表序列,写法：数据 in 序列
# print("maiya" in namelist)              # True,判断是否存在
# print("maiya" not in namelist)          # False，判断是否不存在

# namelist = ["maiya", 18, False]
# 3. 增加，增加指定数据到列表中
# 3.1 列表名.append(数据),在列表的结尾进行追加
# namelist.append("女")
# print(namelist)

# 3.2 列表名.extend(数据),如果数据是序列的话，会逐一添加，不是序列，会报错
# namelist.extend("tom")
# namelist.extend(10)         # 报错
# print(namelist)

# 3.3 列表名.insert(下标,数据)，根据下标添加到指定的位置
# namelist.insert(1, "tom")
# print(namelist)
#
# namelist = ["maiya", 18, False, 18]







