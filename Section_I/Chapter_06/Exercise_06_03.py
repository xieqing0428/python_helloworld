# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_06_03.py
@time: 2019-01-15 21:02

6-3 词汇表：
Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。

想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，
并将它们的含义作为值存储在词汇表中。
以整洁的方式打印每个词汇及其含义。
为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
也可在一行打印词汇，再使用换行符（\n）插入一个空行，然后在下一行以缩进的方式打印词汇的含义

"""
coding = {
    'print': '打印',
    'if': '条件语句',
    'for': '循环语句',
    'and': '和',
    'or': '或',
}
key = 'print'
print(key + ": " + coding[key])
print(key + "\n\t" + coding[key])
key = 'if'
print(key + ": " + coding[key])
print(key + "\n\t" + coding[key])
key = 'for'
print(key + ": " + coding[key])
print(key + "\n\t" + coding[key])
key = 'and'
print(key + ": " + coding[key])
print(key + "\n\t" + coding[key])
key = 'or'
print(key + ": " + coding[key])
print(key + "\n\t" + coding[key])
