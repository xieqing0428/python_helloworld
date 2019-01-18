# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_15.py
@time: 2019-01-17 21:20

8-15 打印模型：
将示例print_models.py中的函数放在另一个名为printing_functions.py的文件中；
在print_models.py的开头编写一条import语句，并修改这个文件以使用导入的函数

"""
import python_helloworld.section_i.chapter_08.example.printing_functions as module

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

module.print_models(unprinted_designs, completed_models)
module.show_completed_models(completed_models)
