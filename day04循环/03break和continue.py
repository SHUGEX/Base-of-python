# 1. break: 遇到break直接退出整个循环
# for i in range(1, 5):
#     # 循环内容
#     if i == 3:
#         break
#     print(f"汤姆跑了第{i}圈")
# 
# # 2. continue:只退出其中一次循环
# for i in range(1, 5):
#     if i == 2 or i == 3:
#         print(f"第{i}个苹果有虫子，不吃了！")
#         continue                 # 退出当前的这一次循环，继续执行下一次循环
#     print(f"汤姆吃了第{i}个苹果")
# 
# # while循环, 注意：遇到continue就需要在前面加个计数器的累加，遇到break直接退出整个循环
# i = 1
# while i <= 4:
#     if i == 2:
#         print(f"第{i}个苹果有虫子，不吃了！")
#         i += 1              # 为了从第二个苹果到第三次循环
#         continue
#     print(f"汤姆吃了第{i}个苹果")
#     i += 1                  # 为了1到4









