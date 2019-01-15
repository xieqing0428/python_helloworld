# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_09_08.py
@time: 2019-01-12 20:46

9-8 权限：
编写一个名为Privileges的类，它只有一个属性——privileges，
其中存储了练习9-7所说的字符串列表。
将方法show_privileges()移到这个类中。
在Admin类中，将一个Privileges实例用作其属性。
创建一个Admin实例，并使用方法show_privileges()来显示其权限。

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
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("管理员的权限有：")
        for privilege in self.privileges:
            print(privilege.title())


admin = Admin('xie', 'qing', 'dalao')
admin.privileges.show_privileges()
