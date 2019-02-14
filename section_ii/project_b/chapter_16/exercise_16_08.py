# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_08.py
@time: 2019-01-25 23:20

16-8 尝试Python数据科学工具：
虽然Python标准库对数据分析的支持相对有限，
但是Python具有非常完善的数据科学生态系统，
有许多易学易用、高效便捷的第三方开源数据分析工具。
除了前面介绍的matplotlib，
还有科学计算工具包Numpy（http://www.numpy.org/）
/Scipy（https://www.scipy.org/）、
快速数据分析工具Pandas（https://pandas.pydata.org/）、
机器学习工具Scikit-learn（http://scikit-learn.org），
以及让深度学习开发更简单的Keras（https://keras.io/，
它支持TensorFlow、CNTK和Theano）。
如果感兴趣，可以用Pandas直接读取JSON文件数据，
并进行格式转换、数据聚合、时间序列分析，
结合Scikit-learn可以对收盘价进行回归分析与预测

"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

experiences = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
salaries = np.array(
    [103100, 104900, 106800, 108700, 110400, 112300, 114200, 116100, 117800,
     119700, 121600])

# 将特征数据集分为训练集和测试集，除了最后 4 个作为测试用例，其他都用于训练
X_train = experiences[:7]
X_train = X_train.reshape(-1, 1)
X_test = experiences[7:]
X_test = X_test.reshape(-1, 1)

# 把目标数据（特征对应的真实值）也分为训练集和测试集
y_train = salaries[:7]
y_test = salaries[7:]

# 创建线性回归模型
regr = linear_model.LinearRegression()

# 用训练集训练模型——看就这么简单，一行搞定训练过程
regr.fit(X_train, y_train)

# 用训练得出的模型进行预测
diabetes_y_pred = regr.predict(X_test)

# 将测试结果以图标的方式显示出来
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
