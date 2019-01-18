# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_04_05.py
@time: 2019-01-15 11:32

4-5 计算1~1 000 000的总和：
创建一个列表，其中包含数字1~1 000 000，
再使用min()和max()核实该列表确实是从1开始，到1 000 000结束的。
另外，对这个列表调用函数sum()，看看Python将一百万个数字相加需要多长时间

"""
values = [value for value in range(1, 1000001)]
print("最小值是：" + str(min(values)))
print("最大值是：" + str(max(values)))
print("总和是：" + str(sum(values)))
