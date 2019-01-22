# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_02.py
@time: 2019-01-22 23:03

15-2 彩色立方：
给你前面绘制的立方图指定颜色映射

"""
import matplotlib.pyplot as plt

# 显示前5000个整数的立方值
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
# 散点图
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=40)

plt.title("cube_5000", fontsize=24)
plt.xlabel("x_values", fontsize=14)
plt.ylabel("y_values", fontsize=14)

plt.axis([1, 5000, 1, 5000**3])

plt.show()
