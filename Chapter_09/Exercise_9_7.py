# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: 9-7.py
@time: 2019-01-12 20:31

9-7 管理员：
管理员是一种特殊的用户。
编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
添加一个名为privileges的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
编写一个名为show_privileges()的方法，它显示管理员的权限。
创建一个Admin实例，并调用这个方法。

"""


class User:

    def __init__(self, first_name, last_name, user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        print('用户姓名为：' + self.first_name.title() + self.last_name.title())
        print('该用户的简介：' + self.user_info)

    def greet_user(self):
        print(self.first_name.title() + self.last_name.title() + '你好呀！')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, user_info):
        super().__init__(first_name, last_name, user_info)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("管理员的权限有：")
        for privilege in self.privileges:
            print(privilege.title())


admin = Admin('xie', 'qing', 'dalao')
admin.show_privileges()
