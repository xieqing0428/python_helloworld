# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_06_04.py
@time: 2019-01-12 23:26

6-4 词汇表2：
既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，
将其中的一系列print语句替换为一个遍历字典中的键和值的循环。
确定该循环正确无误后，再在词汇表中添加5个Python术语。
当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中

"""
coding = {
    'print': '打印',
    'if': '条件语句',
    'for': '循环语句',
    'and': '和',
    'or': '或',
}
for key, value in coding.items():
    print(key + ":" + value)

coding['del'] = '删除'
for key, value in coding.items():
    print(key + ":" + value)
