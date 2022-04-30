# 转义字符：就是带有功能的字符，用于进行print打印的时候
# 1. \n：换行
# print("hello")          # print在执行打印时自带换行效果
# print("world")
# print("hello")

print("hello\nworld")       # \n写在哪里，哪里就会换行

# 2. \t：制表符---》九九乘法表的数据对齐输出，一个tab键（4个空格）的距离
# print("hello\tworld")           # 放中间空三个
# print("\thelloworld")           # 放前面空四个
# print("helloworld\t")           # 放后面空二个

# 总结：\t会根据放的位置不同，作用出来的空格个数就不同
# """
# ctrl + c    复制
# ctrl + v    粘贴
# ctrl + d    向下复制
# ctrl + z    撤销上一步操作
# ctrl + x    剪切
# """
# 3. print结束符：print(“输出内容”，end=”  ”)
# print(123, end="")          # end=""可以取消print换行的效果
# print(123, end="_")          # end="",在引号中加什么print的输出内容后面就跟什么
# print(456)










