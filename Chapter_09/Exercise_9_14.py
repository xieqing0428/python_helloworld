# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_9_14.py
@time: 2019-01-13 16:31

9-14 骰子：
模块random包含以各种方式生成随机数的函数，其中的randint()返回一个位于指定范围内的整数，
例如，下面的代码返回一个1~6内的整数：

from random import randint
x = randint(1, 6)

请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。
创建一个6面的骰子，再掷10次。
创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。

"""

from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(str(self.sides) + '面骰本次摇出的数值为' + str(randint(1, self.sides)))


die6 = Die()
for num in range(10):
    print("第" + str(num + 1) + "次：")
    die6.roll_die()


die10 = Die(10)
for num in range(10):
    print("第" + str(num + 1) + "次：")
    die10.roll_die()


die20 = Die(20)
for num in range(10):
    print("第" + str(num + 1) + "次：")
    die20.roll_die()

