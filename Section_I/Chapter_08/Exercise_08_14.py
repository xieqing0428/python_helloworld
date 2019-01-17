# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_08_14.py
@time: 2019-01-17 21:13

8-14 汽车：
编写一个函数，将一辆汽车的信息存储在一个字典中。
这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。
这个函数必须能够像下面这样进行调用：

car = make_car('subaru', 'outback', color='blue', tow_package=True)

打印返回的字典，确认正确地处理了所有的信息。

"""
cars = {}


def make_car(manufacturer, type_no, **other_info):
    """存储车辆信息"""

    cars['制造商'] = manufacturer
    cars['型号'] = type_no
    for key, value in other_info.items():
        cars[key] = value
    return cars


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
