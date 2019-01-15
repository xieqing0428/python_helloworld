# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_10_9.py
@time: 2019-01-13 21:22

10-9 沉默的猫和狗：
修改你在练习10-8中编写的except代码块，让程序在文件不存在时一言不发

"""

fileErrors = "Example/errors.txt"

try:
    with open(fileErrors) as file_errors:
        for line in file_errors:
            print(line.rstrip())
except FileNotFoundError:
    pass
