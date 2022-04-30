# 一、单选题，一个2分，共10个，选错不得分（20分）
# 1.判断下列变量名哪些不符合规范：（ D ）
# A.info_print1
# B._name
# C.true
# D. 3_password

# 2.在使用格式化输出”我的名字是tom,今年18岁，我的体重是75.5公斤，学号是001”，下列输出正确的是（ C ）
# A.print("我的名字是%s,今年%d岁了，体重%f公斤，学号是%03d" % (name, age, weight, stu_id))
# B.print("我的名字是%s,今年%d岁了，体重%.1f公斤，学号是%d" % (name, age, weight, stu_id))
# C.print("我的名字是%s,今年%d岁了，体重%.1f公斤，学号是%03d" % (name, age, weight, stu_id))
# D.print("我的名字是%s,今年%s岁了，体重%s公斤，学号是%s" % (name, age, weight, stu_id))

# 3.示例：list1=['pink', 'blue', 'yellow']，我们在使用列表时，以下哪个选项，会引起索引错误？（ D  ）
# A． list1[-1]
# B． list1[-2]
# C． list1[0]
# D． list1[3]
#
# 4.下面的代码会输出什么（ C ）
# s = "hello python"
# b = s.split("o")
# print(b)
# A. ['hell', '', ' pyth', 'n']
# B. ['hell', '', ' pyth', '', 'n']
# C. ['hell', ' pyth', 'n']
# D. ['hell', '', 'pyth', 'n']
#
# 5.以下说法正确的是：（ C ）
# A.while循环不可以和for循环嵌套使用
# B.if条件表达式后不一定要使用冒号
# C.如果只是控制循环次数, for i in range(20)和for i in range(20, 40)的作用是一样的
# D.continue可以用于单独的if判断中
#
# 6. 代码list1 = [1, 2, [3, 4]],执行print(list1[2][1])的结果是（ D ）
# A. 1      B. 2        C. 3        D. 4
#
# 7. 关于函数，下列说法中不正确的是：( D )
# A. 函数就是一段封装好的代码
# B. 函数能够实现代码的重用
# C. 函数可以有多个值返回
# D. 函数的位置参数可以随意传递，不用按照顺序传值
#
# 8.关于面向对象的说法中，不正确的是( D )
# A. __init__方法没有返回值
# B. __str__方法必须有返回值
# C. 对象是由类创建出来的，对象是类的实例
# D. 对象可以决定类的属性

# 9. 关于 python 类继承，下列描述错误的是 （ B ）
# A．继承分为单继承和多继承。
# B．对于继承而来的父类方法，子类不可以重写。
# C．子类可以拥有多个父类，并且具有所有父类的属性和方法。
# D．子类除了拥有继承父类而来的属性和方法之外，还可以自定义子类自己的属性和方法。

# 10.下列关于多线程共享数据描述错误的是? ( D )
# A. 多线程之间可以进行数据的共享
# B. 多线程程序可以通过全局变量实现数据的共享
# C. 多线程在使用全局变量共享数据时, 可能会出现问题
# D. 多线程可以使用线程异步解决共享数据时出现的问题
#
# 二、多选题，三分一个，共10题，少选多选错选都不得分（30分）
# 1.以下选项中属于Python 语言的关键字的是（ACD ）
# A. except  B. do  C. pass  D. import
#
# 2.在列表中添加元素的方法有哪些？ (  AB )
# A． append()
# B． insert()
# C． tuple()
# D． add()

# 3 以下关于字典，描述正确的是？（ ABCD ）
# A． 与键相关联的值可以任何 Python 对象，比如数字、 字符串、 列表甚至是字典。
# B． 使用 delete 语句指定字典名和要删除的键，即可删除字典或者键值对。
# C． 可以先使用一对空的花括号，定义一个空字典， 然后再分行添加键值对。
# D． 可以指定字典名、 用方括号括起的键以及与该键相关联的新值，来修改字典值。
#
# 4.关于实参与形参，以下描述正确的是？（ ACD）
# A． 位置实参指的是，实参的顺序与形参相同。
# B． 位置实参与参数顺序无关。
# C． 关键字实参指的是：传递给函数的是 “名称-值对” 。这样在调用函数时就不用考虑实参顺序， 而且还可以清楚地指出实参各个值的用途。
# D． 使用关键字实参时， 必须准确地指出定义中的形参名。
#
# 5.下面说法正确的是： （ACD ）
# A.所有程序错误都可以用异常控制、解决
# B.引发一个不存在索引的列表元素会引发 NameError 错误
# C.异常是程序的执行过程中用来解决错误、避免直接终止程序运行的手段
# D.捕获所有异常可以使用Exception
#
# 6.关于继承，说法正确的是：（ ABC ）
# A.继承的概念：子类拥有父类的所有方法和属性
# B.继承分为单继承和多继承
# C.面向对象三特性：封装、继承、多态
# D.子类可以拥有多个父类，如果子类和父类的方法名相同，则默认使用父类的

