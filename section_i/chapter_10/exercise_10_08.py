# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_10_08.py
@time: 2019-01-13 21:13

10-8 猫和狗：
创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，
在第二个文件中至少存储三条狗的名字。
编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
将这些代码放在一个try-except代码块中，
以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息。
将其中一个文件移到另一个地方，并确认except代码块中的代码将正确地执行

"""

# 诶嘿嘿 10-8 幸运数字

fileCats = "example_15/cats.txt"
fileDogs = "example_15/dogs.txt"
fileErrors = "example_15/errors.txt"

with open(fileCats) as file_cats:
    for line in file_cats:
        print(line.rstrip())

with open(fileDogs) as file_dogs:
    for line in file_dogs:
        print(line.rstrip())

try:
    with open(fileErrors) as file_errors:
        for line in file_errors:
            print(line.rstrip())
except FileNotFoundError:
    print("找不到errors文件")
