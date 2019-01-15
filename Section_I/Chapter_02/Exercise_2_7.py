# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_2_7.py
@time: 2019-01-14 19:26

2-7 剔除人名中的空白：
存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"和"\n"各一次。

打印这个人名，以显示其开头和末尾的空白。
然后，分别使用剔除函数lstrip()、rstrip()和strip()对人名进行处理，并将结果打印出来。

"""
username = "\tAlessa0\n"

print("原人名：" + username)
print("lstrip()：" + username.lstrip())
print("rstrip()：" + username.rstrip())
print("strip()：" + username.strip())