# 7.下面说法正确的是： ( CD )
# A. __init__是创建实例对象的方法
# B. Test是类名, 里面有一个funa实例方法， 可以通过Test.funa()调用
# C. 类属性在内存中只保存一份，实例属性在每个实例对象中都保存一份
# D. 对象可以通过打点去调用对应的属性或方法

# 8.下列说法正确的是  （ ABCD）
# A. 继承中，子类的同名方法会覆盖父类的同名方法
# B. 在属性前加上两个下划线，表示这是私有属性，不能在类的外部调用
# C. 类方法和静态方法都可以通过类对象和实例对象调用
# D. 在子类方法和父类方法同名时，可以使用super重写实现在子类中调用父类同名方法

# 9.下列有关python文件操作，打开一个文件的参数描述正确的有：( ABC )
# A： r：只读模式，文件的指针将会放在文件的开头
# B： w：只写模式，若有内容则覆盖原有内容，如果该文件不存在，创建新文件
# C： a：打开文件，并将内容追加到文件末尾，如果该文件不存在，创建新文件进行追加写入
# D： ab: 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头

# 10.在 Python 中有哪些方式可以实现多任务? ( ABCD )
# A. multiprocessing
# B. threading
# C. gevent
# D. Yield

# 1. 已知一个数字列表list1 =[59,23,56,78,90,234,64,12,9]，求列表中所有元素和（10分）
# 方法一
# list1 = [59, 23, 56, 78, 90, 234, 64, 12, 9]
# sum1 = 0
# for i in range(0, len(list1)):
#     sum1 += list1[i]
# print(sum1)

# 方法二
# list1 = [59, 23, 56, 78, 90, 234, 64, 12, 9]
# print(sum(list1))

# 2. 写一个test1函数，返回三个数（从键盘输入的整数）中的最大值，最小值，平均值（10分）
# list1 = []
# def test1():
#     for i in range(3):
#         list1.append(int(input("请输入第一个整数：\n")))
#     return max(list1), min(list1), sum(list1)/3
# zhi = test1()
# print(f"最大值,最小值，平均值分别是：{zhi[0]},{zhi[1]},{zhi[2]}")

# 3. 定义一个四边形类，用来判断四边形的类型并且计算面积，四边形类有长、宽两个属性
# 根据用户输入的值来决定该四边形的类型（长方形长大于宽或者宽大于长，正方形则长宽相等）
# 以及计算最后的面积是多少，提示：面积 = 长x宽（10分）
# class Sibianxing(object):
#     def __init__(self, long, width):
#         self.long = long
#         self.width = width
#
#     def __str__(self):
#         if (self.long > self.width) or (self.width > self.long):
#             self.mianji = self.long * self.width
#             return f"该四边形的长是：{self.long},宽是：{self.width},面积是:{self.mianji},是一个长方形！"
#         else:
#             self.mianji = self.long * self.width
#             return f"该四边形的长是：{self.long},宽是：{self.width},面积是:{self.mianji},是一个正方形！"
# juxing1 = Sibianxing(4, 5)
# print(juxing1)

# 4. 文件操作，新建一个txt文本，文本中有任意行的数据，请结合文件操作等所学知识实现逐行读取内容，当没有内容可供读取时不再读取的效果。
# file = open('test.txt', 'r', encoding='utf-8')
#
# for i in range(len(file.readlines())):
#     if i == 0:
#         file = open('test.txt', 'r', encoding='utf-8')
#     print(file.readline())
# file.close()

# 5.已知字符串s = " Listen Obligte Valued Excuse"，找出字符串的规律，使用正则表达式匹配出每个单词的首字母。
# import re
# a = " Listen Obligte Valued Excuse"
# # 方法一
# list2 = []
# list1 = re.findall(" .", a)
# for i in list1:
#     for j in i:
#         if j.isspace() == True:
#             b = i.replace(j, "")
#             list2.append(b)
# print(list2)
# # 方法二
# list3 = re.findall(r"\b[A-Z]", a)
# print(list3)
