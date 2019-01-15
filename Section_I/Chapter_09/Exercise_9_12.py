# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_9_12.py
@time: 2019-01-12 22:35

9-12 多个模块：
将User类存储在一个模块中，并将Privileges和Admin类存储在另一个模块中。
再创建一个文件，在其中创建一个Admin实例，并对其调用方法show_privileges()，以确认一切都依然能够正确地运行

"""

from HelloWorld.Section_I.Chapter_09 import Admin

admin = Admin('xie', 'qing', 'dalao')
admin.privileges.show_privileges()
