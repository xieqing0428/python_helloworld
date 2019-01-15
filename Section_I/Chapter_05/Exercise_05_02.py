# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_05_02.py
@time: 2019-01-15 17:23

5-2 更多的条件测试：
你并非只能创建10个测试。
如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。
对于下面列出的各种测试，至少编写一个结果为True和False的测试。

检查两个字符串相等和不等。
使用函数lower()的测试。
检查两个数字相等、不等、大于、小于、大于等于和小于等于。
使用关键字and和or的测试。
测试特定的值是否包含在列表中。
测试特定的值是否未包含在列表中

"""
a = 'case'
b = 'Case'
c = 'case'
d = 1
e = 2
f = 1
g = [1, 2]

print(a == c)
print(a == b)
print(a.lower() == b.lower())
print(d == f)
print(d != e)
print(e > d)
print(f < e)
print(e >= d)
print(f <= e)
print(a == c and d == f)
print(a == c or d == e)
print(f in g)
print(3 not in g)
