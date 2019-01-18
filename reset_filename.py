# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: reset_filename.py
@time: 2019-01-18 17:29

"""
import os    # os模块包含了对系统操作的一些API

# 这里是存放你所需要修改的文件的路径，即你要修改的文件在file文件夹下
up_dir = "/Users/alessa0/PycharmProjects/test/helloworld/section_iii/"

files_list = os.listdir(up_dir)                     # os.listdir函数返回一个存放该路径下文件名的列表

for index, name in enumerate(files_list):           # 遍历文件名列表，enumerate函数放回元素值和对应索引
    old_name = up_dir + name                        # 原来的文件名
    new_name = old_name.lower()      # 对新文件名进行定义，这里可以根据自己的需要来定义
    os.rename(old_name, new_name)
