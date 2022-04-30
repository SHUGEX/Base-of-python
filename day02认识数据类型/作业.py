# 1、请简述python中数据类型有几种，分别有哪些？
#  答：一共有七种类型，分别有数值(整型int、浮点型float)、布尔型（真True、假False）/字符串str、列表list、元祖tuple、集合set、字典dict。
# 2、请使用多种格式化输出方式编写程序输出下方语句：
# 2020-02-27，体重:65公斤，跑步速度:11公里/小时，跑步时间:20.0分钟，运动距离:3.67公里，燃烧卡路里:297.95千卡。
# time = '2020-02-27'
# weight = 65
# speed = 11
# duration = 20.0
# distance = 3.67
# calorie = 297.95
# print(f'{time}，体重:{weight}公斤，跑步速度:{speed}公里/小时，跑步时间:{duration}分钟，运动距离:{distance}公里，燃烧卡路里:{calorie}千卡。')
# print('%s，体重:%d公斤，跑步速度:%d公里/小时，跑步时间:%.1f分钟，运动距离:%.2f公里，燃烧卡路里:%.2f千卡。' % (time, weight, speed, duration, distance, calorie))
# # 3、请结合输入以及格式化输出的所学知识点，提示用户输入姓名，年龄，体重，学号，并以f格式化输出语句：我的名字是x，今年x岁了，体重x公斤，学号是x。
# name = input('Enter your name:')
# age = int(input('Enter your age:'))
# weight = eval(input('Enter your weight:'))
# stu_id = eval(input('Enter your stu_id'))
# print(f'我的名字是{name}，今年{age}岁了，体重{weight}公斤，学号是{stu_id}')
# # 4. 选择题num=float(input('请输入一个整型数据：')),请问num得到的是一个什么数值类型：( B )
# # A.整型      B.浮点型      C.字符串型   D.任意类型
# 
# print('%s，体重:%d公斤，跑步速度:%d公里/小时，跑步时间:%.1f分钟，运动距离:%.2f公里，燃烧卡路里:%.2f千卡。' % (time, weight, speed, duration, distance, calorie))
# print('%s，' % time, end="")
# print('体重:%d公斤，' %  weight, end="")
# print('跑步速度:%d公里/小时，' % speed, end="")
# print('跑步时间:%.1f分钟，' % duration, end="")
# print('运动距离:%.2f公里，' % distance, end="")
# print('燃烧卡路里:%.2f千卡。' % calorie)
