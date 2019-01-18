# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_extend.py
@time: 2019-01-12 22:47

"""

from HelloWorld.Section_I.Chapter_09 import User


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

