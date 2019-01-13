# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: 9-6.py
@time: 2019-01-12 20:21

9-6 冰淇淋小店：
冰淇淋小店是一种特殊的餐馆。
编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。
这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。
创建一个IceCreamStand实例，并调用这个方法

"""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name, type, number_served"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印前述两项信息"""
        print("餐馆的名字叫" + self.restaurant_name.title())
        print("餐馆的烹调类别是" + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("就餐人数为" + str(self.number_served))

    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        print("该餐馆可能接待的就餐人数为" + str(self.number_served))


class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["香草味", "草莓味", "芒果味"]

    def show_flavors(self):
        print("本店提供如下口味冰淇淋:")
        for flavor in self.flavors:
            print(flavor.title())


iceCreamShop = IceCreamStand("冰淇淋小店", "冰淇淋")
iceCreamShop.show_flavors()
