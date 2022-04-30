# # 1、自定义一个列表，并使用for循环遍历出列表中的元素。
# abc = ['a', 'b', 'c', 'd', 'e', 'f']
# for i in abc:
#     print(i, end=' -> ')
# j = 0
# while j < len(abc):
#     print(abc[j], end=' -> ')
#     j += 1
#
#
# # # 2、 比较两个列表中的元素，找出不相同的元素并保存到列表L3中,已知下方列表L1和L2:
# L1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# L2 = ["Sun", "Mon", "Tue", "Tue", "Thu", "Sat", "AD"]
# L3 = []
# for i in L1:
#     if i not in L2:
#         L3.append(i)
# print('\n', L3)
# for i in L2:
#     if i not in L1:
#         L3.append(i)
# print('\n', L3)
#
# L11 = set(L1)
# L22 = set(L2)
# L33 = list(L11 ^ L22)
# print('\n', L33)
