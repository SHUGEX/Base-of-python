# 4.删除，删除列表中的指定数据，del pop remove clear
# # 4.1 del 删除目标
# namelist = ["maiya", 18, False, 18]
# del namelist[1]
# print(namelist)
#
# # 4.2 列表名.pop(下标)，根据下标去删除,返回被删除的数据, 不写下标，默认删除最后一个
# name = namelist.pop()
# print(name)         # False
# print(namelist)
#
# # 4.3 列表名.remove(数据),删除列表中的第一个匹配项
# namelist.remove(18)
# print(namelist)
#
# # 4.4 列表名.clear(),清空列表中的数据
# namelist.clear()
# print(namelist)
#
# namelist = ["maiya", 18, False, 18]
# # 5. 修改，修改列表中的指定数据，根据下标修改
# namelist[2] = True          # 通过赋值覆盖原来的数据
# print(namelist)
#
# namelist[1] = 20
# print(namelist)
