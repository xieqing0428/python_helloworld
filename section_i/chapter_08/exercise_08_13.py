# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_08_13.py
@time: 2019-01-17 21:09

8-13 用户简介：
复制前面的程序user_profile.py，在其中调用build_profile()来创建有关你的简介；
调用这个函数时，指定你的名和姓，以及三个描述你的键-值对

"""
profile = {}


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""

    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('XIE', 'QING',
                             location='Shanghai',
                             field=['Java', 'Python', '数据'],
                             state='找工作')
print(user_profile)
