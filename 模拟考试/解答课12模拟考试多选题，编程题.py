# 二、多选题，三分一个，共10题，少选多选错选都不得分（30分）
# 1.以下选项中属于Python 语言的关键字的是（acd ）
# A. except  B. do  C. pass  D. import
# pass = 1
# print(pass)
# print = 1
# do = 1
# print(do)

# 2.在列表中添加元素的方法有哪些？ ( ab  )
# A． append()
# B． insert()
# C． tuple()
# D． add()
# list1 = [1,2]
# list1.append(1)     # 末尾进行添加
# print(list1)

# list1.insert(1,6)       # insert(下标，元素)
# print(list1)

# a = tuple()         # 创建一个空的元组
# print(a)

# add():集合的添加
# set1 = set()
# set1.add('123')       # 作为一个整体进行添加
# print(set1)


# 3 以下关于字典，描述正确的是？（ abcd ）
# A． 与键相关联的值可以任何 Python 对象，比如数字、 字符串、 列表甚至是字典。
# B． 使用 delete 语句指定字典名和要删除的键，即可删除字典或者键值对。
# C． 可以先使用一对空的花括号，定义一个空字典， 然后再分行添加键值对。
# D． 可以指定字典名、 用方括号括起的键以及与该键相关联的新值，来修改字典值。
# dict1 = {}
# dict1[1] = {1:2}
# print(dict1)

# 删除字典
# del dict1
# print(dict1)

# 删除键值对
# del dict1[2]
# print(dict1)

# dict1[1] = 1
# print(dict1)
# 没有就添加，有就修改

# 4.关于实参与形参，以下描述正确的是？（ac ）
# A． 位置实参指的是，实参的顺序与形参相同。
# B． 位置实参与参数顺序无关。
# C． 关键字实参指的是：传递给函数的是 “名称=值对” 。这样在调用函数时就不用考虑实参顺序，
# 而且还可以清楚地指出实参各个值的用途。
# D． 使用关键字实参时， 必须准确地指出定义中的形参名。
# def func(**kwargs):
#     print(kwargs)
#
#
# func(a=1)

# 5.下面说法正确的是： （acd ）
# A.所有程序错误都可以用异常控制、解决
# B.引发一个不存在索引的列表元素会引发 NameError 错误
# C.异常是程序的执行过程中用来解决错误、避免直接终止程序运行的手段
# D.捕获所有异常可以使用Exception
# try:
#     a
# except Exception as e:
#     print(e)
# print(11)

# a = '123'
# print(a[6])


# 6.关于继承，说法正确的是：（bc  ）
# A.继承的概念：子类拥有父类的所有方法和属性
# B.继承分为单继承和多继承
# C.面向对象三特性：封装、继承、多态
# D.子类可以拥有多个父类，如果子类和父类的方法名相同，则默认使用父类的


# 7.下面说法正确的是： (cd  )
# A. __init__是创建实例对象的方法
# B. Test是类名, 里面有一个funa实例方法， 可以通过Test.funa()调用
# C. 类属性在内存中只保存一份，实例属性在每个实例对象中都保存一份
# D. 对象可以通过打点去调用对应的属性或方法
# class Test(object):
#     a1 = 1
#     def funa(self):
#         print(123)
#
#
# a = Test()
# a.funa()
# print(Test.a1)
# print(a.a1)

# 8.下列说法正确的是  （ abcd ）
# A. 继承中，子类的同名方法会覆盖父类的同名方法
# B. 在属性前加上两个下划线，表示这是私有属性，不能在类的外部调用
# C. 类方法和静态方法都可以通过类对象和实例对象调用
# D. 在子类方法和父类方法同名时，可以使用super重写实现在子类中调用父类同名方法
# class A(object):
#     @staticmethod
#     def test():
#         print('我是静态方法')
#
#     @classmethod
#     def test2(cls):     # cls接受类和对象
#         print('我是类方法')
#
# A.test()
# A.test2()
# a = A()
# a.test()
# a.test2()


# 9.下列有关python文件操作，打开一个文件的参数描述正确的有：( abc )
# A： r：只读模式，文件的指针将会放在文件的开头
# B： w：只写模式，若有内容则覆盖原有内容，如果该文件不存在，创建新文件
# C： a：打开文件，并将内容追加到文件末尾，如果该文件不存在，创建新文件进行追加写入
# D： ab: 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头

# 10.在 Python 中有哪些方式可以实现多任务? ( abcd )
# A. multiprocessing
# B. threading
# C. gevent
# D. Yield

# 1. 已知一个数字列表list1 =[59,23,56,78,90,234,64,12,9]，求列表中所有元素和（10分）
# 方法1
# list1 =[59,23,56,78,90,234,64,12,9]
# sum1 = 0
# for i in list1:
#     sum1 += i
# print(sum1)

# 方法2：
# list1 =[59,23,56,78,90,234,64,12,9]
# print(sum(list1))


# 2. 写一个test1函数，返回三个数（从键盘输入的整数）中的最大值，最小值，平均值（10分）
# list1 = []
# def test1():
#     for i in range(3):
#         list1.append(int(input('输入数：')))
#     return max(list1),min(list1),sum(list1)/3
#
#
# a = test1()
# print(f'最大值是{a[0]},最小值{a[1]},平均值{a[2]}')


# 3. 定义一个四边形类，用来判断四边形的类型并且计算面积，四边形类有长、宽两个属性
# 根据用户输入的值来决定该四边形的类型（长方形长大于宽或者宽大于长，正方形则长宽相等）
# 以及计算最后的面积是多少，提示：面积 = 长x宽（10分）
# class SiBianXin(object):
#     def __init__(self,width,long):
#         self.width = width
#         self.long = long
#
#     def __str__(self):
#         if self.width == self.long:
#             mianji = self.long * self.width
#             return f'四边形是正方形，面积是{mianji}'
#         else:
#             mianji = self.long * self.width
#             return f'四边形是长方形，面积是{mianji}'
#
# a = SiBianXin(2,2)
# print(a)


# 4. 文件操作，新建一个txt文本，文本中有任意行的数据，请结合文件操作等所学知识实现逐行读取内容，
# 当没有内容可供读取时不再读取的效果。
# file = open(r'text.txt','r',encoding='utf-8')
# # print(file.readlines())
# for i in file.readlines():
#     print(i,end='')
# file.close()

# 5.已知字符串s = " Listen Obligte Valued Excuse"，找出字符串的规律，使用正则表达式匹配出每个单词的首字母。
import re
# s = " Listen Obligte Valued Excuse"
# print(re.findall('[A-Z]',s))

# s = "listen obligte valued excuse"
# print(re.findall('[a-z]',s))
# list1 = s.split(' ')
# list2 = []
# for i in list1:
#     # print(i[0])
#     list2.append(re.findall('^[a-z]',i))
#
#
# print(list2)



# s = "listen obligte valued excuse"
# list1 = s.split(' ')
# list2 = []
# for i in list1:
#     # print(i[0])
#     list2.append(re.match('[A-Za-z]',i).group())
#
# print(list2)




