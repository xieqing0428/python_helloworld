# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_06_06.py
@time: 2019-01-15 21:34

6-6 调查：
在6.3.1节编写的程序favorite_languages.py中执行以下操作。
创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。
对于还未参与调查的人，打印一条消息邀请他参与调查

"""
favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'ruby',
      'phil': 'python',
      }
users = ['jen', 'sarah', 'edward', 'phil', 'tony']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
for user in users:
    if user in favorite_languages:
        print(user.title() + "谢谢！")
    else:
        print(user.title() + "能做个调查吗？")
