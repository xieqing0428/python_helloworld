# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_15_01.py
@time: 2019-01-22 22:53

15-1 立方：
数字的三次方被称为其立方。
请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。

"""
import matplotlib.pyplot as plt

# 显示前5个整数的立方值
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
# 折线图
plt.plot(x_values, y_values, linewidth=5)

plt.title("cube_5", fontsize=24)
plt.xlabel("x_values", fontsize=14)
plt.ylabel("y_values", fontsize=14)

plt.tick_params(axis="both", labelsize=14)

plt.show()

# 显示前5000个整数的立方值
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
# 散点图
plt.scatter(x_values, y_values, s=40)

plt.title("cube_5000", fontsize=24)
plt.xlabel("x_values", fontsize=14)
plt.ylabel("y_values", fontsize=14)

plt.axis([1, 5000, 1, 5000**3])

plt.show()
