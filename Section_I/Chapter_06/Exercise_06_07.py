# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_06_07.py
@time: 2019-01-15 21:42

6-7 人：
在为完成练习6-1而编写的程序中，再创建两个表示人的字典，
然后将这三个字典都存储在一个名为people的列表中。
遍历这个列表，将其中每个人的所有信息都打印出来

"""
people = {
    'user1': {
        'first_name': 'ming',
        'last_name': 'xiao',
        'age': '18',
        'city': 'nanjing',
    },
    'user2': {
        'first_name': 'ming',
        'last_name': 'hong',
        'age': '28',
        'city': 'tianjing',
    },
    'user3': {
        'first_name': 'ming',
        'last_name': 'wang',
        'age': '38',
        'city': 'shanghai',
    },
}
for user, info in people.items():
    print("User:" + user)
    print("姓名：" + info['first_name'] + info['last_name'])
    print("年龄:" + info['age'])
    print("居住地点:" + info['city'])