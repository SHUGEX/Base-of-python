# “需求”：警务人员和警犬一起工作，警犬分2种:追击敌人和追查毒品，警务人员携带不同的警犬，执行不同的工作
# 多态指的是一类事物有多种形态，一个抽象类有多个子类
# # 1. 人类，2. 警犬类， 3.追击敌人警犬类， 4. 追查毒品警犬类
# class Person(object):
#     # 定义方法：带不同的狗执行不同的工作
#     def work_with_dog(self, dog):                # self接收的是tom,dog接收到的ad
#         # dog.sleep()
#         dog.work()
#
# class Dog(object):
#     pass
#
# # 定义追击敌人的警犬
# class ArmyDog(Dog):
#     def work(self):
#         print("追击敌人！")
#     def sleep(self):
#         print("狗狗在睡觉！")
#
# # 定义追查毒品的警犬
# class DrugDog(Dog):
#     def work(self):
#         print("追查毒品！")
#
# # 通过类去创建对象
# tom = Person()
# ad = ArmyDog()
# dd = DrugDog()
#
# tom.work_with_dog(dd)             # 人带狗执行工作:把狗这个对象作为实参传到实例方法的形参中









