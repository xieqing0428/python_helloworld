# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: employees.py
@time: 2019-01-14 16:48

编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。

"""


class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, plus=5000):
        return self.salary + plus


