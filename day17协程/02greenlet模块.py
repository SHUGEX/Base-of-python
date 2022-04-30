# 1. 在解释器设置中,file-->settings-->Project Interpreter-->点击+号--->输入库名，直接点击安装
# 2. 在cmd中,输入pip list查看已经安装好的库，输入pip install 库名
# 3. 使用alt + enter(回车)

# 使用greenlet模块“步骤”：
# 	1.  导入greenlet模块
# from greenlet import greenlet
# import greenlet
# def sing():
#     print("开始唱歌")
#     green2.switch()
#     print("唱歌结束")
#
# def dance():
#     print("开始跳舞")
#     green1.switch()
#     print("跳舞结束")
#
# # 	2.  实例化协程对象
# green1 = greenlet.greenlet(sing)
# green2 = greenlet.greenlet(dance)
#
# # 	3.  调用switch()函数,谁先调用谁先执行，由程序决定
# green2.switch()
# green1.switch()
# # 使用greenlet模块实现的协程是单线程下以并发的执行方式实现的多任务












