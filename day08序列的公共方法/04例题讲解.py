# 购物车: 将商品添加到购物车中，实现步骤如下：
# （1）已知商品列表中有商品的名称和价格：
# goods = [['Iphone', 10888], ['MacPro', 14800], ["小米10", 3999], ['Coffee', 32], ['book', 80], ['Nike Shoes', 899]]
# （2）用户通过输入序号将商品添加到购物车中，商品列表需要循环刷新以便购物车可以不断购入同一商品（可用enumerate显示序号)
"""
解题思路：
    1. 准备数据：已知商品列表 和 定义购物车空列表
    2. 循环遍历商品列表，获取每一个商品，然后让商品一直呈现给用户看：商品----》属性（序号，名称，价格）
    3. 使用input接收用户输入的序号，根据序号把对应的商品添加到购物车列表
    4. 购物车的功能：a. 把商品添加到购物车， b. 查看购物车， c. 输入序号错误，提示商品不存在
"""
# 商品列表
# goods = [['Iphone', 10888], ['MacPro', 14800], ["小米10", 3999], ['Coffee', 32], ['book', 80], ['NikeShoes', 899]]
# shopping_list = []           # 购物车列表
# while True:                 # 加入死循环让商品列表重复呈现
#     print("---------商品列表---------")
#     for i, j in enumerate(goods, start=1):       # 把enumerate返回的元组，使用两个变量保存，进行了拆包,i保存序号，j保存是商品也就是子列表
#         print(f"{i}.{j[0]}\n\t\t\t ----${j[1]}")
#     num = input("请输入需要购物的商品序号（用空格隔开）：").split(" ")
#     n = 0
#     f = 0
#     for k in num:
#         n += 1
#         if k.isdigit() and (0 < int(k) < 7):          # isdigit是判断输入的序号是否是数字，并且是1-6的数字范围
#             # 将商品添加到购物车
#             shopping_list.append(goods[int(k)-1])         # num-1是为了让这个序号和列表中的默认下标对应上
#             x, y = goods[int(k)-1]
#             f += y
#             print(f"{n}.{x}\n\t\t\t ----${y}")
#         else:
#             print("您输入的序号错误！")
#     print(f"\t\t共{n}件商品已经添加到购物车！共计{f}元")
#     r = input("输入1继续选购，输入0清空购物车：")
#     if r == '1':
#         continue
#     elif r == '0':
#         break
#     else:
#         print("您输入的序号错误！")
# print("您的购物车有:")
# for i, j in enumerate(shopping_list, start=1):
#     print(f"{i}.{j[0]}\n\t\t\t ----${j[1]}")
# print(f"\t\t\t----共消费{f}元")
#
#










