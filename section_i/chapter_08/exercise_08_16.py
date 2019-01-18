# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_16.py
@time: 2019-01-17 21:54

8-16 导入：
选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。
在主程序文件中，使用下述各种方法导入这个函数，再调用它：

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

"""
import helloworld.section_i.chapter_08.example.printing_functions
from helloworld.section_i.chapter_08.example.printing_functions \
    import show_completed_models
from helloworld.section_i.chapter_08.example.printing_functions \
    import print_models as fn
import helloworld.section_i.chapter_08.example.printing_functions as module
from helloworld.section_i.chapter_08.example.printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

helloworld.section_i.chapter_08.example.printing_functions.print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
module.print_models(unprinted_designs, completed_models)
module.show_completed_models(completed_models)
show_completed_models(completed_models)
fn(unprinted_designs, completed_models)
