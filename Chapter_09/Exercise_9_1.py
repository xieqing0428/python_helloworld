# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: 9-1.py
@time: 2019-01-12 15:13

9-1 餐馆：
创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业
根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

"""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name, type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印前述两项信息"""
        print("餐馆的名字叫" + self.restaurant_name.title())
        print("餐馆的烹调类别是" + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")


restaurant = Restaurant('全聚德', '烤鸭')
print('餐馆叫' + restaurant.restaurant_name.title())
print('这家店做' + restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()

