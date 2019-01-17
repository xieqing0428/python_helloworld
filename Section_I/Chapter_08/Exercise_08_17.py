# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_08_17.py
@time: 2019-01-17 22:02

"""


def make_shirt(size, description):
    print("T恤的尺码是：" + str(size) + ", 印到T恤的字样为：" + str(description))


make_shirt('M', '你猜')
make_shirt(size='M', description='你猜')


def describe_city(city='Reykjavik', country='Iceland'):
    print(city + " is in " + country)


describe_city()
describe_city('Shanghai', 'China')
describe_city('xx')


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
