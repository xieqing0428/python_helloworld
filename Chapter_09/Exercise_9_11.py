# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_9_11.py
@time: 2019-01-12 22:33

9-11 导入Admin类：
以为完成练习9-8而做的工作为基础，将User、Privileges和Admin类存储在一个模块中，
再创建一个文件，在其中创建一个Admin实例并对其调用方法show_privileges()，以确认一切都能正确地运行。

"""
from HelloWorld.Chapter_09.Exercise_9_8 import Admin

admin = Admin('xie', 'qing', 'dalao')
admin.privileges.show_privileges()
